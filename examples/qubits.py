import numpy
from braket import fidelity, rhonorm, eyemat, ket2dm, qubits_from_mask

E = eyemat(2)

Q = numpy.random.randn(4, 1) + numpy.random.randn(4, 1) * 1j
Q = ket2dm(Q) 
Q = Q / rhonorm(Q)

p = 0.25
P = (1 - p) * Q + p * E

F = fidelity(P, Q)
print(F)

