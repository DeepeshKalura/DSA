from collections import defaultdict

edges = [[1,2],[1,3], [1,4], [1,11], [2, 9], [2,10], [3, 8], [4, 5], [4, 6], [4,7]]

graph = defaultdict(list)

for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)


iv = [False] * 12

def bfs(start):
    iv[start] = True

    queue = [start]

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbor in graph[node]:
            if not iv[neighbor]:
                iv[neighbor] = True
                queue.append(neighbor)
    

bfs(1)
print()      

