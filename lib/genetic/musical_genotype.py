import math
import random

from config import settings
from lib.genetic.abstract_genotype import AbstractGenotype
from lib.musical.note import Note
from lib.musical.notes import Notes


class MusicalGenotype(AbstractGenotype):

    def __init__(self, data, length=10, notes=None):
        self.data = data
        self.notes = notes if notes else Notes.get_random(length)

        super().__init__(self.get_fitness_funcs(), [self.randomize_note])

    def get_fitness_funcs(self):
        funcs = []
        for mood in self.data:
            mood_data = self.data[mood]
            for feature in settings.MOOD_FEATURES[mood]:
                funcs.append(self.feature_to_data_fitness(feature, mood_data))

        return funcs


    def feature_to_data_fitness(self, feature, data):
        def fitness_func():
            seqs = self.notes.get_seqs(data)
            sum = 0
            for i in range(len(seqs)):
                sum += self.sequence_fitness(feature, seqs[i],  data[i].diff)

            return sum/len(seqs)

        return fitness_func

    def sequence_fitness(self, feature, seq, difference):
        diff = difference / (seq[-1]+1 - seq[0])
        deviations = [math.fabs(diff - feature_difference(feature,self, i)()) for i in range(seq[0],seq[-1])]

        return sum(deviations)/len(deviations)

    def crossover(self, other):
        cut_point_a = random.randint(0, len(self.notes))
        cut_point_b = random.randint(0, len(other.notes)-1)

        return MusicalGenotype(self.data, notes=Notes(self.notes[0:cut_point_a] + self.notes[cut_point_b:-1]))

    def randomize_note(self):
        i = random.randint(0, len(self.notes))
        self.notes[0] = Note.get_random()

    def __getitem__(self, item):
        return self.notes[item]

    def __len__(self):
        return len(self.notes)

    def __repr__(self):
        return str([str(note) for note in self.notes])


def feature_difference(feature, genotype, i):
    def _feature_diff():
        return feature(genotype, i)- feature(genotype, i-1) if i > 0 else 1

    return _feature_diff

