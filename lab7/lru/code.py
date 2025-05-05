def lru_page_replacement(pages, capacity):
    cache = []
    page_faults = 0

    for page in pages:
        if page not in cache:
            if len(cache) == capacity:
                # Remove the least recently used page (first in the list)
                cache.pop(0)
            page_faults += 1
            cache.append(page)
        else:
            # Move the page to the end to mark it as recently used
            cache.remove(page)
            cache.append(page)

        print(f"Page: {page} => Cache: {cache}")

    print(f"\nTotal Page Faults: {page_faults}")

# Example usage
pages = [1, 2, 3, 2, 1, 4, 5]
pages1 =[2,3,2,1,5,2,4,5,3,2,5,2]
capacity = 3
lru_page_replacement(pages1, capacity)
