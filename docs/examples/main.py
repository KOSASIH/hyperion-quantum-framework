import hyperion as hq

def main():
    # Create a new quantum circuit with 2 qubits
    circuit = hq.Circuit(2)

    # Add a Hadamard gate to the first qubit
    circuit.H(0)

    # Add a CNOT gate with the first qubit as control and the second qubit as target
    circuit.CNOT(0, 1)

    # Add a measurement to the second qubit
    circuit.measure(1)

    # Run the circuit on the IBM Q 16 Melbourne backend
    result = hq.run(circuit, backend='ibmq_16_melbourne')

    # Print the result
    print(result)

if __name__ == '__main__':
    main()
