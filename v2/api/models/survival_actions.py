#!/usr/bin/python2.7


from assets import survival_actions
import Models
import utils


class Assets(Models.AssetCollection):

    def __init__(self, *args, **kwargs):
        self.root_module=survival_actions
        Models.AssetCollection.__init__(self,  *args, **kwargs)

