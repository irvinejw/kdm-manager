#!/usr/bin/python2.7

from bson.objectid import ObjectId
from copy import copy
from datetime import datetime, timedelta
import json
from bson import json_util

from flask import request, Response

import utils

#
#   Base classes for game assets are here. Also, special exceptions for those
#       classes live here as well.
#

class AssetMigrationError(Exception):
    """ Handler for asset migration/conversion errors. """

    def __init__(self, message="An error occurred while migrating this asset!"):
        self.logger = utils.get_logger()
        self.logger.exception(message)
        Exception.__init__(self, message)

class AssetInitError(Exception):
    """ Handler for asset-based errors. """

    def __init__(self, message="An error occurred while initializing this asset!"):
        self.logger = utils.get_logger()
        self.logger.exception(message)
        Exception.__init__(self, message)

class AssetLoadError(Exception):
    """ Handler for asset-based errors. """

    def __init__(self, message="Asset could not be retrieved from mdb!"):
        self.logger = utils.get_logger()
        self.logger.exception(message)
        Exception.__init__(self, message)


class AssetCollection():
    """ The base class for game asset objects, i.e. working with the dict assets
    in the assets/ folder.

    Each model in the models/ folder should have a method that subclasses this
    base class.

    All asset objects that use this as their base class MUST define their own
    self.assets dict (preferably in their __init__() method). """

    def __init__(self):
        """ sets misc attributes of the collection's assets dict. """
        self.logger = utils.get_logger()
        for a in self.assets.keys():
            self.assets[a]["handle"] = a
            if hasattr(self, "type"):
                self.assets[a]["type"] = self.type

    def get_handles(self):
        """ Dumps all asset handles, i.e. the list of self.assets keys. """
        return sorted(self.assets.keys())

    def get_names(self):
        """ Dumps all asset 'name' attributes, i.e. a list of name values. """
        return sorted([self.assets[k]["name"] for k in self.get_handles()])

    def get_asset(self, handle):
        """ Return an asset dict based on a handle. Return None if the handle
        cannot be retrieved. """

#        if not hasattr(self, "logger"):
#            raise AttributeError("AssetCollection object has no logger! %s -> %s" % (self, dir(self)))

        try:
            asset = self.assets[handle]
            if not "handle" in asset.keys():
                asset["handle"] = handle
#            self.logger.debug(asset)
            return asset
        except Exception as e:
            self.logger.exception(e)
            return None

    def get_asset_from_name(self, name, case_sensitive=False):
        """ Tries to return an asset dict by looking up "name" attributes within
        the self.assets. dict. Returns None if it fails.

        By default, the mactching here is NOT case-sensitive: everything is
        forced to upper() to allow for more permissive matching/laziness. """

        if type(name) not in [str,unicode]:
            self.logger.error("get_asset_from_name() cannot proceed! '%s' is not a str or unicode object!" % name)
            raise AssetInitError("The get_asset_from_name() method requires a str or unicode type name!")

        name = name.strip()
        if not case_sensitive:
            name = name.upper()

        name_lookup = {}
        for a in self.assets.keys():
            if "name" in self.assets[a]:
                if case_sensitive:
                    name_lookup[self.assets[a]["name"]] = a
                elif not case_sensitive:
                    asset_name_upper = self.assets[a]["name"].upper()
                    name_lookup[asset_name_upper] = a

        if name in name_lookup.keys():
            return self.get_asset(name_lookup[name])
        else:
            return None


    def request_response(self, req):
        """ Processes a JSON request for a specific asset from the collection,
        initializes the asset (if it can) and then calls the asset's serialize()
        method to create an HTTP response. """

        a_name = req.get("name", None)
        a_handle = req.get("handle", None)

        try:
            if a_handle is not None:
                A = self.AssetClass(a_handle)
            elif a_name is not None:
                A = self.AssetClass(name=a_name)
            else:
                return utils.http_422
        except Exception as e:
            self.logger.exception(e)
            return utils.http_404

        return Response(response=A.serialize(), status=200, mimetype="application/json")




class GameAsset():
    """ The base class for initializing individual game asset objects. All of
    the specific models in the models/ folder will sub-class this model for
    their generally available methods, etc.

    """

    def __init__(self, handle=None, name=None):

        # initialize basic vars
        self.logger = utils.get_logger()
        self.name = name
        self.handle = handle

    def __repr__(self):
        return "%s object '%s' (assets.%ss['%s'])" % (self.type.title(), self.name, self.type, self.handle)


    def initialize(self):
        """ Call this method to initialize the object. """

        if self.handle is not None:
            self.initialize_from_handle()
        elif self.name is not None:
            self.initialize_from_name()
        elif handle is None and name is None:
            raise AssetInitError("Asset objects must be initialized with 'handle' or 'name' kwargs.")
        else:
            raise AssetInitError()


    def initialize_asset(self, asset_dict):
        """ Pass this a valid asset dictionary to set the object's attributes
        with a bunch of exec calls. """

        if type(asset_dict) != dict:
            raise AssetInitError("Asset objects may not be initialized with a '%s' type object!" % type(asset_dict))

        for k, v in asset_dict.iteritems():
            if type(v) == str:
                exec """self.%s = "%s" """ % (k,v)
            else:
                exec "self.%s = %s" % (k,v)


    def initialize_from_handle(self):
        """ If we've got a not-None handle, we can initiailze the asset object
        by checking self.assets to see if our handle is a valid key.
        If we can't find a valid key, throw an exception. """

        # sanity warning
        if " " in self.handle:
            self.logger.warn("Asset handle '%s' contains whitespaces. Handles should use underscores." % self.handle)

        asset_dict = self.assets.get_asset(self.handle)
        self.initialize_asset(asset_dict)

        if self.name is None:
            raise AssetInitError("Asset handle '%s' could not be retrieved!" % self.handle)


    def initialize_from_name(self):
        """ If we've got a not-None name, we can initiailze the asset object
        by checking self.assets to see if we can find an asset whose "name"
        value matches our self.name. """


        # sanity warning
        if "_" in self.name:
            self.logger.warn("Asset name '%s' contains underscores. Names should use whitespaces." % self.name)

        lookup_dict = {}
        for asset_handle in self.assets.get_handles():
            asset_dict = self.assets.get_asset(asset_handle)
            lookup_dict[asset_dict["name"]] = asset_handle

        if self.name in lookup_dict.keys():
            self.handle = lookup_dict[self.name]
            self.initialize_from_handle()

        if self.handle is None:
            raise AssetInitError("Asset handle '%s' could not be retrieved!" % self.handle)


    def serialize(self):
        """ Allows the object to represent itself as JSON by transforming itself
        into a JSON-safe dict. """

        shadow_self = copy(self)

        for banned_attrib in ["logger", "assets"]:
            if hasattr(shadow_self, banned_attrib):
                delattr(shadow_self, banned_attrib)

        return json.dumps(shadow_self.__dict__, default=json_util.default)


    #
    # look-up and manipulation methods below
    #

    def get(self, attrib):
        """ Wrapper method for trying to retrieve asset object attributes.
        Returns a None type value if the requested attrib doesn't exist. """

        try:
            return getattr(self, attrib)
        except:
            return None



class UserAsset():
    """ The base class for all user asset objects, such as survivors, sessions,
    settlements and users. All user asset controllers in the 'models' module
    use this as their base class. """


    def __repr__(self):
        """ Default __repr__ method for all user assets. Note that you should
        PROBABLY define a __repr__ for your individual assets, if for no other
        reason than to make the logs look cleaner. """

        try:
            exec 'repr_name = self.%s["name"]' % (self.collection[:-1])
        except:
            self.logger.warn("UserAsset object has no 'name' attribute!")
            repr_name = "UNKNOWN"
        return "%s object '%s' [%s]" % (self.collection, repr_name, self._id)


    def __init__(self, collection=None, _id=None):

        # initialize basic vars
        self.logger = utils.get_logger()

        if collection is not None:
            self.collection = collection
        elif hasattr(self,"collection"):
            pass
        else:
            err_msg = "User assets (settlements, users, etc.) may not be initialized without specifying a collection!"
            self.logger.error(err_msg)
            raise AssetInitError(err_msg)

        # use attribs to determine whether the object has been loaded
        self.loaded = False

        if _id is None:
            self.new()
            _id = self._id

        try:
            self._id = ObjectId(_id)
            self.load()
            self.loaded = True
        except Exception as e:
            self.logger.error("Could not load _id '%s' from %s!" % (_id, self.collection))
            self.logger.exception(e)
            raise


    def save(self):
        """ Saves the user asset back to either the 'survivors' or 'settlements'
        collection in mdb, depending on self.collection. """

        if self.collection == "settlements":
            utils.mdb.settlements.save(self.settlement)
        elif self.collection == "survivors":
            utils.mdb.survivors.save(self.survivor)
        elif self.collection == "users":
            utils.mdb.users.save(self.user)
        else:
            raise AssetLoadError("Invalid MDB collection for this asset!")
        self.logger.info("Saved %s to mdb.%s successfully!" % (self, self.collection))


    def load(self):
        """ Retrieves an mdb doc using self.collection and makes the document an
        attribute of the object. """

        mdb_doc = utils.mdb[self.collection].find_one({"_id": self._id})
        if mdb_doc is None:
            raise AssetLoadError()

        if self.collection == "settlements":
            self.settlement = mdb_doc
            self._id = self.settlement["_id"]
        elif self.collection == "survivors":
            self.survivor = mdb_doc
            self._id = self.survivor["_id"]
        elif self.collection == "users":
            self.user = mdb_doc
            self._id = self.user["_id"]
            self.login = self.user["login"]
        else:
            raise AssetLoadError("Invalid MDB collection for this asset!")


    def return_json(self):
        """ Calls the asset's serialize() method and creates a simple HTTP
        response. """
        return Response(response=self.serialize(), status=200, mimetype="application/json")


    def get_request_params(self):
        """ Checks the incoming request (from Flask) for JSON and tries to add
        it to self. """

        params = {}

        if request.method == "GET":
            self.logger.warn("%s:%s get_request_params() call is being ignored!" % (request.method, request.url))
            return False

        if request.get_json() is not None:
            try:
                params = dict(request.get_json())
            except ValueError:
                self.logger.warn("%s request JSON could not be converted to dict!" % request.method)
                params = request.get_json()
        else:
            self.logger.error("%s request did not contain JSON data!" % request.method)
            self.logger.error("Request URL: %s" % request.url)

        self.params = params


    #
    #   get/set methods for User Assets below here
    #

    def get_serialize_meta(self):
        """ Sets the 'meta' dictionary for the object when it is serialized. """

        output = copy(utils.api_meta)
        try:
            output["meta"]["object"]["version"] = self.object_version
        except Exception as e:
            self.logger.error("Could not create 'meta' dictionary when serializing object!")
            self.logger.exception(e)
            self.logger.warn(utils.api_meta)
            self.logger.warn(output["meta"])
        return output


    def get_current_ly(self):
        """ Convenience/legibility function to help code readbility and reduce
        typos, etc. """

        return int(self.settlement["lantern_year"])

    #
    #   asset update methods below
    #

    def log_event(self, msg, event_type=None):
        """ Logs a settlement event to mdb.settlement_events. """
        d = {
            "created_on": datetime.now(),
            "created_by": None,
            "settlement_id": self.settlement["_id"],
            "ly": self.settlement["lantern_year"],
            "event": msg,
            "event_type": event_type,
        }
        utils.mdb.settlement_events.insert(d)
        self.logger.debug("%s event: %s" % (self, msg))




