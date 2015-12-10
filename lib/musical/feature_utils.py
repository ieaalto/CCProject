import math

import config.musical


def norm(fn, min, max):
    def normalized(genotype, i):
        return (fn(genotype, i)-min)/(max-min)

    return normalized


def normalize(min, max):
    def normalizer(fn):
        return norm(fn, min, max)

    return normalizer


def neg(fn):
    def negation(genotype, i):
        return math.fabs(fn(genotype, i)-1)

    return negation


def region(fn):
    def regional_mean(genotype, i):
        n = 0
        k = 0
        for j in range(-config.musical.REGION_RADIUS, config.musical.REGION_RADIUS +1):
            if len(genotype) > i+j >= 0 :
                weigth = math.pow(config.musical.REGION_FALLOFF, math.fabs(j))
                n += weigth
                k += weigth*fn(genotype, i+j)

        return k/n

    return regional_mean