import math
import random

from config import settings
from lib.genetic.abstract_genotype import AbstractGenotype
from lib.musical.note import Note
from lib.musical.notes import Notes
from lib.markov.chains import melody
import uuid


class MusicalGenotype(AbstractGenotype):
    '''
    Genotype representing a melody. Fitness function matches the features to data.
    '''


    def __init__(self, data, length=10, notes=None):
        '''
        :param data: dictionary containing pairs of dictionary keyword and an Intervals object.
        :param length: an initial length. Won't stay constant after mutations and crossovers.
        :param notes: a Notes object. Randomized if not specified.
        :return:
        '''
        self.data = data
        self.notes = notes if notes else Notes.get_random(length)
        self.id = uuid.uuid4()

        super().__init__(self.get_fitness_funcs(), [self.randomize_notes])

    def get_fitness_funcs(self):
        '''
        For each feature for each mood in data, return a fitness function.
        :return: a list of functions
        '''
        funcs = []
        for mood in self.data:
            mood_data = self.data[mood]
            for feature in settings.MOOD_FEATURES[mood]:
                funcs.append(self.feature_to_data_fitness(feature, mood_data))

        return funcs


    def feature_to_data_fitness(self, feature, data):
        '''
        Return a fitness function for the feature that matches the feature with an Intervals object.
        :param feature: a function f(genotype, i)
        :param data: an Intervals object
        :return: a fitness function.
        '''
        def fitness_func():
            seqs = self.notes.get_seqs(data)
            s = 0
            n = 0
            for i in range(len(seqs)):
                s += 1/(self.sequence_fitness(feature, seqs[i],  data[i].diff)*seqs[i][2] + 0.0001)
                n += seqs[i][2]

            return n/s

        return fitness_func

    def sequence_fitness(self, feature, seq, difference):
        '''
        Returns the fitness for a sequence and a feature.
        :param feature:
        :param seq:
        :param difference:
        :return: mean deviation, float.
        '''

        diff = difference / (seq[1]+1 - seq[0])
        deviations = [math.fabs(diff - _feature_difference(feature, self, i)()) for i in range(seq[0], seq[1])]

        return sum(deviations)/len(deviations)

    def crossover(self, other):
        '''
        Return a crossover genotype of self and another MusicalGenotype object. Splits the Notes objects at random points and concatenates them.
        :param other:
        :return: a new MusicalGenotype
        '''
        cut_point_a = _limited_random(self)
        cut_point_b = _limited_random(other)

        return MusicalGenotype(self.data, notes=Notes(self.notes[0:cut_point_a] + self.notes[cut_point_b:-1]))

    def limited_random(self, other):
        cut_point_b = random.randint(0, len(other.notes) if other.notes.duration < settings.MAX_LENGTH else len(
            other.notes) // 2)
        return cut_point_b

    def randomize_notes(self):
        '''
        Randomizes a random number of notes. Used a mutation function.
        '''
        n = random.randint(0, len(self))
        for k in range(0, n):
            i = random.randint(0, len(self))
            self.notes[0] = Note.get_random()

    def __getitem__(self, item):
        return self.notes[item]

    def __len__(self):
        return len(self.notes)

    def __repr__(self):
        return str([str(note) for note in self.notes])

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return hash(self) == hash(other)


def _feature_difference(feature, genotype, i):
    def _feature_diff():
        return feature(genotype, i)- feature(genotype, i-1) if i > 0 else 1

    return _feature_diff

def _limited_random(other):
        cut_point_b = random.randint(0, len(other.notes) if other.notes.duration < settings.MAX_LENGTH else len(
            other.notes) // 2)
        return cut_point_b

