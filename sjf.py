class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0

def sjf_scheduling(processes):
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))  # Sort by arrival time, then burst time
    
    total_wt, total_tat = 0, 0
    current_time = 0
    
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        process.waiting_time = current_time - process.arrival_time
        process.turnaround_time = process.waiting_time + process.burst_time
        current_time += process.burst_time

        total_wt += process.waiting_time
        total_tat += process.turnaround_time

    avg_wt = total_wt / len(processes)
    avg_tat = total_tat / len(processes)

    return processes, avg_wt, avg_tat

# User input
num_processes = int(input("Enter number of processes: "))
processes = []

# Input arrival times first
arrival_times = []
for i in range(num_processes):
    arrival_time = int(input(f"Enter arrival time for Process P{i+1}: "))
    arrival_times.append(arrival_time)

# Input burst times after arrival times are given
for i in range(num_processes):
    burst_time = int(input(f"Enter burst time for Process P{i+1}: "))
    processes.append(Process(i+1, arrival_times[i], burst_time))

# Perform SJF Scheduling
scheduled_processes, avg_wt, avg_tat = sjf_scheduling(processes)

# Print results
print("\nProcess | Arrival Time | Burst Time | Waiting Time | Turnaround Time")
for p in scheduled_processes:
    print(f"P{p.pid}      | {p.arrival_time}           | {p.burst_time}         | {p.waiting_time}          | {p.turnaround_time}")

print(f"\nAverage Waiting Time = {avg_wt:.2f}")
print(f"Average Turnaround Time = {avg_tat:.2f}")
