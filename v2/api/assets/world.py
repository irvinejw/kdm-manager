#!/usr/bin/python2.7

# general imports

# local imports
import utils

general = {
    "dead_survivors": {
        "name": "Dead survivors",
        "max_age": 5,
        "comment": "worldwide count of all dead survivors",
    },
    "live_survivors": {
        "max_age": 5,
        "name": "Live survivors",
        "comment": "worldwide count of all living survivors",
    },
    "total_survivors": {
        "name": "Total survivors",
        "comment": "worldwide count of all survivors, living and dead",
    },
    "total_settlements": {
        "name": "Total settlements",
        "comment": "worldwide count of all settlements, regardless of status",
    },
    "abandoned_settlements": {
        "name": "Abandoned settlements",
        "comment": "worldwide count of all abandoned and removed settlements",
    },
    "active_settlements": {
        "name": "Active settlements",
        "comment": "worldwide count of all settlements that have not been abandoned or removed"
    },
    "total_users": {
        "max_age": 30,
        "name": "Total users",
        "comment": "total of all registered users"
    },
    "total_users_last_30": {
        "max_age": 60,
        "name": "Total users in the last 30 days",
        "comment": "total of all users who have signed in during the last 30 days"
    },
    "new_settlements_last_30": {
        "max_age": 60,
        "name": "Total settlements created in the last 30 days",
        "comment": "total of all settlements with a 'created_on' date within the last 30 days"
    },
    "recent_sessions": {
        "max_age": 30,
        "name": "Recent sessions",
        "comment": "total of all sessions within the 'recent_session' horizon"
    },
    "max_pop": {
        "name": "Maximum population",
        "comment": "highest population across all settlements",
    },
    "max_death_count": {
        "name": "Maximum death count",
        "comment": "highest death count across all settlements",
    },
    "max_survival_limit": {
        "name": "Maximum Survival Limit",
        "comment": "highest survival limit across all settlements",
    },
    "avg_ly": {
        "max_age": 30,
        "name": "Average Lantern Year",
        "comment": "average ly across all settlements",
    },
    "avg_lost_settlements": {
        "max_age": 30,
        "name": "Average Lost Settlements",
        "comment": "average number of lost settlements across all settlements",
    },
    "avg_pop": {
        "max_age": 30,
        "name": "Average Population",
        "comment": "average population across all settlements",
    },
    "avg_death_count": {
        "max_age": 30,
        "name": "Average Death Count",
        "comment": "average death count across all settlements",
    },
    "avg_survival_limit": {
        "max_age": 30,
        "name": "Average Survival Limit",
        "comment": "average survival limit across all settlements",
    },
    "avg_milestones": {
        "max_age": 30,
        "name": "Average milestone story events",
        "comment": "average number of milestone story events across all settlements",
    },
    "avg_storage": {
        "max_age": 30,
        "name": "Average items in Settlement Storage",
        "comment": "average number of items in settlement storage across all settlements",
    },
    "avg_defeated_monsters": {
        "max_age": 30,
        "name": "Average defeated monsters",
        "comment": "average number of defeated monsters across all settlements",
    },
    "avg_expansions": {
        "max_age": 30,
        "name": "Average number of active expansions",
        "comment": "average number of active expansion modules across all settlements",
    },
    "avg_innovations": {
        "max_age": 30,
        "name": "Average Innovations",
        "comment": "average number of innovations across all settlements",
    },
    "avg_disorders": {
        "max_age": 30,
        "name": "Average Disorders",
        "comment": "average number of disorders per survivor across all survivors",
    },
    "avg_abilities": {
        "max_age": 30,
        "name": "Average Abilities and Impairments",
        "comment": "average number of abilities and impairments per survivor across all survivors",
    },
    "avg_hunt_xp": {
        "max_age": 30,
        "name": "Average Hunt XP",
        "comment": "average hunt xp per survivor across all survivors",
    },
    "avg_insanity": {
        "max_age": 30,
        "name": "Average Insanity",
        "comment": "average insanity per survivor across all survivors",
    },
    "avg_courage": {
        "max_age": 30,
        "name": "Average Courage",
        "comment": "average courage per survivor across all survivors",
    },
    "avg_understanding": {
        "max_age": 30,
        "name": "Average Understanding",
        "comment": "average understanding per survivor across all survivors",
    },
    "avg_fighting_arts": {
        "max_age": 30,
        "name": "Average Fighting Arts",
        "comment": "average number of fighting arts per survivor across all survivors",
    },
    "avg_user_settlements": {
        "max_age": 30,
        "name": "Average Settlements per user",
        "comment": "average number of settlements created per user across all users",
    },
    "avg_user_survivors": {
        "max_age": 30,
        "name": "Average Survivors per user",
        "comment": "average number of survivors created per user across all users",
    },
    "avg_user_avatars": {
        "max_age": 30,
        "name": "Average avatars per user",
        "comment": "average number of avatars uploaded per user across all users",
    },
    "total_multiplayer_settlements": {
        "max_age": 60,
        "name": "Total multiplayer settlements",
        "comment": "total number of settlements with more than one player",
    },
    "killboard": {
        "name": "Kill Board",
        "comment": "monster kills logged by all settlements",
    },
    "latest_kill": {
        "max_age": 3,
        "name": "Latest kill",
        "comment": "latest monster kill logged by any settlement",
    },
    "latest_survivor": {
        "max_age": 3,
        "name": "Latest Survivor",
        "comment": "most recently created survivor across all settlements",
    },
    "latest_fatality": {
        "max_age": 3,
        "name": "Latest fatality",
        "comment": "most recently killed survivor across all settlements",
    },
    "latest_settlement": {
        "max_age": 3,
        "name": "Latest Settlement",
        "comment": "most recently created settlement",
    },
    "top_survivor_names": {
        "max_age": 60,
        "name": "Top Survivor names",
        "comment": "most popular survivor names across all settlements",
    },
    "top_settlement_names": {
        "max_age": 60,
        "name": "Top Settlement names",
        "comment": "most popular survivor names across all settlements",
    },
    "principle_selection_rates": {
        "max_age": 60,
        "name": "Principle selection rates",
        "comment": "principle selection rates across all settlements",
    },
    "settlement_popularity_contest_expansions": {
        "max_age": 60,
        "name": "Popularity contest: expansions",
        "comment": "number of settlements where each available expansion module is enabled",
    },
    "settlement_popularity_contest_campaigns": {
        "max_age": 60,
        "name": "Popularity contest: campaigns",
        "comment": "number of settlements where each different campaign is enabled",
    },

}







