# Disk Scheduling
# First Come First Serve (FCFS) Scheduling

def FCFS(sequences, head):
    seek_count = 0
    current_head = head
    current_sequence =[head]

    for seq in sequences:
        distance = abs(current_head - seq)
        seek_count += distance
        current_head = seq
        current_sequence.append(seq)
    
    return seek_count, current_sequence
    
    
def take_input():
    head = int(input("Enter the initial head position: "))
    n = int(input("Enter the number of seqence: "))
    req_sequences = []

    for i in range(n):
        req = int(input(f'Enter {i+1} sequence number: '))
        req_sequences.append(req)
    return req_sequences, head

def print_sequence(sequences):
    for seq in sequences:
        print(seq, end=" ---> ")

if __name__ == "__main__":
    inputs = take_input()
    req_sequences = inputs[0]
    head = inputs[1]

    res = FCFS(req_sequences, head)
    print('Total Seek count = ', res[0])  
    print_sequence(res[1])