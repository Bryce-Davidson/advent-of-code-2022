lines = open('input.txt', 'r').readlines()

TOT=70000000
UPDATE=30000000

d = {}
cur_dir = []
for line in lines:
    line = line.split()
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "..":
                cur_dir.pop()
            else:
                cur_dir.append(line[2])

    else:
        if line[0] != "dir":
            for i in range(1, len(cur_dir)+1):
                a = "/".join(cur_dir[:i])
                if a not in d:
                    d[a] = []
                n = int(line[0])
                d[a].append(n)

options = []

FREE = TOT - sum(d["/"])
REQ = UPDATE - FREE

for k, v in d.items():
    s = sum(v)
    if s >= REQ:
        options.append(s)

print(min(options))