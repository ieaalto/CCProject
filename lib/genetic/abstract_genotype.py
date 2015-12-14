import random

class AbstractGenotype:
    changed = True
    _latestFitness = None

    def __init__(self, fitness_funcs, mutation_funcs, weights=None):
        self.fitness_funcs = fitness_funcs
        self.mutation_funcs = mutation_funcs

        self.weights = weights if weights else [1 / len(fitness_funcs) for i in range(len(fitness_funcs))]
        if len(self.weights) != len(self.fitness_funcs): raise ValueError("Weigth must be given for each fitness function!")

    def get_fitness(self):
        if self.changed:
            self._latestFitness = sum([self.fitness_funcs[i]() * self.weights[i] for i in range(len(self.fitness_funcs))])
            self.changed = False

        return self._latestFitness

    def mutate(self):
        random.choice(self.mutation_funcs)()
        self.changed = True

    def crossover(self, other):
        raise NotImplementedError()

