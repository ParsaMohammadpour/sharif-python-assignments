edges = {}
n, m = [int(i) for i in input().split()]
answers = [input() for i in range(n)]
for i in range(m):
    first, second = input().split()
    if first not in edges.keys():
        edges[first] = []
    edges[first].append(second)

for i in answers:
    if i not in edges.keys():
        print(0)
        continue
    print(len(edges[i]))
    for j in edges[i]:
        print(j)