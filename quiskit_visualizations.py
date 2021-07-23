from qiskit import *
from qiskit.visualization import plot_histogram
from qiskit.tools.monitor import job_monitor
# quantum circuit to make a Bell state
bell = QuantumCircuit(2, 2)
bell.h(0)
bell.cx(0, 1)
meas = QuantumCircuit(2, 2)
meas.measure([0,1], [0,1])
# execute the quantum circuit
backend = BasicAer.get_backend('qasm_simulator') # the device to run on
circ = bell + meas
result = execute(circ, backend, shots=1000).result()
counts  = result.get_counts(circ)
print(counts)
plot_histogram(counts)

# Execute 2-qubit Bell state again
second_result = execute(circ, backend, shots=1000).result()
second_counts  = second_result.get_counts(circ)
# Plot results with legend
legend = ['First execution', 'Second execution']
plot_histogram([counts, second_counts], legend=legend)

# Execute 2-qubit Bell state again
second_result = execute(circ, backend, shots=1000).result()
second_counts  = second_result.get_counts(circ)
# Plot results with legend
legend = ['First execution', 'Second execution']
plot_histogram([counts, second_counts], legend=legend)
plot_histogram([counts, second_counts], legend=legend, sort='desc', figsize=(15,12), \
color=['orange', 'black'], bar_labels=True)

from qiskit.visualization import plot_state_city, plot_bloch_multivector
from qiskit.visualization import plot_state_paulivec, plot_state_hinton
from qiskit.visualization import plot_state_qsphere
# execute the quantum circuit
backend = BasicAer.get_backend('statevector_simulator') # the device to run on
result = execute(bell, backend).result()
psi  = result.get_statevector(bell)
plot_state_city(psi)
plot_state_hinton(psi)
plot_state_qsphere(psi)
plot_state_paulivec(psi)
plot_bloch_multivector(psi)

plot_state_city(psi, title="My City", color=['black', 'orange'])
plot_state_hinton(psi, title="My Hinton")
plot_state_paulivec(psi, title="My Paulivec", color=['purple', 'orange', 'green'])
plot_bloch_multivector(psi, title="My Bloch Spheres")

from qiskit.visualization import plot_bloch_vector
plot_bloch_vector([0,1,0])
plot_bloch_vector([0,1,0], title='My Bloch Sphere')