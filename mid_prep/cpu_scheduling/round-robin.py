from collections import deque

def round_robin(process_list, time_quanta):
    time = 0
    gannt = []
    completed = {}
    queue = deque()
    first_response = {}
    backup = {}

    # sort process list based on arrival time
    process_list.sort()

    # backup and pre process first response dict
    for process in process_list:
        pid = process[2]
        brust_time = process[1]
        arrival_time = process[0]

        first_response[pid] = -1
        backup[pid] = [arrival_time,brust_time]
    
    remaining_process = process_list[:]

    while remaining_process or queue:
        # append the current arrived process to queue
        for process in remaining_process[:]:
            if process[0] <= time:
                queue.append(process)
                # remove the process from remaining list
                remaining_process.remove(process)
        
        # handle corner case -- if no item in queue
        if not queue:
            time += 1
            gannt.append('Idle')
            continue
        
        # handle process
        process = queue.popleft()
        pid = process[2]
        arrival_time = process[0]

        # handle first response time
        if first_response[pid] == -1:
            first_response[pid] = time - process[0]
        
        execution_time = min(time_quanta,process[1])
        process[1] -= execution_time
        time += execution_time
        gannt.append(pid)

        # check if any other process arrived by this time
        for p in remaining_process[:]:
            if p[0] <= time:
                queue.append(p)
                remaining_process.remove(p)
        
        if process[1] == 0:
            brust_time = backup[pid][1]
            # CT
            ct = time
            # TAT
            tat = ct - arrival_time
            # WT
            wt = tat - brust_time
            # RT
            rt = first_response[pid]

            completed[pid] = [pid,arrival_time, brust_time, ct,wt,  tat, rt]
        else:
            queue.append(process)
    
    return {
        'gannt': gannt,
        'completed': completed
    }
        



def round_robin_v1(process_list, time_quanta):
    time = 0
    gannt = []
    completed = {}
    first_response = {}
    backup = {}
    queue = deque()

    # process_list.sort()

    # handle first response time
    for process in process_list:
        pid = process[2]
        first_response[pid] = -1
        backup[pid] = [process[0], process[1]]

    remaining_process = process_list[:]

    while remaining_process or queue:

        # add the available process to queue
        for process in remaining_process:
            if process[0] <= time:
                queue.append(process)
                remaining_process.remove(process)
        
        # handle corner case - no item in queue
        if not queue:
            gannt.append("Idle")
            time += 1
            continue
        
        # take the first  process from queue 
        process = queue.popleft()

        # handle first response time
        if first_response[process[2]] == -1:
            first_response[process[2]] = time - process[0]
        
        # handle process
        execution_time = min(process[1], time_quanta)
        time += execution_time
        gannt.append(process[2])
        process[1] -= execution_time

        # check new process arrived or not
        for p in remaining_process[:]:
            if p[0] <= time:
                queue.append(p)
                remaining_process.remove(p)
        
        if process[1] == 0:
            pid = process[2]
            arrival_time = backup[pid][0]
            burst_time = backup[pid][1]

            ct = time
            tat = ct - arrival_time
            wt = tat - burst_time
            rt = first_response[pid]

            completed[pid] = [pid, arrival_time, burst_time, ct, wt, tat, rt]
        else:
            queue.append(process)
    
    return {
        'gannt': gannt,
        'completed': completed
    }


def print_table(completed):
    print("Process\tArrival\tBrust\tCT\tWT\tTAT\tRT")

    for key in completed:
        print(f'{completed[key][0]} \t {completed[key][1]} \t {completed[key][2]} \t {completed[key][3]} \t {completed[key][4]} \t {completed[key][5]}\t {completed[key][6]}')


if __name__ == "__main__":
    process_list = [
            [0,5,'p1'],
            [1,4,'p2'],
            [2,2,'p3'],
            [4,1,'p4'],
        ]
        
    time_quanta = 2
        
    res = round_robin_v1(process_list, time_quanta)

    print(res['gannt'])


    print_table(res['completed'])