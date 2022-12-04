lines = open('input.txt', 'r').readlines()

total = 0
for line in lines:
    line = line.strip()
    s1, s2 = line.split(",")

    s1l, s1u = s1.split("-")
    s2l, s2u = s2.split("-")

    s1l, s1u = int(s1l), int(s1u)
    s2l, s2u = int(s2l), int(s2u)

    r1 = set(range(s1l, s1u + 1))
    r2 = set(range(s2l, s2u + 1))

    if len(r1 & r2) != 0:
        total += 1

print(total)


