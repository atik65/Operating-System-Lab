# time quanta = 1

def priority_preemptive(process_list, time_quanta):
    time = 0
    gantt_chart = []
    completed = {}
    backup = {}
    first_response = {}

    # Sort processes by arrival time initially
    process_list.sort(key=lambda x: x[3])

    for process in process_list:
        pid = process[1]
        backup[pid] = {"arrival_time": process[3], "burst_time": process[2], "priority": process[0]}
        first_response[pid] = -1 

    remaining_processes = process_list[:] 

    while remaining_processes:

        available_processes = []
        for p in remaining_processes:
            if p[3] <= time:
                available_processes.append(p)

        if not available_processes:
            gantt_chart.append("Idle")
            time += 1
            continue

        # Select the highest-priority process (higher number = higher priority)
        process = max(available_processes, key=lambda x: x[0])
        
        pid = process[1]

        # Record first response time if it's the first execution
        if first_response[pid] == -1:
            first_response[pid] = time - process[3]

        execution_time = min(time_quanta, process[2])

        gantt_chart.append(pid)
        time += execution_time
        process[2] -= execution_time  

        # If process is completed
        if process[2] == 0:
            completion_time = time
            arrival_time = backup[pid]["arrival_time"]
            burst_time = backup[pid]["burst_time"]
            turnaround_time = completion_time - arrival_time
            waiting_time = turnaround_time - burst_time
            response_time = first_response[pid]  

            completed[pid] = [arrival_time, burst_time, backup[pid]["priority"], 
                              completion_time, turnaround_time, waiting_time, response_time]
            
            remaining_processes.remove(process)  

    return {"gantt_chart": gantt_chart, "completed": completed}

def print_table(completed):
    print("\nProcess\tArrival Time\tBurst Time\tPriority\tCompletion Time\tTurnaround Time\tWaiting Time\tResponse Time")
    for key, values in completed.items():
        print(f"{key}\t{values[0]}\t\t{values[1]}\t\t{values[2]}\t\t{values[3]}\t\t{values[4]}\t\t{values[5]}\t\t{values[6]}")

def collect_input():
    process_list = []
    n = int(input("Enter the number of processes: "))
    time_quanta = int(input("Enter the time quanta: "))  # Collecting time quanta

    for i in range(n):
        priority = int(input(f'Enter the priority for process {i+1} (Higher value -> Higher priority): '))
        pid = f"P{i+1}"
        arrival_time = int(input(f'Enter the arrival time for process {i+1}: '))
        burst_time = int(input(f'Enter the burst time for process {i+1}: '))
        process_list.append([priority, pid, burst_time, arrival_time])

    return process_list, time_quanta

if __name__ == "__main__":
    inputs = collect_input()
    result = priority_preemptive(inputs[0], inputs[1])

    print("\nGantt Chart:", result["gantt_chart"])
    print_table(result["completed"])