V = 6
parent = [0] * V
rank = [0] * V

def make_set(x):
    parent[x] = x
    rank[x] = 0

def find_set(x):
    if parent[x] == x:
        return x
    else:
        rep = find_set(parent[x])
        parent[x] = rep
        return rep

def union(u, v):
    rep_u = find_set(u)
    rep_v = find_set(v)
    if rep_u != rep_v:
        if rank[rep_u] > rank[rep_v]:
            parent[rep_v] = rep_u
        elif rank[rep_v] > rank[rep_u]:
            parent[rep_u] = rep_v
        else:
            parent[rep_v] = rep_u
            rank[rep_u] = rank[rep_u] + 1
        print("Connection Established")
    else:
        print("Already Connected")

for i in range(V):
    make_set(i)


union(4,5)
union(1,5)

union(1,4)

