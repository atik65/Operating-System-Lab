#Scan Disk Sheduling Algorithm
def scan_disk_sheduling(request_sequence, initial_head):
    current_head = initial_head
    sequence = []
    total_seektime = 0
    
    request_sequence = sorted(request_sequence)
    
    left = [r for r in request_sequence if r < current_head]
    right = [r for r in request_sequence if r >= current_head]
    
    left.reverse()

    for request in  right + left:
        if request > 0:
            total_seektime += abs(request - current_head)
        sequence.append(request)
        current_head = request      
    
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
   
    res = scan_disk_sheduling(req_sequences, head)
    print("Total Seek ope Operation", res[0])
    print_sequence(res[1])
