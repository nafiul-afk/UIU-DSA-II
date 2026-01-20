import math

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

def bellmanFord(edges, V, source):
    distance = [math.inf] * V
    parent = [-1] * V
    
    distance[source] = 0
    parent[source] = source
    
    for i in range(1, V, 1):
        update = False
        for i in range(len(edges)):
            if distance[edges[i].v] > distance[edges[i].u] + edges[i].w:
                distance[edges[i].v] = distance[edges[i].u] + edges[i].w
                parent[edges[i].v] = edges[i].u
                update = True
        if update == False:
            break
    
    
    for i in range(len(edges)):
        if distance[edges[i].v] > distance[edges[i].u] + edges[i].w:
            print("Negative Cycle Exist")
            return
    
    print(distance)
    print(parent)
    
        
    
                


edges = [Edge(0, 1, 5), Edge(1, 2, 4), Edge(2, 0, -10)]

V = 3

source = 0

bellmanFord(edges, V, source)