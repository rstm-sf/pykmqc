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

from kmqc.base import Qudit
from kmqc.gates import ApplyX, ApplyZ, ApplyXconjugate, ApplyZconjugate
from kmqc.program import Program


class ApplyF0(Program):

    def __init__(self, dim, qudit):
        self._set_instr(dim, qudit)

    def _set_instr(self, dim, qudit):
        self.instructions = list()
        for i in range(dim):
            b = math.sqrt((dim - i) / dim)
            self.append_instruction(
                ApplyX(i, math.sqrt(1.0 / dim), b, qudit))


class ApplyF0conjugate(Program):

    def __init__(self, dim, qudit):
        self._set_instr(dim, qudit)

    def _set_instr(self, dim, qudit):
        self.instructions = list()
        for i in reversed(range(dim)):
            b = math.sqrt((dim - i) / dim)
            self.append_instruction(
                ApplyXconjugate(i, math.sqrt(1.0 / dim), b, qudit))


class ApplyZ_all(Program):

    def __init__(self, word, k_list, qudit):
        self._set_instr(word, k_list, qudit)

    def _set_instr(self, word, k_list, qudit):
        self.instructions = list()
        for i in range(len(k_list)):
            self.append_instruction(
                ApplyZ(i, (word * k_list[i]) / n, qudit))
        return instr


class ApplyZconjugate_all(Program):

    def __init__(self, word, k_list, qudit):
        self._set_instr(word, k_list, qudit)

    def _set_instr(self, word, k_list, qudit):
        self.instructions = list()
        for i in reversed(range(len(k_list))):
            self.append_instruction(
                ApplyZconjugate(i, (word * k_list[i]) / n, qudit))
        return instr


class HashFun(Program):

    def __init__(self, word, k_list, qudit):
        algo = self._get_algo(word, k_list, qudit)
        self.instructions = algo.instructions

    def _get_algo(self, word, k_list, qudit):
        algo = ApplyF0(len(k_list), qudit)
        algo += ApplyZ_all(word, k_list, qudit)
        return algo


class ReversTest(Program):

    def __init__(self, arg):
        algo = self._get_algo(word, k_list, qudit)
        self.instructions = algo.instructions

    def _get_algo(self, word, k_list, qudit):
        algo = ApplyF0conjugate(len(k_list), qudit)
        algo += ApplyZconjugate_all(word, k_list, qudit)
        return algo
