from z3 import *
import re

file = open("input/2025/10.txt").read().strip()

p2 = 0
for line in file.splitlines():
    _, *rest, jolts = line.split()

    jolts = list(map(int, jolts[1:-1].split(",")))
    s = Optimize();

    vecs = []
    for positions in rest:
        vec = [ 0 if str(n) not in positions else 1 for n in range(len(jolts)) ]
        vecs.append(vec)

    variables = [Int(var) for var in "abcdefghijklmnopqrstuvwxyz"[0:len(vecs)]]

    for var in variables:
        s.add(var >= 0)

    foo = []
    for vec, var in zip(vecs, variables):
        foo.append([ var * v for v in vec ])

    for lis, jolt in zip(zip(*foo), jolts):
        # print(lis, jolt)
        s.add(Sum(lis) == jolt)

    total = Sum(variables)
    h = s.minimize(total)

    if s.check() == sat:
        m = s.model()
        p2 += sum([m[d].as_long() for d in m.decls()])
    else:
        assert(false)

# 21114 TOO HIGH
print(p2)