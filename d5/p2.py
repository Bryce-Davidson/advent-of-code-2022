lines = open('input.txt', 'r').readlines()

matrix = [
    ["N", "S", "D", "C", "V", "Q", "T"],
    ["M", "F", "V"],
    ["F", "Q", "W", "D", "P", "N", "H", "M"],
    ["D", "Q", "R", "T", "F"],
    ["R", "F", "M", "N", "Q", "H", "V", "B"],
    ["C", "F", "G", "N", "P", "W", "Q"],
    ["W", "F", "R", "L", "C", "T"],
    ["T", "Z", "N", "S"],
    ["M", "S", "D", "J", "R", "Q", "H", "N"]
]

moves = lines[10:]

def parse_move(move):
    toks = move.strip().split(" ")
    return toks[1], toks[3], toks[5]

def move_crates(num, i_from, i_to):
    if num == 0:
        return
    temp = []
    for i in range(num):
        if len(matrix[i_from - 1]) != 0:
            temp.append(matrix[i_from - 1].pop())
    temp.reverse()
    for i in temp:
        matrix[i_to - 1].append(i)

for move in moves:
    move = parse_move(move)
    move_crates(int(move[0]), int(move[1]), int(move[2]))

s = ""
for i, e in enumerate(matrix):
    s += matrix[i][-1]
print(s)
