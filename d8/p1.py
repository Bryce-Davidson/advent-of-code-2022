rows = [line.strip() for line in open('input.txt', 'r').readlines()]

def vis(tree: int, l: list):
    return len(l) == 0 or tree > max(l)

def column(rows: list, i: int):
    return [row[i] for row in rows]

def int_map(l: list):
    return [int(x) for x in l]

vis_trees = 0
for i, row in enumerate(rows):
    for j, tree in enumerate(row):
        col = column(rows, j)
        left, right = int_map(row[:j]), int_map(row[j+1:])
        top, bottom = int_map(col[:i]), int_map(col[i+1:])
        for d in [ left, top, right, bottom ]:
            if vis(int(tree), d):
                vis_trees += 1
                break
print(vis_trees)