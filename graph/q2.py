import collections

n = 7

edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]

graph = collections.defaultdict(list)


tnop:int = n * (n-1) // 2 # total_number_of_pairs


for x, y in edges:
    
    graph[x].append(y)
    graph[y].append(x)


def dfs(start:int):
    pairs:int = 0
    a.append(start)
    try :
        t = graph[start]
    except:
        t = []
    for i in range(len(t)):
        if t[i] not in a:
            dfs(t[i])
    
    for i in a:
        if(i>start):
            pairs+=1
    return pairs
 
tp:int = 0
for i in range(n):
    a = []
    pairs:int = 0
    pairs = dfs(i)
    print(pairs)
    tp+=pairs


print(tnop - tp)

