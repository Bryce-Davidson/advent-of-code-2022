"""
The score for a single round is the score for the shape you selected

(1 for Rock, 2 for Paper, and 3 for Scissors)

plus the score for the outcome of the round

(0 if you lost, 3 if the round was a draw, and 6 if you won).
"""
lines = open('input.txt', 'r').readlines()


scores = [
    [3,6,0],
    [0,3,6],
    [6,0,3]
]

opp = {
    "A": 0,
    "B": 1,
    "C": 2
}

points = player = {
    "X": 0,
    "Y": 1,
    "Z": 2
}

results = []

for line in lines:
    opp_move, player_move = line.strip().split(" ")

    opp_index = opp[opp_move]
    player_index = player[player_move]

    result = scores[opp_index][player_index] + points[player_move] + 1
    results.append(result)

print(sum(results))