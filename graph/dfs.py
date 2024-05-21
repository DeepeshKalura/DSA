graph = {
 1 : [2, 3, 4],
 2 : [1, 5],
 3 : [1],
 4 : [1],
 5 : [2],
}


visited = [False] * len(graph)
trueArray = [True] * len(graph)

def dfs(graph, start:int):
    if(visited == trueArray):
        return 
    print(start, end=" ")
    visited[start-1] = True
    for i in graph[start]:
        if(visited[i-1] == False):
            dfs(graph=graph, start=i)
    

dfs(graph=graph, start=1)

# 1 2 5 3 4