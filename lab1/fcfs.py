import copy

data =[]
backup = []

process_no = int(input("Enter No of process:"))


for i in range(0,process_no):
    processID = input(f"Enter Process ID =")
    arrival = int(input(f"Enter Arrival Time  ="))
    brust = int(input(f"Enter Brust Time of ="))
   
    process = {
        "process": processID,
        "arrival": arrival,
        "brust": brust
    }
    data.append(process)


def sort_method(process):
    return process['arrival']

# backup process data before sorting
backup = copy.deepcopy(data)

# sorting process data
data.sort(key = sort_method)


cpu_execution_now = 0

#calculate completion time
for process in data:
    # print("brust = ", process)
    CT = cpu_execution_now + process['brust']
    WT = cpu_execution_now - process['arrival']
    cpu_execution_now = CT
   
   
    process['CT'] = cpu_execution_now
    process['WT'] = WT
   
    TA = process['CT'] - process['arrival']
    process['TAT'] = TA



# printing result in tabular form
print("Process\tArrival\tBrust\tCT\tWT\tTAT")
for process in data:
    print(f"{process['process']}\t{process['arrival']}\t{process['brust']}\t{process['CT']}\t{process['WT']}\t{process['TAT']}")
