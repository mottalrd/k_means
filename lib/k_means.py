import random
import numpy as np
from numpy.linalg import norm
from collections import namedtuple
from recordtype import recordtype

Cluster = recordtype('Cluster', ('center', 'members', 'converged'))

class KMeans:
    def __init__(self, X, k, iters = 1):
        self.X = X
        self.k = k
        self.iters = iters
        self.cost = None
        self.clusters = []

    def fit(self):
        self.clusters = self.__find_centers(self.X, self.k, self.clusters)
        self.cost = self.__cost(self.clusters)

        for _ in xrange(self.iters - 1):
            new_clusters = self.__find_centers(self.X, self.k, self.clusters)
            new_cost = self.__cost(self.clusters)

            if (new_cost < self.cost):
                self.clusters = new_clusters
                self.cost = new_cost

        return self.clusters

    def __find_centers(self, X, k, clusters):
        self.__init_clusters(clusters, X, k)
        self.__assign_members_to(clusters, X)
        self.__compute_center_for(clusters)

        while not self.__has_converged(clusters):
            for cluster in clusters:
                cluster.members = []
            self.__assign_members_to(clusters, X)
            self.__compute_center_for(clusters)

        return clusters

    def __init_clusters(self, clusters, X, k):
        for c in np.array(random.sample(X, k)):
            clusters.append(Cluster(center = c, members = [], converged = False))

    def __assign_members_to(self, clusters, X):
        centers = map(lambda c: c.center, clusters)

        for x in X:
            closest_center = centers[norm(centers - x, axis=-1).argmin()]
            cluster = filter(lambda c: (c.center == closest_center).all(), clusters)[0]
            cluster.members.append(x)

    def __compute_center_for(self, clusters):
        for cluster in clusters:
            c = np.array(cluster.members).mean(axis=0)
            if (c == cluster.center).all():
                cluster.converged = True
            cluster.center = c

    def __has_converged(self, clusters):
        return np.array([cluster.converged for cluster in clusters]).all()

    def __cost(self, clusters):
        result = 0
        for cluster in clusters:
            result += ((cluster.members - cluster.center) ** 2).sum()
        return result
