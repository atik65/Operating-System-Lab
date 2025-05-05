def sstf(req_sequence, head):
    current_head = head
    sequence = [current_head]
    seek_count = 0

    while req_sequence:
        req_sequence = sorted(req_sequence, key=lambda req: abs(req - current_head))

        next_request = req_sequence.pop(0)
        distance = abs(current_head - next_request)
        seek_count += distance
        sequence.append(next_request)
        current_head = next_request

    return {
        'seek_count': seek_count,
        'sequence':sequence
    }

def sstf_v1 (request_sequence, head):
    current_head = head
    seek_count = 0
    sequence = [current_head]

    while request_sequence:
        request_sequence = sorted(request_sequence, key=lambda seq: abs(seq-current_head))

        next = request_sequence.pop(0)
        seek_count += abs(next-current_head)
        sequence.append(next)
        current_head = next
    return {
        'seek_count': seek_count,
        'sequence': sequence
    }


def print_sequence(sequence):
    for seq in sequence:
        print(seq, end=' ---> ')


if __name__ == "__main__":
    req_sequence = [176,79,34,60,92,11,41,114]
    head = 50
    res = sstf_v1(req_sequence, head)
    print('Seek count = ', res['seek_count'])
    print_sequence(res['sequence'])
