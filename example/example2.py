import kmqc

from kmqc import base
from kmqc import gates


n = 8;
q = 256;
eps = 0.2;
nreg = 1;
dim = 200;
word_a = 15;
word_b = 15;
k_list = list(range(dim))

p = kmqc.Program(base.InitDimQudit(dim))
p += kmqc.HashFun(word_a, n, k_list, kmqc.Qudit(0))
p += kmqc.ReversTest(word_a, n, k_list, kmqc.Qudit(0))
p.append_instruction(gates.Measure(0, kmqc.Qudit(0)))
conn = kmqc.connect(**kmqc.config('qvm_conn.ini', 'qvm_conn'))
r = conn.execute(p)
print(r)
