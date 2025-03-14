#Shortest Seek Time First: SSTF disk scheduling

def sstf(request_sequence, initial_head):
    current_head = initial_head
    sequence = [current_head]
    total_seektime = 0

    while request_sequence !=[]:
        request_sequence = sorted(request_sequence, key= lambda x: abs(x-current_head))
        next_request = request_sequence.pop(0)
        sequence.append(next_request)
        total_seektime += abs(next_request - current_head)
        current_head = next_request
    return total_seektime, sequence
   
def take_input():
    head = int(input("Enter the initial head position: "))
    n = int (input("Enter the total number of sequene: "))
    req_sequences = []

    for i in range(n):
        req = int(input(f'Enter sequence number  {i+1} : '))
        req_sequences.append(req)
    return req_sequences, head

def print_sequence(sequences):
    for i in range(len(sequences)):
        if i < len(sequences)-1:
            print(sequences[i], end=" ---> ")
        else: 
            print(sequences[i], end="")

if __name__ == "__main__":
    inputs = take_input()
    req_sequences = inputs[0]
    head = inputs[1]

    res = sstf(req_sequences, head)
    print("Total Seek Operation", res[0])
    print_sequence(res[1])