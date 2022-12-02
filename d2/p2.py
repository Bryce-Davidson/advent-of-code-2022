"""
X means you need to lose
Y means you need to end the round in a draw
Z means you need to win

(1 for Rock, 2 for Paper, and 3 for Scissors)

A: rock
B: paper
C: scissors
"""
lines = open('input.txt', 'r').readlines()

move = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

scores = {
    "A": {
        "X": 0 + move["Z"],
        "Y": 3 + move["X"],
        "Z": 6 + move["Y"],
    },
    "B": {
        "X": 0 + move["X"],
        "Y": 3 + move["Y"],
        "Z": 6 + move["Z"],
    },
    "C": {
        "X": 0 + move["Y"],
        "Y": 3 + move["Z"],
        "Z": 6 + move["X"],
    },
}

results = []

for line in lines:
    opp_move, player_move = line.strip().split(" ")
    result = scores[opp_move][player_move]
    results.append(result)

print(sum(results))