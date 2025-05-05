def c_scan(req_sequence, head):
    seek_count = 0
    sequence = []
    current_head = head

    req_sequence.sort()
    left = [seq for seq in req_sequence if seq < current_head]

    right = [seq for seq in req_sequence if seq >= current_head]

    for seq in right + left:
        distance = abs(seq-current_head)
        seek_count += distance
        sequence.append(seq)
        current_head = seq
    
    return {
        'seek_count': seek_count,
        'sequence': sequence
    }


def print_sequence(sequence):
    for seq in sequence:
        print(seq, end=" ---> ")

if __name__ == '__main__':
    req_sequences = [0,14,41,53,65,67,98,122,124,183,199]
    head = 53
    res = c_scan(req_sequences, head)
    print("Seek Count = ", res['seek_count'])
    print_sequence(res['sequence'])