stream = open('input.txt', 'r').read()

for i in range(len(stream)-14):
    if len(set(stream[i:i+14])) == 14:
        print(i+14)
        break