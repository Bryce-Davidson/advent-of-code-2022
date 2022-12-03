chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

lines = open('input.txt', 'r').readlines()

total = []
for i in range(len(lines)-2)[::3]:
    one, two, three = lines[i].strip(), lines[i+1].strip(), lines[i+2].strip()
    char = list((set(one) & set(two) & set(three)))[0]
    score = chars.index(char) + 1
    total.append(score)
print(sum(total))