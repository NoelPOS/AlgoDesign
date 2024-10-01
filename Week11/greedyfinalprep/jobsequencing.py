class Job:
    def __init__(self, job_id, profit, deadline):
        self.job_id = job_id
        self.profit = profit
        self.deadline = deadline

def job_scheduling(jobs):
    jobs.sort(key=lambda x: x.profit, reverse=True)
    max_deadline = max(job.deadline for job in jobs)
    result = [-1] * max_deadline
    total_profit = 0

    for job in jobs:
        for j in range(min(job.deadline, max_deadline) - 1, -1, -1):
            if result[j] == -1:
                result[j] = job.job_id
                total_profit += job.profit
                break

    return result, total_profit

jobs = [Job(1, 100, 2), Job(2, 19, 1), Job(3, 27, 2), Job(4, 25, 1), Job(5, 15, 3)]
schedule, profit = job_scheduling(jobs)
print(f"Scheduled jobs: {schedule}, Total profit: {profit}")
