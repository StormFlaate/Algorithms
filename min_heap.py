
def heappush(heap: list[int], item: int) -> list[int]:
    """
    heappush will add a new item at the end/bottom of the heap (really just a list)
    and then it will bump its way upward. It will stop if it is at the top (index 0)
    or if the parent node is of bigger value.
    """
    heap.append(item)
    n: int = len(heap)-1
    while n > 0 and heap[(n-1)//2] > heap[n]:
        heap[n] = heap[(n-1)//2]
        heap[(n-1)//2] = item
        n = (n-1)//2
    
    return heap

def heappop(heap: list[int]) -> int:
    if len(heap) == 1:
        return heap.pop() 
    min_val = heap[0]
    heap[0] = heap.pop()
    n: int = 0
    while n < len(heap):
        switch = n
        if 2*n+1 < len(heap) and heap[2*n+1] < heap[switch]:
            switch = 2*n+1
        if 2*n+2 < len(heap) and heap[2*n+2] < heap[switch]:
            switch = 2*n+2
        if switch == n:
            break
        tmp = heap[n]
        heap[n] = heap[switch]
        heap[switch] = tmp
        n = switch
    return min_val











