import kmqc

from kmqc import gates, Program


p = Program(
    gates.X(1),
    gates.H(0),
    gates.H(1),
    gates.CNOT(0, 1),
    gates.H(0)
)
conn = kmqc.connect(**kmqc.config('qvm_conn.ini', 'qvm_conn'))
r = conn.execute(p)
print(r)

