\# Quantum Brute-Force Search (3-Bit) using Grover’s Algorithm



This project demonstrates how a quantum computer can perform a brute-force

search on a 3-bit search space using \*\*Grover’s Algorithm\*\*, implemented in

\*\*Qiskit\*\*.



The goal is to find a hidden 3-bit value (e.g., `101`) faster than classical

brute-force search by exploiting \*\*quantum superposition and amplitude

amplification\*\*.



---



\## Problem Statement



A classical computer must check all possible 3-bit values:



000, 001, 010, 011, 100, 101, 110, 111



In the worst case, this requires \*\*8 iterations\*\*.



Grover’s algorithm allows a quantum computer to find the correct value in

approximately \*\*√8 ≈ 2 iterations\*\*.



---



\## Key Concepts Used



\- Qubits and Superposition

\- Quantum Oracle (Phase Flip)

\- Diffusion Operator (Inversion About the Mean)

\- Measurement and Probability

\- Quadratic Speedup



---



\## Tools \& Technologies



\- Python 3.11

\- Qiskit

\- Qiskit Aer Simulator

\- Grover’s Algorithm



---



\## How to Run



\### 1. Install Python 3.11

Ensure Python 3.11 is installed and added to PATH.



\### 2. Install dependencies



pip install -r requirements.txt



\### 3. Run the program

python grover\_3bit.py





\## Expected Output



The correct state (101) appears with the highest probability:



{'101': ~780, others: ~30–40}



\## Disclaimer



This project is a conceptual demonstration of quantum brute-force

acceleration. It does not break real cryptographic systems.



\## References



1. Grover, L. K. (1996). A fast quantum mechanical algorithm for database search.



2\. IBM Qiskit Documentation

