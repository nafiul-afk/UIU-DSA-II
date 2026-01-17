from functools import cmp_to_key

class DSU:
    def __init__(self, V):
        self.parent = [0] * V
        self.rank = [0] * V
        
        for i in range(V):
            self.make_set(i)
    
    def make_set(self, x):
        self.parent[x] = x
    
    def find_set(self, x):
        if self.parent[x] == x:
            return x
        else:
            rep = self.find_set(self.parent[x])
            self.parent[x] = rep
            return rep
        
    def union(self, u, v):
        rep_u = self.find_set(u)
        rep_v = self.find_set(v)
        
        if rep_u != rep_v:
            if self.rank[rep_u] > self.rank[rep_v]:
                self.parent[rep_v] = rep_u
            elif self.rank[rep_v] > self.rank[rep_u]:
                self.parent[rep_u] = rep_v
            else:
                self.parent[rep_v] = rep_u
                self.rank[rep_u] = self.rank[rep_u] + 1
            return True
        else:
            return False

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w
    def __str__(self):
        return f"{self.u} <-> {self.v}, cost: {self.w}"

def edge_comparator(a, b):
    if a.w < b.w:
        return -1
    elif a.w > b.w:
        return 1
    else:
        return 0

dsu = DSU(4)

edges = [Edge(0, 1, 10),
         Edge(0, 2, 14),
         Edge(1, 2, 8),
         Edge(1, 3, 5),
         Edge(2, 3, 9)]

edges.sort(key=cmp_to_key(edge_comparator))

mst_edges = []
mst_cost = 0

for edge in edges:
    if dsu.union(edge.u, edge.v) == True:
        mst_edges.append(edge)
        mst_cost = mst_cost + edge.w

print(mst_cost)
for edges in mst_edges:
    print(edges)





