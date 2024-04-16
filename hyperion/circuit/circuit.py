import copy
import itertools
import numpy as np

class Circuit:
    """
    Circuit class for representing a quantum circuit.

    Attributes:
        qubits (list): The list of qubits in the circuit.
        gates (list): The list of gates in the circuit.
        measurements (list): The list of measurements in the circuit.
        num_qubits (int): The number of qubits in the circuit.
        depth (int): The depth of the circuit.
    """

    def __init__(self, num_qubits=1):
"""
        Initialize the Circuit object.

        Args:
            num_qubits (int): The number of qubits in the circuit.
        """
        self.qubits = [Qubit() for _ in range(num_qubits)]
        self.gates = []
        self.measurements = []
        self.num_qubits = num_qubits
        self.depth = 0

    def H(self, qubit):
        """
        Add a Hadamard gate to the given qubit.

        Args:
            qubit (Qubit): The qubit to add the gate to.
        """
        gate = Gate('H', [qubit])
        self.gates.append(gate)
        self.depth = max(self.depth, gate.depth)

    def X(self, qubit):
        """
        Add an X gate to the given qubit.

        Args:
            qubit (Qubit): The qubit to add the gate to.
        """
        gate = Gate('X', [qubit])
        self.gates.append(gate)
        self.depth = max(self.depth, gate.depth)

    def Y(self, qubit):
        """
        Add a Y gate to the given qubit.

        Args:
            qubit (Qubit): The qubit to add the gate to.
        """
        gate = Gate('Y', [qubit])
        self.gates.append(gate)
        self.depth = max(self.depth, gate.depth)

    def Z(self, qubit):
        """
        Add a Z gate to the given qubit.

        Args:
            qubit (Qubit): The qubit to add the gate to.
        """
        gate = Gate('Z', [qubit])
        self.gates.append(gate)
        self.depth = max(self.depth, gate.depth)

    def CNOT(self, control, target):
        """
        Add a CNOT gate with the given control and target qubits.

        Args:
            control (Qubit): The control qubit.
            target (Qubit): The target qubit.
        """
        gate = Gate('CNOT', [control, target])
        self.gates.append(gate)
        self.depth = max(self.depth, gate.depth)

    def measure(self, qubit):
        """
        Add a measurement to the given qubit.

        Args:
            qubit (Qubit): The qubit to add the measurement to.
        """
        measurement = Measurement(qubit)
        self.measurements.append(measurement)

    def to_matrix(self):
        """
        Return the matrix representation of the circuit.

        Returns:
            np.ndarray: The matrix representation of the circuit.
        """
        num_qubits = self.num_qubits
        identity = np.identity(2, dtype=np.complex128)
        matrix = np.kron(identity, identity)

        for gate in self.gates:
            matrix = np.dot(gate.to_matrix(), matrix)

        for measurement in self.measurements:
            qubit = measurement.qubit
            index = qubit.index
            matrix = np.delete(matrix, index, axis=0)
            matrix = np.delete(matrix, index, axis=1)

        return matrix

    def copy(self):
        """
        Return a copy of the circuit.

        Returns:
            Circuit: A copy of the circuit.
        """
        circuit = Circuit(self.num_qubits)
        circuit.gates = copy.deepcopy(self.gates)
        circuit.measurements = copy.deepcopy(self.measurements)
        circuit.num_qubits = self.num_qubits
        circuit.depth = self.depth

        for i, qubit in enumerate(self.qubits):
            circuit.qubits[i] = copy.deepcopy(qubit)

        return circuit
