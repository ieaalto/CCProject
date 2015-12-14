import math


def normalize(v):
    minimum, maximum = min(v), max(v)
    v = [(k-minimum)/(maximum-minimum) for k in v]

    return v

def normalize_common_magnitude(vectors):
    all_values = [value for vect in vectors for value in vect]
    minimum, maximum = min(all_values), max(all_values)

    for i in range(len(vectors)):
        vectors[i] = [(k-minimum)/(maximum-minimum) for k in vectors[i]]

    return vectors
