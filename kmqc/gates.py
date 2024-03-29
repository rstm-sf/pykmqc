# Copyright (C) 2018-2019 Rustam Sayfutdinov, rstm.sf@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import math

from six import integer_types

from kmqc.base import Gate, QubitGate, Qudit


def _to_qudit(qudit):
    if isinstance(qudit, integer_types):
        return Qudit(qudit)
    elif isinstance(qudit, Qudit):
        return qudit
    else:
        raise TypeError('Кубит должен быть целого типа или Qudit!')


class ApplyX(Gate):
    """
    X_i(x, y) = [
        [I_{i - 1}, 0, 0, 0, ],
        [0, x / sqrt(|x|^2 + |y|^2), -y / sqrt(|x|^2 + |y|^2), 0, ],
        [0, y^* / sqrt(|x|^2 + |y|^2), x^* / sqrt(|x|^2 + |y|^2), 0, ],
        [0, 0, 0, I_{d - i - 1}, ]]
    """

    def __init__(self, i, x, y, qudit):
        params = {'i': i, 'x': x, 'y': y, }
        super().__init__('applyX', params, [_to_qudit(qudit), ])


class ApplyZ(Gate):
    """
    Z_d(theta) = \sum_{j=0}^{d-1}
        e^{i (1 - \left| {sgn (d - 1 - j) }\right|)} \ket{j}\bra{j}
    """

    def __init__(self, i, theta, qudit):
        params = {'i': i, 'theta': theta, }
        super().__init__('applyZ', params, [_to_qudit(qudit), ])


class ApplyXconjugate(Gate):
    """
    X_i^*(x, y) = [
        [I_{i - 1}, 0, 0, 0, ],
        [0, x / sqrt(|x|^2 + |y|^2), -y / sqrt(|x|^2 + |y|^2), 0, ],
        [0, y^* / sqrt(|x|^2 + |y|^2), x^* / sqrt(|x|^2 + |y|^2), 0, ],
        [0, 0, 0, I_{d - i - 1}, ]]^*
    """

    def __init__(self, i, x, y, qudit):
        params = {'i': i, 'x': x, 'y': y, }
        super().__init__('applyXconjugate', params, [_to_qudit(qudit), ])


class ApplyZconjugate(Gate):
    """
    {Z}_d^\dag(\theta) = {\sum_{j=0}^{d-1}
        e^{i (1 - \left| {sgn (d - 1 - j) }\right|)} \ket{j}\bra{j}}\dag
    """

    def __init__(self, i, theta, qudit):
        params = {'i': i, 'theta': theta, }
        super().__init__('applyZconjugate', params, [_to_qudit(qudit), ])


class Measure(Gate):
    """
    {Z}_d^\dag(\theta) = {\sum_{j=0}^{d-1}
        e^{i (1 - \left| {sgn (d - 1 - j) }\right|)} \ket{j}\bra{j}}\dag
    """

    def __init__(self, idx_creg, qudit):
        params = {'idx_creg': idx_creg, }
        super().__init__('measure', params, [_to_qudit(qudit), ])


class Rx(QubitGate):
    """
    Rx(mu) = [[cos(mu / 2), -1j * sin(mu / 2)],
               [-1j * sin(mu / 2), cos(mu / 2)]]
    """

    def __init__(self, mu, qubit):
        params = {'mu': mu, }
        super().__init__('Rx', params, [_to_qudit(qubit), ])


class Ry(QubitGate):
    """
    Ry(theta) = [[cos(theta / 2), -sin(theta / 2)],
                 [sin(theta / 2), cos(theta / 2)]]
    """

    def __init__(self, theta, qubit):
        params = {'theta': theta, }
        super().__init__('Ry', params, [_to_qudit(qubit), ])


class Rz(QubitGate):
    """
    Rz(phi) = [[exp(-1j * phi / 2), 0]
               [0, exp(1j * phi / 2)]]
    """

    def __init__(self, phi, qubit):
        params = {'phi': phi, }
        super().__init__('Rz', params, [_to_qudit(qubit), ])


class U1(QubitGate):
    """
    U1(mu) = [[1, 0],
               [0, exp(1j * mu)]]
    """

    def __init__(self, mu, qubit):
        params = {'mu': mu, }
        super().__init__('U1', params, [_to_qudit(qubit), ])


class U2(QubitGate):
    """
    U2(mu) = Rz(phi + pi / 2) Rx(pi / 2) Rz(mu - pi / 2)
    """

    def __init__(self, phi, mu, qubit):
        params = {'phi': phi, 'mu': mu, }
        super().__init__('U2', params, [_to_qudit(qubit), ])


class U3(QubitGate):
    """
    U3(mu) = Rz(phi + 3 * pi) Rx(pi / 2) Rz(theta + pi) Rx(pi / 2) Rz(mu)
    """

    def __init__(self, theta, phi, mu, qubit):
        params = {'theta': theta, 'phi': phi, 'mu': mu, }
        super().__init__('U3', params, [_to_qudit(qubit), ])


class Z(U1):
    """
    Z = [[1, 0],
         [0, -1]]
    """

    def __init__(self, qubit):
        super().__init__(math.pi, qubit)


class S_H(U1):
    """
    S = [[1, 0],
         [0, -1j]]
    """

    def __init__(self, qubit):
        super().__init__(-math.pi / 2.0, qubit)


class X(U3):
    """
    X = [[0, 1],
         [1, 0]]
    """

    def __init__(self, qubit):
        super().__init__(math.pi, 0.0, math.pi, qubit)


class Y(U3):
    """
    Y = [[0, 0 - 1j],
         [0 + 1j, 0]]
    """

    def __init__(self, qubit):
        super().__init__(math.pi, math.pi / 2.0, math.pi / 2.0, qubit)


def _make_qubit_gate(name, count_qubits):
    def gate():
        def constructor(*qubits):
            qubits = list(qubits)
            if len(qubits) != count_qubits:
                raise ValueError(
                    'Количество кубитов для {} должно равняться {}!'.format(
                        name, count_qubits))
            return QubitGate(name, None, [_to_qudit(q) for q in qubits])
        return constructor
    return gate


H = _make_qubit_gate('Hadamard', 1)()
"""
H = sqrt(2) / 2 * [[1, 1],
                   [1, -1]]
"""

S = _make_qubit_gate('S', 1)()
"""
S = [[1, 0],
     [0, 1j]]
"""

T = _make_qubit_gate('T', 1)()
"""
T = [[1, 0],
     [0, exp(1j * pi / 4)]]
"""

T_H = _make_qubit_gate('THerm', 1)()
"""
T = T ^ H = [[1, 0],
             [0, exp(-1j * pi / 4)]]
"""

CNOT = _make_qubit_gate('CNOT', 2)()
"""
CNOT = [[1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0]]
"""

CCNOT = _make_qubit_gate('CCNOT', 3)()
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
    'ApplyX': ApplyX,
    'ApplyZ': ApplyZ,
    'ApplyXconjugate': ApplyXconjugate,
    'ApplyZconjugate': ApplyZconjugate,
    'Measure': Measure,
    'Rx': Rx,
    'Ry': Ry,
    'Rz': Rz,
    'U1': U1,
    'U2': U2,
    'U3': U3,
    'H': H,
    'S': S,
    'S_H': S_H,
    'T': T,
    'T_H': T_H,
    'X': X,
    'Y': Y,
    'Z': Z,
    'CNOT': CNOT,
    'CCNOT': CCNOT,
}
