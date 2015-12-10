from lib.musical.features import *

##Testing
MOCK = True

##Semantics
MOODS = {
            "negative": [],
            "positive":[],
            "active": [],
            "inactive": []
}

##Features

MOOD_FEATURES = {
                 #"negative": [],
                 #"positive": [],
                 #"active": [],
                 #"inactive": []
                "test" : [mean_pitch, mean_velocity]
}

##Data
ROUNDING = 2 ##Round to n decimal places