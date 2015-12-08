import init_tests
import pytest
from k_means import *
import numpy as np

class TestKMeans():

    @pytest.fixture
    def data(self):
        return np.array([
            [1, 1],
            [2, 2],
            [3, 3],
            [10, 10],
            [11, 11],
            [12, 12]
        ])

    @pytest.fixture
    def subject(self, data):
        return KMeans(data, 2).fit()

    def test_has_two_clusters(self, subject):
        assert len(subject) == 2

    def test_has_three_points_each_clusters(self, subject):
        assert len(subject[0].members) == 3
        assert len(subject[1].members) == 3
