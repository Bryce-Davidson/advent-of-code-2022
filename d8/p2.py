from math import prod

rows = [line.strip() for line in open('input.txt', 'r').readlines()]

def vis_trees(tree: int, l: list):
    for i, other in enumerate(l):
        if tree <= other:
            return i + 1
    return len(l)

def column(rows: list, i: int):
    return [row[i] for row in rows]

def int_map(l: list):
    return [int(x) for x in l]

scenic_scores = []
for i, row in enumerate(rows):
    for j, tree in enumerate(row):
        col = column(rows, j)
        left, right = int_map(row[:j])[::-1], int_map(row[j+1:])
        top, bottom = int_map(col[:i])[::-1], int_map(col[i+1:])
        score = 1
        for d in [ left, top, right, bottom ]:
            vis = vis_trees(int(tree), d)
            score *= vis
        scenic_scores.append(score)

print(max(scenic_scores))