
def fcfs(process_list):
    time = 0
    gant = []
    completed = {}

    # sort process list based on arrival time
    process_list.sort()

    for process in process_list:
        arrival_time = process[0]
        brust_time = process[1]
        pid = process[2]

        # handle corner case
        if(time < arrival_time):
            gant.append("Idle")
            time += 1
            continue
        
        # handle process
        time += brust_time
        gant.append(pid)

        # CT
        ct = time
        # TAT
        tat = ct - arrival_time
        # WT
        wt = tat - brust_time

        # completed.append(
        #     [pid,arrival_time, brust_time, ct,  wt, tat]
        # )
        completed[pid] =  [pid,arrival_time, brust_time, ct,  wt, tat]
    return {
        'gant': gant,
        'completed': completed
    }

def print_table(completed):
    print("Process\tArrival\tBrust\tCT\tWT\tTAT")

    for key in completed:
        print(f'{completed[key][0]} \t {completed[key][1]} \t {completed[key][2]} \t {completed[key][3]} \t {completed[key][4]} \t {completed[key][5]}')

if __name__ == "__main__":
    # process = [arrival_time, brust_time, process_id]
    process_list = [
        [2,5,'p0'],
        [0,3,'p1'],
        [4,4,'p2'],
    ]

    res = fcfs(process_list)
    print(res['gant'])
    print_table(res['completed'])