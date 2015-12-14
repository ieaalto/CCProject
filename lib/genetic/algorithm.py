import math

from random import *


class Genetic:
    '''
    A basic genetic algorithm.
    '''

    def __init__(self, genotype_generator, pop_size, generations, selection, mutation_probability=0.05):
        '''
        :param genotype_generator: A GenotypeFactory object.
        :param pop_size: the size of each generation.
        :param generations: the number of generations.
        :param selection: the selection policy. Should be a function that it is given a Genetic object as an argument.
        :param mutation_probability: The probability of mutation for each new genotype created by crossover.
        :return:
        '''
        self.genotype_generator = genotype_generator
        self.pop_size = pop_size
        self.generations = generations
        self.selection = selection
        self.mutation_probability = mutation_probability
        self.population = self.genotype_generator.generate(self.pop_size)

    def sort_by_fitness(self):
        self.population.sort(key=lambda g: math.fabs(g.get_fitness()))

    def repopulate(self):
        children = []
        while len(self.population) + len(children) < self.pop_size:
            a, b = _nonequal_randoms(len(self.population))

            children.append(self.population[a].crossover(self.population[b]))
        self.mutate(children)
        self.population += children

    def mutate(self, group):
        for g in group:
            if randrange(0,1) < self.mutation_probability:
                g.mutate()

    def evolve(self):
        for i in range(self.generations):
            self.population = self.selection(self)
            self.repopulate()

    def get_n_fittest(self, n):
        self.sort_by_fitness()
        return self.population[:n]


def truncation_selection(n):
    '''
    A simple selection method. Selects portion n of the genotypes by choosing the most fittest.
    :param n:
    :return:
    '''
    if 1 < n or n < 0:
        raise ValueError("n must be between 0 and 1")

    def select_n(genetic):
        m = int(genetic.pop_size*n)
        return genetic.get_n_fittest(m)

    return select_n

def _nonequal_randoms(max):
    a, b = 0, 0
    while a == b:
        a = randint(0,  max - 1)
        b = randint(0, max - 1)
    return a, b