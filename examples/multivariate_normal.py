"""
This module contains methods for computing probabilities
and sampling form multivariate normal distributions
"""

import random
import numpy as np
import numpy.linalg as linalg


class JointNormalDistribution(object):
    def __init__(self, mean, variance):
        self.mu = mean
        self.sigma = variance
        self.dim = mean.size

    def pdf(self, x):
        """ Method for computing the probabillity of a vector w.r.t the
        distribution."""
        return (1./(np.sqrt((2.*np.pi)**self.dim) * linalg.det(self.sigma)) *
                    np.exp(-0.5*(x-self.mu).T * linalg.inv(self.sigma) *
                    (x-self.mu)))

    def sample(self, nsample):
        """ Method for generating samples from the distribution. """
        z = np.zeros(nsample)
        for i in range(nsample):
            z[i] = random.gauss(0, 1.)
        A = np.chelesky(self.sigma)
        return self.mu + np.dot(A, z)
