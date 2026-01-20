from queue import PriorityQueue
import math

def print_path(parent, destination):
    if parent[destination] == destination:
        print(destination, end = " ")
    else:
        print_path(parent, parent[destination])
        print(destination, end = " ")

def dijkstra(graph, source, V):
    distance = [math.inf]*V
    parent = [-1] * V
    found_optimal = [0] * V
    
    pq = PriorityQueue()
    
    distance[source] = 0
    pq.put((distance[source], source))
    parent[source] = source
    
    while not pq.empty():
        current_node = pq.get()[1]
        if found_optimal[current_node] == 1:
            continue
        found_optimal[current_node] = 1
        
        for neighbor, cost in graph[current_node]:
            if found_optimal[neighbor] != 1:
                if distance[neighbor] > distance[current_node] + cost:
                    distance[neighbor] = distance[current_node] + cost
                    pq.put((distance[neighbor], neighbor))
                    parent[neighbor] = current_node
    
    for i in range(V):
        print_path(parent, i)
        print()
    
                
        
        
    

graph = {
    0 : [(1, 5), (2, 4)],
    1 : [(2, 2), (3, 10)],
    2 : [(3, 7)],
    3 : []
    }

V = 4

source = 0

dijkstra(graph, source, V)







