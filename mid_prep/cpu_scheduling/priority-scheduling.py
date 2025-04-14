# priority_preemptive

def priority_scheduling(process_list, time_quanta):
    time = 0
    gannt = []
    completed = {}
    backup = {}
    first_response = {}

    # sort based on arrival time
    # process_list.sort()

    for process in process_list:
        pid = process[2]
        first_response[pid] = -1
        backup[pid] = [process[0], process[1], process[2], process[3]]


    remaining_process = process_list[:]

    while remaining_process:
        available = []

        for process in remaining_process[:]:
            if process[0] <= time:
                available.append(process)
        
        # handle corner case 
        if not available:
            gannt.append("Idle")
            time +=1
            continue
        
        process = max(available, key = lambda p : p[3])
        pid = process[2]
        
        if first_response[pid] == -1:
            first_response[pid] = time - process[0]
        
        execution_time = min(time_quanta, process[1])
        time += execution_time
        gannt.append(pid)
        process[1] -= execution_time

        if process[1] == 0:
            arrival_time = backup[pid][0]
            burst_time = backup[pid][1]
            priority = backup[pid][3]

            ct = time
            tat = ct - arrival_time
            wt = tat - burst_time
            rt = first_response[pid]

            remaining_process.remove(process)
            
            completed[pid] = [pid, arrival_time, burst_time,  priority, ct,  wt, tat, rt]
    
    return {
        'gannt': gannt,
        'completed': completed
    }


        
        
def priority_scheduling_v1(process_list, time_quanta):
    # process = [arrival,burst,pid,priority]

    time = 0
    gannt = []
    completed = {}
    backup = {}
    first_response = {}

    for process in process_list:
        
        pid = process[2]
        first_response[pid] = -1
        backup[pid] = [process[0], process[1], process[3]]
    
    remaining_process = process_list[:]

    while remaining_process:
        available = []

        for process in remaining_process[:]:
            if process[0] <= time:
                available.append(process)
        
        # handle corner case 
        if not available:
            gannt.append("Idle")
            time += 1
            continue
        
        process = max(available, key = lambda p : p[3])
        pid = process[2]

        # track the first response time
        if first_response[pid] == -1:
            first_response[pid] = time - process[0]
        
        execution_time = min(time_quanta, process[1])
        time += execution_time
        process[1] -= execution_time
        gannt.append(pid)

        if process[1] == 0:
            arrival_time = backup[pid][0]
            burst_time = backup[pid][1]
            priority = backup[pid][2]
            ct = time
            tat = ct - arrival_time
            wt = tat - burst_time
            rt = first_response[pid]
            remaining_process.remove(process)

            completed[pid] = [pid, arrival_time, burst_time, priority, ct, wt, tat, rt]
    
    return {
        'gannt': gannt,
        'completed': completed
    }


def print_table(completed):
    print("Process\tArrival\tBrust\tPriority\tCT\tWT\tTAT\tRT")

    for key in completed:
        print(f'{completed[key][0]} \t {completed[key][1]} \t {completed[key][2]} \t {completed[key][3]} \t\t {completed[key][4]} \t {completed[key][5]} \t {completed[key][6]} \t{completed[key][7]}')


if __name__ == "__main__":
    # process = [arrival,burst,pid,priority]
    process_list = [
            [0,5,'p1',10],
            [1,4,'p2',20],
            [2,2,'p3',30],
            [4,1,'p4',40],
        ]
        
    time_quanta = 1
        
    res = priority_scheduling_v1(process_list, time_quanta)

    print(res['gannt'])
    print_table(res['completed'])