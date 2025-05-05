
def lru(req_sequence, frame_size):
    cache = []
    page_fault = 0

    for page in req_sequence:
        if page not in cache:
            if len(cache) ==  frame_size:
                cache.pop(0)
            page_fault += 1
            cache.append(page)
        else:
            cache.remove(page)
            cache.append(page)

    return page_fault


reference_string =[1,3,0,3,5,6,3]
frame_size = 3
miss = lru(reference_string,frame_size)
print('Total no. of miss = ', miss)

