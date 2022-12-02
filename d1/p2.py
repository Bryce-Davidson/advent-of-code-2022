with open('input.txt', 'r') as f:
    lines = f.readlines()

current_group = []
groups = []
# Seperate the groups into sublists
for line in lines:
    if line == '\n':
        groups.append(sum(current_group))
        current_group = []
    else:
        current_group.append(int(line.strip()))

sort_group = sorted(groups, reverse=True)
print(sum(sort_group[:3]))