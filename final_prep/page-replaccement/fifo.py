def fifo(page_sequence, frame_size):

    queue = []
    page_fault = 0

    for page in page_sequence:
        if page not in queue:
            if len(queue) ==  frame_size:
                queue.pop(0)
            
            page_fault += 1
            queue.append(page)
    
    return page_fault

reference_string =[1,3,0,3,5,6,3]
frame_size = 3

miss = fifo(reference_string, frame_size)
print('Total no. of miss = ', miss)

