from unittest import TestCase

from lib.musical.feature_utils import neg, region
from lib.musical.features import *


class TestFeatures(TestCase):

    def setUp(self):
        self.a = [3,2,1,2,3]

    def test_normalize(self):
        n_fn = normalize(1,3)(fn)
        self.assertEquals(1, n_fn(self.a, 0))
        self.assertEquals(0, n_fn(self.a, 2))

    def test_neg(self):
        n_fn = normalize(1,3)(fn)

        self.assertEquals(0, neg(n_fn)(self.a, 0))
        self.assertEquals(1, neg(n_fn)(self.a, 2))

    def test_region(self):

        self.assertEquals(1.8, region(fn)(self.a, 2))

def fn(array, i):
    return array[i]