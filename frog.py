n, m = input().split(' ')
n, m = int(n), int(m)

mx = []
for i in range(m):
    x = input().split(' ')
    while(len(x) > n):
        x = input().split(' ')
    mx += x

graph = {}
for i in range(1, n+1):
    current = i-1
    currentList = []
    if current < n-1:
        if mx[current] and mx[current+1] == '0':
            currentList.append(current+1)
    if mx[current] and mx[current+m+1] == '0':
        currentList.append(current+m+1)
    graph[current] = currentList


for i in range(n, len(mx)):
    current = i
    currentList = []
    if current < len(mx)-1:
        if mx[current] and mx[current+1] == '0':
            currentList.append(current+1)
    if mx[current] and mx[current-n] == '0':
        currentList.append(current-n)
        graph[current] = currentList


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


print(len(find_all_paths(graph, (n*(m-1)), (n-1))))
