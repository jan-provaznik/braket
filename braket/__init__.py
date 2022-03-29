import numpy
import functools

def dag (q):
    return numpy.conjugate(q.T)

def ket2dm (ket):
    return ket @ dag(ket)

def eyemat (nsys):
    dim = 2 ** nsys
    return numpy.eye(dim) / dim

def qubit (q):
    if (q == 0):
        return numpy.array([ 1, 0 ]).reshape(2, 1)
    if (q == 1):
        return numpy.array([ 0, 1 ]).reshape(2, 1)
    raise ValueError

def qubits_from_mask (mask):
    return functools.reduce(numpy.kron, map(qubit, mask))

def ketnorm (ket):
    return numpy.sqrt(numpy.sum(numpy.abs(ket) ** 2))

def rhonorm (rho):
    return numpy.trace(rho)

def fidelity (rho, sigma):
    from scipy.linalg import sqrtm
    sigma = sqrtm(sigma)
    return sqrtm(sigma @ rho @ sigma).trace() ** 2

