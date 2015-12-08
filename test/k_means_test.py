import init_tests
import pytest
from k_means import *
import numpy as np

class TestKMeans():

    @pytest.fixture
    def data_with_two_clusters(self):
        return np.array([
            [1, 1],
            [2, 2],
            [3, 3],
            [10, 10],
            [11, 11],
            [12, 12]
        ])

    def test_has_two_clusters(self, data_with_two_clusters):
        assert len(k_means(data_with_two_clusters, 2)['mu']) == 2

    def test_has_three_points_each_clusters(self, data_with_two_clusters):
        assert len(k_means(data_with_two_clusters, 2)['clusters'][0]) == 3
        assert len(k_means(data_with_two_clusters, 2)['clusters'][1]) == 3
