# Useful additional packages
import matplotlib.pyplot as plt
import numpy as np
from math import pi
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute
from qiskit.tools.visualization import circuit_drawer
from qiskit.quantum_info import state_fidelity
from qiskit import BasicAer
backend = BasicAer.get_backend('unitary_simulator')

q = QuantumRegister(1)
qc = QuantumCircuit(q)
qc.u3(pi/2,pi/2,pi/2,q)
qc.draw()
job = execute(qc, backend)
job.result().get_unitary(qc, decimals=3)

qc = QuantumCircuit(q)
qc.u2(pi/2,pi/2,q)
qc.draw()
job = execute(qc, backend)
job.result().get_unitary(qc, decimals=3)

qc = QuantumCircuit(q)
qc.u1(pi/2,q)
qc.draw()
job = execute(qc, backend)
job.result().get_unitary(qc, decimals=3)

qc = QuantumCircuit(q)
qc.id(q)
qc.draw()
job = execute(qc, backend)
job.result().get_unitary(qc, decimals=3)

qc = QuantumCircuit(q)
qc.x(q)
qc.draw()
job = execute(qc, backend)
job.result().get_unitary(qc, decimals=3)

qc = QuantumCircuit(q)
qc.y(q)
qc.draw()
job = execute(qc, backend)
job.result().get_unitary(qc, decimals=3)

qc = QuantumCircuit(q)
qc.z(q)
qc.draw()
job = execute(qc, backend)
job.result().get_unitary(qc, decimals=3)

qc = QuantumCircuit(q)
qc.h(q)
qc.draw()
job = execute(qc, backend)
job.result().get_unitary(qc, decimals=3)

qc = QuantumCircuit(q)
qc.s(q)
qc.draw()
job = execute(qc, backend)
job.result().get_unitary(qc, decimals=3)

qc = QuantumCircuit(q)
qc.sdg(q)
qc.draw()
job = execute(qc, backend)
job.result().get_unitary(qc, decimals=3)

qc = QuantumCircuit(q)
qc.t(q)
qc.draw()
job = execute(qc, backend)
job.result().get_unitary(qc, decimals=3)

qc = QuantumCircuit(q)
qc.tdg(q)
qc.draw()
job = execute(qc, backend)
job.result().get_unitary(qc, decimals=3)

qc = QuantumCircuit(q)
qc.rx(pi/2,q)
qc.draw()
job = execute(qc, backend)
job.result().get_unitary(qc, decimals=3)

qc = QuantumCircuit(q)
qc.ry(pi/2,q)
qc.draw()
job = execute(qc, backend)
job.result().get_unitary(qc, decimals=3)

qc = QuantumCircuit(q)
qc.rz(pi/2,q)
qc.draw()
job = execute(qc, backend)
job.result().get_unitary(qc, decimals=3)

q = QuantumRegister(2)
qc = QuantumCircuit(q)
qc.cx(q[0],q[1])
qc.draw()
job = execute(qc, backend)
job.result().get_unitary(qc, decimals=3)

qc = QuantumCircuit(q)
qc.cy(q[0],q[1])
qc.draw()
job = execute(qc, backend)
job.result().get_unitary(qc, decimals=3)

qc = QuantumCircuit(q)
qc.cz(q[0],q[1])
qc.draw()
job = execute(qc, backend)
job.result().get_unitary(qc, decimals=3)

qc = QuantumCircuit(q)
qc.ch(q[0],q[1])
qc.draw()
job = execute(qc, backend)
job.result().get_unitary(qc, decimals=3)

qc = QuantumCircuit(q)
qc.crz(pi/2,q[0],q[1])
qc.draw()
job = execute(qc, backend)
job.result().get_unitary(qc, decimals=3)

qc = QuantumCircuit(q)
qc.cu1(pi/2,q[0], q[1])
qc.draw()
job = execute(qc, backend)
job.result().get_unitary(qc, decimals=3)

qc = QuantumCircuit(q)
qc.cu3(pi/2, pi/2, pi/2, q[0], q[1])
qc.draw()
job = execute(qc, backend)
job.result().get_unitary(qc, decimals=3)

qc = QuantumCircuit(q)
qc.swap(q[0], q[1])
qc.draw()
job = execute(qc, backend)
job.result().get_unitary(qc, decimals=3)

q = QuantumRegister(3)
qc = QuantumCircuit(q)
qc.ccx(q[0], q[1], q[2])
qc.draw()
job = execute(qc, backend)
job.result().get_unitary(qc, decimals=3)

qc = QuantumCircuit(q)
qc.cswap(q[0], q[1], q[2])
qc.draw()
job = execute(qc, backend)
job.result().get_unitary(qc, decimals=3)


q = QuantumRegister(1)
c = ClassicalRegister(1)
qc = QuantumCircuit(q, c)
qc.measure(q, c)
qc.draw()
backend = BasicAer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=1024)
job.result().get_counts(qc)

qc = QuantumCircuit(q, c)
qc.h(q)
qc.measure(q, c)
qc.draw()
job = execute(qc, backend, shots=1024)
job.result().get_counts(qc)

qc = QuantumCircuit(q, c)
qc.reset(q[0])
qc.measure(q, c)
qc.draw()
job = execute(qc, backend, shots=1024)
job.result().get_counts(qc)

qc = QuantumCircuit(q, c)
qc.h(q)
qc.reset(q[0])
qc.measure(q, c)
qc.draw()
job = execute(qc, backend, shots=1024)
job.result().get_counts(qc)

qc = QuantumCircuit(q, c)
qc.x(q[0]).c_if(c, 0)
qc.measure(q,c)
qc.draw()
job = execute(qc, backend, shots=1024)
job.result().get_counts(qc)

qc = QuantumCircuit(q, c)
qc.h(q)
qc.measure(q,c)
qc.x(q[0]).c_if(c, 0)
qc.measure(q,c)
qc.draw()
job = execute(qc, backend, shots=1024)
job.result().get_counts(qc)

# Initializing a three-qubit quantum state
import math
desired_vector = [
    1 / math.sqrt(16) * complex(0, 1),
    1 / math.sqrt(8) * complex(1, 0),
    1 / math.sqrt(16) * complex(1, 1),
    0,
    0,
    1 / math.sqrt(8) * complex(1, 2),
    1 / math.sqrt(16) * complex(1, 0),
    0]
q = QuantumRegister(3)
qc = QuantumCircuit(q)
qc.initialize(desired_vector, [q[0],q[1],q[2]])
qc.draw()
backend = BasicAer.get_backend('statevector_simulator')
job = execute(qc, backend)
qc_state = job.result().get_statevector(qc)
state_fidelity(desired_vector,qc_state)