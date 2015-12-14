from lib.musical.features import *

##Testing
MOCK = True

##Semantics
MOODS = {
}

##Genetic
POPULATION = 500
GENERATIONS = 30

##Features

MOOD_FEATURES = {
                "test" : [note_time, mean_velocity, neg(pitch_variance)]
}

MAX_LENGTH = 400
##Data
ROUNDING = 2 ##Round to n decimal places

##Markov chains
MARKOV_DATA = "notes.txt"
ORDER = 2
