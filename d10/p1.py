ops = [line.strip() for line in open('input.txt', 'r').readlines()]

X, C, s = 1, 0, 0
I = [20, 60, 100, 140, 180, 220]
for i, op in enumerate(ops):
    C += 1
    if C in I:
        s += X*C
    if "add" in op:
        C += 1
        if C in I:
            s += X*C
        X += int(op.split(" ")[1])
print(s)