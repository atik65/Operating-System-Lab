def optimal_page_replacement(pages, capacity):
    memory = []
    page_faults = 0

    for i in range(len(pages)):
        current_page = pages[i]

        if current_page in memory:
            continue  

        if len(memory) < capacity:
            memory.append(current_page)
            page_faults += 1
        else:
            # Find the page to be replaced
            future_uses = []

            for page in memory:
                if page in pages[i+1:]:
                    index = pages[i+1:].index(page)
                else:
                    index = float('inf')  
                future_uses.append(index)

            replace_index = future_uses.index(max(future_uses))
            memory[replace_index] = current_page
            page_faults += 1

    print("Total Page Faults:", page_faults)

pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 3]
capacity = 4
optimal_page_replacement(pages, capacity)