class Activity:
    def __init__(self, activity_name, start, finish):
        self.activity_name = activity_name
        self.start = start
        self.finish = finish
        
    def __str__(self):
        return self.activity_name


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

#  Sort by finish time (NO cmp_to_key)
activities.sort(key=lambda x: x.finish)

taken_activities = [activities[0]]
available_time = activities[0].finish

for i in range(1, len(activities)):
    if activities[i].start >= available_time:
        taken_activities.append(activities[i])
        available_time = activities[i].finish

for activity in taken_activities:
    print(activity)
