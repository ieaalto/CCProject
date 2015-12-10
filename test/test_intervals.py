from unittest import TestCase
from lib.data_representation.intervals import Intervals

class TestIntervals(TestCase):

    def test_intervals_splits_trivial_vectors_correctly(self):
        ivs1 = Intervals([0,1,2,1,0])
        ivs2 = Intervals([2,1,0,1,2])

        self.assertEquals([[0,1,2], [1,0]], ivs1.get_intervals())
        self.assertEquals([[2,1,0], [1,2]], ivs2.get_intervals())

    def test_intervals_splits_simple_vectors_correctly(self):
        ivs1 = Intervals([0,1,2,1,0,1,2])
        ivs2 = Intervals([0,-1,-2,0,1,2,0])

        self.assertEquals([[0,1,2], [1,0], [1,2]], ivs1.get_intervals())
        self.assertEquals([[0,-1,-2], [0,1,2], [0]], ivs2.get_intervals())

    def test_intervals_splits_complex_vectors_correctly(self):
        ivs1 = Intervals([1,2,2,1])
        ivs2 = Intervals([0,1,2,1,1,2])
        ivs3 = Intervals([0,0,1,3,2,3,4,4,4,2])

        self.assertEquals([[1,2,2],[1]], ivs1.get_intervals())
        self.assertEquals([[0,1,2],[1,1],[2]], ivs2.get_intervals())
        self.assertEquals([[0,0],[1,3],[2],[3,4,4,4],[2]],ivs3.get_intervals())

    def test_intervals_calculates_correct_differences(self):
        ivs1 = Intervals([0,1,2,1,0])
        ivs2 = Intervals([0,1,2,1,0,1,2])
        ivs3 = Intervals([0,0,1,3,2,3,4,4,4,2])

        self.assertEquals([2,-2], ivs1.get_differences())
        self.assertEquals([2,-2, 2], ivs2.get_differences())
        self.assertEquals([0, 3, -1, 2, -2], ivs3.get_differences())