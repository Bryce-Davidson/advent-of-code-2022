ops = [line.strip() for line in open('input.txt', 'r').readlines()]

X, C = 1, 0
screen = [["." for i in range(40)] for j in range(6)]

def draw(C: int, X: int):
    row, col = C // 40, C % 40
    if col in range(X-1, X+2):
        screen[row][col] = "#"

for i, op in enumerate(ops):
    draw(C, X)
    C += 1
    if "add" in op:
        draw(C, X)
        C += 1
        X += int(op.split(" ")[1])

for row in screen:
    print(" ".join(row))