def sjf(process_list):
    time = 0
    gannt =[]
    completed ={}

    while process_list !=[]:
        available = []

        for process in process_list:
            arrival_time = process[1]
            if arrival_time <=time:
                available.append(process)

        if available == []:
            gannt.append("Idle")
            time +=1
        else:
            available.sort()
            process = available[0]

            pid = process[2]
            arrival_time = process[1]
            burst_time = process[0]

            time += burst_time

            ct = time
            tat = ct - arrival_time
            wt = tat - burst_time

            gannt.append(pid)
            process_list.remove(process)
            completed[pid] = [pid,burst_time,arrival_time,ct,tat,wt]
    return {
        'gannt': gannt,
        'completed': completed
    }



def sjf_v1(process_list):
    gannt =[]
    completed ={}
    time = 0

    while process_list:
        available = []

        for process in process_list:
            arrival_time = process[1]
            if arrival_time <= time:
                available.append(process)
        
        if available == []:
            gannt.append('Idle')
            time += 1
        else:
            available.sort()
            process = available[0]
            
            pid = process[2]
            arrival_time = process[1]
            burst_time = process[0]

            time += burst_time

            ct = time
            tat = ct - arrival_time
            wt = tat - burst_time

            gannt.append(pid)
            process_list.remove(process)
            completed[pid] = [pid,burst_time,arrival_time,ct,tat,wt]
    return {
        'gannt': gannt,
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
    
    res = sjf_v1(process_list)
    print(res['gannt'])
    print_table(res['completed'])
