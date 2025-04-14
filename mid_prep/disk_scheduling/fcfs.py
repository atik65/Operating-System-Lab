
def fcfs(req_sequences,head):
    current_head = head
    sequence = [head]
    seek_count = 0

    for seq in req_sequences:
        distance = abs(seq - current_head)
        seek_count += distance
        current_head = seq
        sequence.append(seq)
    
    return {
        'sequence': sequence,
        'seek_count': seek_count
    }


def print_sequence(sequence):
    for seq in sequence:
        print(seq, end=' ---> ')


if __name__ == "__main__":
    req_sequences = [176,79,34,60,92,11,41,114]
    head = 50

    res = fcfs(req_sequences, head)
    print("Seek Count = ", res['seek_count'])
    print_sequence(res['sequence'])
