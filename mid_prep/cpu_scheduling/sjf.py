# SJF -- Shortest Job First
def sjf(process_list):
    time = 0
    gannt = []
    completed = {}

    

    while process_list != []:
        available = []

        # find the available processes
        for process in process_list:
            arrival_time = process[1]
            if arrival_time <= time:
                available.append(process)
        
        # check the corner case -- no available process
        if available == []:
            time +=1
            gannt.append("Idle")
        else:
            # sort available process based on brust time
            available.sort()

            # handle process
            process = available[0]

            pid = process[2]
            arrival_time = process[1]
            brust_time = process[0]

            time += brust_time
            # CT
            ct = time

            # TAT
            tat = ct - arrival_time

            # WT
            wt = tat - brust_time

            # remove the porcess
            process_list.remove(process)

            gannt.append(pid)
            completed[pid] = [pid, brust_time, arrival_time, ct, tat, wt]

    return {
        'gannt':gannt,
        'completed': completed
    }





def sjf_v1(process_list):
    time = 0
    gannt = []
    completed = {}

    while process_list != []:
        available = []

        # check for avaiable processes
        for process in process_list:
            arrival_time = process[1]
            if arrival_time <= time :
                available.append(process)
        
        # corner case -- if no process available
        if available == []:
            time += 1
            gannt.append("Idle")
            continue

        else:

            # sort the available porcess
            available.sort()

            process = available[0]
            pid = process[2]
            arrival_time = process[1]
            brust_time = process[0]

            time += brust_time

            # CT
            ct = time

            # TAT
            tat = ct - arrival_time

            #WT 
            wt = tat - brust_time

            # append to process to gannt
            gannt.append(pid)

            # remove the process
            process_list.remove(process)

            # append to completed
            completed[pid] = [pid, brust_time, arrival_time, ct, tat, wt]

    return {
        'gannt' : gannt,
        'completed' : completed
    } 

            



def sjf_v2(process_list):
    time = 0
    gannt = []
    completed = {}

    while process_list != []:
        available = []

        for process in process_list:
            arrival_time = process[1]
            if arrival_time <= time:
                available.append(process)
                
        # no process available
        if available == []:
            time += 1
            gannt.append("Idle")
            continue
        else:
            # sort available porcess
            available.sort()

            process = available[0]
            pid = process[2]
            arrival_time = process[1]
            brust_time = process[0]

            time += brust_time

            # CT
            ct = time

            # TAT
            tat = ct - arrival_time

            # WT
            wt = tat - brust_time

            # remove the process
            process_list.remove(process)
            gannt.append(pid)
            completed[pid] =  [pid, brust_time, arrival_time, ct, tat, wt]
    
    return {
        'gannt' : gannt,
        'completed': completed
    }



def print_table(completed):
    print("Process\tBrust\tArrival\tCT\tTAT\tWT")

    for key in completed:
        print(f'{completed[key][0]}\t{completed[key][1]}\t{completed[key][2]}\t{completed[key][3]}\t{completed[key][4]}\t{completed[key][5]}')

if __name__ == "__main__":
# process = [brust_time, arrival_time, pid]
    process_list = [
            [6,2,'p1'],
            [2,5,'p2'],
            [8,1,'p3'],
            [3,0,'p4'],
            [4,4,'p5'], 
        ]
    
    res = sjf_v2(process_list)
    print(res['gannt'])
    print_table(res['completed'])
