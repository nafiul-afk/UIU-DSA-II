from queue import PriorityQueue

pq = PriorityQueue()

pq.put((2, 2, "A"))
pq.put((2, 2, "C"))
pq.put((2, 2, "B"))

while not pq.empty():
    print(pq.get())

