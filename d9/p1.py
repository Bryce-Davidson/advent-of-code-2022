moves = [line.strip() for line in open('input.txt', 'r').readlines()]

knots = [0+0j]*2
vis = set([0+0j])

def move_head(H: complex, D: str):
    return H + {"U": +1j, "D": -1j, "L": -1, "R": +1}[D]

def move_tail(H: complex, T: complex):
    d = H - T
    if abs(d) >= 2:
        T += (d.real > 0) - (d.real < 0) + 1j * ((d.imag > 0) - (d.imag < 0))
    return T

for move in moves:
    D, q = move.split(" ")
    for i in range(int(q)):
        knots[1] = move_head(knots[1], D)
        knots[0] = move_tail(knots[1], knots[0])
        vis.add(knots[0])

print(len(vis))