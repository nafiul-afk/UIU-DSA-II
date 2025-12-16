from functools import cmp_to_key

class Activity:
    def __init__(self, activity_name, start, finish):
        self.activity_name = activity_name
        self.start = start
        self.finish = finish
        
    def __str__(self):
        return f"{self.activity_name}"


def my_comparator(a, b):
    if a.finish < b.finish:
        return -1
    elif a.finish > b.finish:
        return 1
    else:
        return 0

activities = [
    Activity("a1", 1, 3),
    Activity("a2", 0, 4),
    Activity("a3", 1, 2),
    Activity("a4", 4, 6),
    Activity("a5", 2, 9),
    Activity("a6", 5, 8),
    Activity("a7", 3, 5),
    Activity("a8", 4, 8)
    ]
activities.sort(key=cmp_to_key(my_comparator))

# for activity in activities:
#     print(activity, end = " ")

taken_activities = []
taken_activities.append(activities[0])
available_time = activities[0].finish

for i in range(1, len(activities)):
    if activities[i].start >= available_time:
        taken_activities.append(activities[i])
        available_time = activities[i].finish

for activity in taken_activities:
    print(activity)
