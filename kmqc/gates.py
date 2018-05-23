from six import integer_types

from kmqc.base import Gate, Qubit


def _to_qubit(qubit):
    if isinstance(qubit, integer_types):
        return Qubit(qubit)
    elif isinstance(qubit, Qubit):
        return qubit
    else:
        raise TypeError("Кубит должен быть целого типа или Qubit!")


def _make_gate(name, count_qubits):
    def gate():
        def constructor(*qubits):
            qubits = list(qubits)
            if len(qubits) != count_qubits:
                raise ValueError(
                    "Количество кубитов для {} должно равняться {}!".format(
                        name, count_qubits))
            return Gate(name, [_to_qubit(q) for q in qubits])
        return constructor
    return gate


H = _make_gate("Hadamard", 1)()
"""
H = sqrt(2) / 2 * [[1, 1],
                   [1, -1]]
"""

S = _make_gate("S", 1)()
"""
S = [[1, 0],
     [0, 1j]]
"""

T = _make_gate("T", 1)()
"""
T = [[1, 0],
     [0, exp(1j * pi / 4)]]
"""

T_H = _make_gate("THerm", 1)()
"""
T = T ^ H = [[1, 0],
             [0, exp(-1j * pi / 4)]]
"""

X = _make_gate("X", 1)()
"""
X = [[0, 1],
     [1, 0]]
"""

CNOT = _make_gate("CNOT", 2)()
"""
CNOT = [[1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0]]
"""

CCNOT = _make_gate("CCNOT", 3)()
"""
CCNOT = [[1, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 1, 0]]
"""

DEFINITE_GATES = {
    "H": H,
    "S": S,
    "T": T,
    "T_H": T_H,
    "X": X,
    "CNOT": CNOT,
    "CCNOT": CCNOT,
}
