lines = open('input.txt', 'r').readlines()

cur_dir = []
o = [\
    cur_dir.pop() if d == ".." else cur_dir.append(d) for d in \
        [line[2] if line[0] != "dir" else line[0] for line in \
        [line.split() for line in lines] if line[1] == "cd"] \
    ]

# d = {}
# cur_dir = []
# for line in lines:
#     line = line.split()
#     if line[0] == "$":
#         if line[1] == "cd":
#             if line[2] == "..":
#                 cur_dir.pop()
#             else:
#                 cur_dir.append(line[2])

#     else:
#         if line[0] != "dir":
#             for i in range(1, len(cur_dir)+1):
#                 a = "/".join(cur_dir[:i])
#                 if a not in d:
#                     d[a] = []
#                 n = int(line[0])
#                 d[a].append(n)
