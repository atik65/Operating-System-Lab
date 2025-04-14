
def sstf(request_sequence, head):
    current_head = head
    seek_count = 0
    sequence = [current_head]

    while request_sequence:
        request_sequence = sorted(request_sequence, key = lambda seq: abs(seq - current_head))
        next_request = request_sequence.pop(0)
        distance = abs(current_head - next_request)
        seek_count += distance
        sequence.append(next_request)
        current_head = next_request

    return {
        'sequence': sequence,
        'seek_count': seek_count
    }


def sstf_v1(request_sequence, head):
    current_head = head
    seek_count = 0
    sequence = [current_head]

    while request_sequence != []:
        request_sequence = sorted(request_sequence, key = lambda seq: abs(seq-current_head))

        next_request = request_sequence.pop(0)
        distance = abs(next_request-current_head)
        seek_count += distance
        sequence.append(next_request)
        current_head = next_request
    
    return {
        'seek_count': seek_count,
        'sequence': sequence
    }

def print_sequence(sequence):
    for seq in sequence:
        print(seq, end=" ---> ")

if __name__ == '__main__':
    req_sequences = [176,79,34,60,92,11,41,114]
    head = 50
    res = sstf_v1(req_sequences, head)
    print("Seek Count = ", res['seek_count'])
    print_sequence(res['sequence'])