from functools import cmp_to_key

class Train:
    def __init__(self, train_name, arrival_time, departure_time):
        self.train_name = train_name
        self.arrival_time = arrival_time
        self.departure_time = departure_time
        
    def __str__(self):
        return f"{self.train_name}"


def my_comparator(a, b):
    if a.departure_time < b.departure_time:
        return -1
    elif a.departure_time > b.departure_time:
        return 1
    else:
        return 0

trains = [
    Train("t1", 8, 12),
    Train("t2", 6, 9),
    Train("t3", 11, 14),
    Train("t4", 2, 7),
    Train("t5", 1, 7),
    Train("t6", 12, 20),
    Train("t7", 7, 12),
    Train("t8", 13, 19)
    ]
trains.sort(key=cmp_to_key(my_comparator))

# for train in trains:
#     print(train, end = " ")

taken_trains = []
taken_trains.append(trains[0])
cooling_time = 1
available_time = trains[0].departure_time + cooling_time

for i in range(1, len(trains)):
    if trains[i].arrival_time >= available_time:
        taken_trains.append(trains[i])
        available_time = trains[i].departure_time + cooling_time

for train in taken_trains:
    print(train)

