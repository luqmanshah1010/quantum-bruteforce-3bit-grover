from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

# --------------------------------------------------
# Step 1: Create a quantum circuit with 3 qubits
# and 3 classical bits for measurement
qc = QuantumCircuit(3, 3)

# --------------------------------------------------
# Step 2: Create superposition
# This places all 8 possible states into equal probability
qc.h([0, 1, 2])

# --------------------------------------------------
# Step 3: Oracle for target state |101>
# Convert |101> -> |111>, flip phase, restore
qc.x(1)
qc.ccz(0, 1, 2)
qc.x(1)

# --------------------------------------------------
# Step 4: Diffusion operator (Inversion about the mean)
qc.h([0, 1, 2])
qc.x([0, 1, 2])
qc.ccz(0, 1, 2)
qc.x([0, 1, 2])
qc.h([0, 1, 2])

# --------------------------------------------------
# Step 5: Measure all qubits
qc.measure([0, 1, 2], [0, 1, 2])

# --------------------------------------------------
# Step 6: Run on Aer simulator
backend = Aer.get_backend("aer_simulator")
qc = transpile(qc, backend)
job = backend.run(qc, shots=1024)
result = job.result()
counts = result.get_counts()

# --------------------------------------------------
# Step 7: Display results
print("Measurement Results:")
print(counts)

