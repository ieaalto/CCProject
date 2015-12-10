import random
from lib.genetic.abstract_genotype import AbstractGenotype


class TestGenotype(AbstractGenotype):

    def __init__(self, target, string = None):
        self.string = str(random.randint(0, 9999)).zfill(4) if string == None else string
        self.target = target

        super().__init__([self.shared_digits_with_target], [self.change_one_char])

    def shared_digits_with_target(self):
        score = 0
        for i in range(4):
            if self.string[i] == self.target[i] :
                score += 1
        return score

    def change_one_char(self):
        i = random.randint(0,3)
        str_list = list(self.string)

        str_list[i] = str(random.randint(0,9))

        self.string = "".join(str_list)

    def crossover(self, other):
        return TestGenotype(self.fitness_params, string=self.string[0:2]+other.string[2:4])

    def __str__(self):
        return self.string




