import heapq

def interval_partitioning(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort by start time
    rooms = []
    
    for interval in intervals:
        if rooms and rooms[0] <= interval[0]:
            heapq.heappop(rooms)  # Free the earliest room
        heapq.heappush(rooms, interval[1])  # Assign new end time to the room
    
    return len(rooms)

intervals = [(30, 75), (0, 50), (60, 150), (5, 20)]
min_rooms = interval_partitioning(intervals)
print(f"Minimum number of rooms: {min_rooms}")
