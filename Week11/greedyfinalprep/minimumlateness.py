class Task:
    def __init__(self, task_id, time, deadline):
        self.task_id = task_id
        self.time = time
        self.deadline = deadline

def minimize_max_lateness(tasks):
    # Step 1: Sort tasks by their deadlines
    tasks.sort(key=lambda x: x.deadline)
    
    current_time = 0
    max_lateness = 0
    schedule = []
    
    # Step 2: Process tasks in the order of deadlines
    for task in tasks:
        current_time += task.time  # Update current time after finishing this task
        lateness = max(0, current_time - task.deadline)  # Calculate lateness
        max_lateness = max(max_lateness, lateness)  # Update the maximum lateness
        schedule.append(task.task_id)  # Add task to the schedule
    
    return schedule, max_lateness

# Example tasks (task_id, processing time, deadline)
tasks = [Task(1, 4, 7), Task(2, 2, 4), Task(3, 3, 5), Task(4, 1, 3)]

# Step 3: Minimize maximum lateness
schedule, max_lateness = minimize_max_lateness(tasks)

print(f"Optimal Schedule: {schedule}")
print(f"Maximum Lateness: {max_lateness}")
