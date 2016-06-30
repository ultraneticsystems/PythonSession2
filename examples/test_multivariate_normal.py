import numpy as np
import multivariate_normal

def test_pdf():
    mean = np.array([0., 0.])
    sigma = np.array([[1., 0.], [0., 1.]])
    value = np.array([0., 0.])
    dist = multivariate_normal.JointNormalDistribution(mean, sigma)
    print dist.pdf(value)
    assert dist.pdf(value) == 0.15915494309189535

