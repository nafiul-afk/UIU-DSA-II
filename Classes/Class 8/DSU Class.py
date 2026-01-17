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

dsu = DSU(6)

dsu.union(4, 5)
dsu.union(3, 5)

dsu.union(1,2)
dsu.union(2, 5)

print(dsu.parent)
print(dsu.rank)


