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

import requests

from kmqc.base import InitDimQudit


class Connection(object):

    def __init__(self, endpoint, user_id, api_key):
        self.endpoint = endpoint
        self.session = self._get_session(user_id, api_key)

    def execute(self, program):
        url = self.endpoint
        payload = self._get_payload(program)
        response = self._post(url, payload)
        return response.json()

    def _post(self, url, json):
        response = self.session.post(url, json=json)
        response.raise_for_status()
        return response

    def _get_session(self, user_id, api_key):
        session = requests.Session()
        session.headers.update({
            'X-User-Id': user_id,
            'X-Api-Key': api_key,
        })
        return session

    def _get_payload(self, program):
        if isinstance(program[0], InitDimQudit):
            return self._get_payload_qudit(program)
        else:
            return self._get_payload_qubit(program)

    def _get_payload_qudit(self, program):
        circuit = list()
        qudits = set()
        dimension = program[0].dimension
        del program[0]
        for instruction in program:
            qudits |= set(instruction.get_qudit_idxs())
            circuit.append(instruction.to_circuit_json())
        return {
            'count_qudits': len(qudits),
            'dimension': dimension,
            'circuit': circuit,
        }

    def _get_payload_qubit(self, program):
        circuit = list()
        qubits = set()
        for instruction in program:
            qubits |= set(instruction.get_qudit_idxs())
            circuit.append(instruction.to_circuit_json())
        return {
            'count_qubits': len(qubits),
            'circuit': circuit,
        }
