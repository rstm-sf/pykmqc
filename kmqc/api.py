import requests


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
        circuit = list()
        count_qubits = 0
        for instruction in program:
            if count_qubits < instruction.count_qubits():
                count_qubits = instruction.count_qubits()
            circuit.append(instruction.to_circuit_json())
        return {
            "count_qubits": count_qubits,
            "circuit": circuit,
        }
