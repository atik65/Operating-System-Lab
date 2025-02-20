#SJF - Shortest Job First (Non pre-emptive)
# Process: [burst_time, arrival_time, pid]

def sjf(process_list):
    time = 0
    gantt_chart_list = []
    completed ={}

    while process_list != []:
        available = []
        for p in process_list:
            if p[1] <= time:
                available.append(p)
        #No processes available -- corner case
        if available == []:
            time += 1
            gantt_chart_list.append("Idle")
            continue
        else:
            available.sort() #Sort by burst time -- because default sort will be done by first index [burst_time, arrival_time, pid]
            process = available[0]
            #Service the process
            burst_time = process[0]
            pid = process[2]
            arrival_time = process[1]
            # Add to gantt chart
            time += burst_time
            gantt_chart_list.append(pid)
            # calculate completion time, turnaround time and waiting time
            ct = time
            tt = ct - arrival_time
            wt = tt - burst_time
            # remove from process from main list
            process_list.remove(process)
            # Add to completed
            completed[pid] = [burst_time, arrival_time ,ct,tt,wt]

    return {
        "gantt_chart": gantt_chart_list,
        "completed": completed
    }


def print_table(completed):
    print("Process\tBurst Time\tArrival Time\tCompletion Time\tTurnaround Time\tWaiting Time")
    for key in completed:
        print(key, "\t", completed[key][0], "\t\t", completed[key][1], "\t\t", completed[key][2], "\t\t", completed[key][3], "\t\t", completed[key][4])

def collect_input():
    process_list = []
    n = int(input("Enter the number of processes: "))
    for i in range(n):
        burst_time = int(input(f'Enter the burst time for process {i+1}: '))
        arrival_time = int(input(f'Enter the arrival time for process {i+1}: '))
        pid = "p"+str(i+1)
        process_list.append([burst_time, arrival_time, pid])
    return process_list

if __name__ == "__main__":
    process_list= collect_input()
    res = sjf(process_list)

    print(res["gantt_chart"])
    print_table(res["completed"])