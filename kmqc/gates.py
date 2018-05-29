from six import integer_types

from kmqc.base import Gate, Qubit


def _to_qubit(qubit):
    if isinstance(qubit, integer_types):
        return Qubit(qubit)
    elif isinstance(qubit, Qubit):
        return qubit
    else:
        raise TypeError("Кубит должен быть целого типа или Qubit!")


class Rx(Gate):
    """
    Rx(mu) = [[cos(mu / 2), -1j * sin(mu / 2)],
               [-1j * sin(mu / 2), cos(mu / 2)]]
    """
    def __init__(self, mu, qubit):
        params = {"mu": mu, }
        super().__init__("Rx", params, [_to_qubit(qubit), ])


class Rz(Gate):
    """
    Rz(mu) = [[exp(-1j * mu / 2), 0]
               [0, exp(1j * mu / 2)]]
    """
    def __init__(self, mu, qubit):
        params = {"mu": mu, }
        super().__init__("Rz", params, [_to_qubit(qubit), ])


class U1(Gate):
    """
    U1(mu) = [[1, 0],
               [0, exp(1j * mu)]]
    """
    def __init__(self, mu, qubit):
        params = {"mu": mu, }
        super().__init__("u1", params, [_to_qubit(qubit), ])


class U2(Gate):
    """
    U2(mu) = Rz(phi + pi / 2) Rx(pi / 2) Rz(mu - pi / 2)
    """
    def __init__(self, phi, mu, qubit):
        params = {"phi": phi, "mu": mu, }
        super().__init__("u2", params, [_to_qubit(qubit), ])


class U3(Gate):
    """
    U3(mu) = Rz(phi + 3 * pi) Rx(pi / 2) Rz(theta + pi) Rx(pi / 2) Rz(mu)
    """
    def __init__(self, theta, phi, mu, qubit):
        params = {"theta": theta, "phi": phi, "mu": mu, }
        super().__init__("u3", params, [_to_qubit(qubit), ])


def _make_gate(name, count_qubits):
    def gate():
        def constructor(*qubits):
            qubits = list(qubits)
            if len(qubits) != count_qubits:
                raise ValueError(
                    "Количество кубитов для {} должно равняться {}!".format(
                        name, count_qubits))
            return Gate(name, None, [_to_qubit(q) for q in qubits])
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
    "Rx": Rx,
    "Rz": Rz,
    "U1": U1,
    "U2": U2,
    "U3": U3,
    "H": H,
    "S": S,
    "T": T,
    "T_H": T_H,
    "CNOT": CNOT,
    "CCNOT": CCNOT,
}
