import math

import config.musical


def norm(fn, min, max):
    '''
    Normalize the function fn's return values. Used as a decorator.
    :param fn:
    :param min:
    :param max:
    :return: a normalized function.
    '''
    def normalized(genotype, i):
        return (fn(genotype, i)-min)/(max-min)

    return normalized


def feature(min, max):
    '''
    Normalizes the funtion and caches the return values for efficiency. Used as a decorator.
    :param min: minimum value outputted by the original value. Will be 0.0 for the normalized function.
    :param max: maximum value, like before. Will be 1.0.
    '''

    vals = {}

    def normalizer(fn):
        def feature_fn(genotype, i):
            if genotype.changed or genotype not in vals:
                vals[genotype] = fn(genotype, i)

            return vals[genotype]

        return norm(feature_fn, min, max)

    return normalizer


def neg(fn):
    '''
    Negates the return values of the function fn. 1.0 will be 0.0 and vice versa. Normalize fn before use! Used as a decorator.
    :param fn:
    :return:
    '''
    def negation(genotype, i):
        return math.fabs(fn(genotype, i)-1)

    return negation

