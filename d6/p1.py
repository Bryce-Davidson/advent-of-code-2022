stream = open('input.txt', 'r').read()

for i in range(len(stream)-4):
    if len(set(stream[i:i+4])) == 4:
        print(i+4)
        break

# print([x for x in [y+4 for y in range(len(stream)-4) if len(set(stream[y:y+4])) == 4]][0])