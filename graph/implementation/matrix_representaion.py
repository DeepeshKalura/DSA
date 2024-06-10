from typing import List


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1
          

    def print_adj_matrix(self):
        for row in self.adj_matrix:
            print(" ".join(map(str, row)))

    
    def bfs(self, start:int, vi:List[bool]):

        hm = {0: 'A', 1:'B', 2:'C', 3:'D', 4: 'E', 5:'F'}
        q = [start]
        vi[start] = True

        while q:
            left = q.pop(0)
            print(hm[left], end=" ")
            for i, node in enumerate(self.adj_matrix[left]):
                if(node == 1 and not vi[i]):
                    q.append(i)
                    vi[i] = True

            

#        A
#       / \
#      B   C
#     / \ / \
#    D   E   F

# Example usage:
g = Graph(6)  # Create a graph with 6 vertices

# Add edges
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 4)
g.add_edge(4, 5)


vi = [False] * g.num_vertices
g.bfs(start=0, vi=vi)
print()
