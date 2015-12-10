import math

from random import *


class Genetic:

    def __init__(self, genotype_generator, pop_size, generations, selection, mutation_probability=0.05):
        self.genotype_generator = genotype_generator
        self.pop_size = pop_size
        self.generations = generations
        self.selection = selection
        self.mutation_probability = mutation_probability
        self.population = self.genotype_generator.generate(self.pop_size)

    def sort_by_fitness(self):
        self.population.sort(key=lambda g: math.fabs(g.get_fitness()))

    def get_random(self):
        return self.population[randint(0,len(self.population)-1)]

    def repopulate(self):
        children = []
        while len(self.population) + len(children) < self.pop_size:
            children.append(self.get_random().crossover(self.get_random()))
        self.population += children

    def mutate(self):
        for g in self.population:
            if randrange(0,1) < self.mutation_probability:
                g.mutate()

    def evolve(self):
        for i in range(self.generations):
            self.population = self.selection(self)
            self.repopulate()
            self.mutate()

    def get_n_fittest(self, n):
        self.sort_by_fitness()
        return self.population[:n]


def truncation_selection(n):
    if 1 < n or n < 0:
        raise ValueError("n must be between 0 and 1")

    def select_n(genetic):
        m = int(genetic.pop_size*n)
        return genetic.get_n_fittest(m)

    return select_n