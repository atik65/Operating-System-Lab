from collections import deque

def fifo_page_replacement(page_reference, frame_size):
    memory =[]
    miss = 0
    queue = deque()
    

    for page in page_reference:
        if page in memory:
            continue

        miss +=1

        if len(memory) < frame_size:
            memory.append(page)
            queue.append(page)
        else:
            oldest_page = queue.popleft()
            memory.remove(oldest_page)
            memory.append(page)
            queue.append(page)

    return miss
    

reference_string =[1,3,0,3,5,6,3]
frame_size = 3

miss = fifo_page_replacement(reference_string, frame_size)
print('Total no. of miss = ', miss)