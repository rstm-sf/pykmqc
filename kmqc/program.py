from kmqc.base import Instruction


class Program(object):

    def __init__(self, *instructions):
        self.instructions = list()
        self.append_instruction(instructions)

    def append_instruction(self, *instructions):
        for instruction in instructions:
            if isinstance(instruction, list):
                self.append_instruction(*instruction)
            elif isinstance(instruction, tuple):
                self.append_instruction(*instruction)
            elif isinstance(instruction, Program):
                if id(self) != id(instruction):
                    for i in instruction:
                        self.append_instruction(i)
            elif isinstance(instruction, Instruction):
                self.instructions.append(instruction)
        return self

    def __add__(self, other):
        p = Program()
        p.append_instruction(self)
        p.append_instruction(other)
        return p

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __iter__(self):
        return self.instructions.__iter__()
