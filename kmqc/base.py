from six import integer_types, string_types


class Qubit(object):

    def __init__(self, index):
        if not isinstance(index, integer_types) and index < 0:
            raise TypeError("Инедкс должен быть целым неотрицательным числом!")
        self.index = index

    def __eq__(self, other):
        return isinstance(other, Qubit) and other.index == self.index

    def __ne__(self, other):
        return not self.__eq__(other)


class Instruction(object):
    """ Абстрактный класс. """


class Gate(Instruction):

    def __init__(self, name, qubits):
        if not isinstance(name, string_types):
            raise TypeError("Название гейта должно быть строкового типа!")
        if not isinstance(qubits, list) or not qubits:
            raise TypeError("Кубиты должны передаваться в непустом списке!")
        for q in qubits:
            if not isinstance(q, Qubit):
                raise TypeError("Кубиты должны иметь тип Qubit!")
        self.name = name
        self.qubits = qubits

    def to_circuit_json(self):
        return {
            "operator": self.name,
            "qubits": [q.index for q in self.qubits]
        }

    def count_qubits(self):
        return len(self.qubits)
