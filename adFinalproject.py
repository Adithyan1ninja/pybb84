pip install qiskit
pip install qiskit[visualization]

from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from numpy.random import randint
import numpy as np
from qiskit.providers.aer import QasmSimulator

num_qubits = 32

alice_basis = np.random.randint(2, size=num_qubits)
alice_state = np.random.randint(2, size=num_qubits)
bob_basis = np.random.randint(2, size=num_qubits)


print(f"Alice's State:\t {np.array2string(alice_state)}")
print(f"Alice's Bases:\t {np.array2string(alice_basis)}")
print(f"Bob's Bases:\t {np.array2string(bob_basis)}")

def bb84_circuit(state, basis, measurement_basis):
   
   
    
    num_qubits = len(state)
    
    bb84_circuit = QuantumCircuit(num_qubits)

    
    for i in range(len(basis)):
        if state[i] == 1:
            bb84_circuit.x(i)
        if basis[i] == 1:
            bb84_circuit.h(i)
   

    
    for i in range(len(measurement_basis)):
        if measurement_basis[i] == 1:
            bb84_circuit.h(i)

    
    bb84_circuit.measure_all()
    
    return bb84_circuit
    
    circuit = bb84_circuit(alice_state, alice_basis, bob_basis)
key = execute(circuit.reverse_bits(),backend=QasmSimulator(),shots=1).result().get_counts().most_frequent()
encryption_key = ''
for i in range(num_qubits):
    if alice_basis[i] == bob_basis[i]:
         encryption_key += str(key[i])
print(f"Key: {encryption_key}")


