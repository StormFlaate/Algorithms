import heapq


def _sift_up(heap: list[int], startpos:int, endpos:int):
    n: int = startpos
    while n < endpos:
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


def _shift_down(heap: list[int], startpos:int, endpos:int):
    n: int = startpos
    while n > endpos and heap[(n-1)//2] > heap[n]:
        tmp = heap[n]
        heap[n] = heap[(n-1)//2]
        heap[(n-1)//2] = tmp
        n = (n-1)//2


def heappush(heap: list[int], item: int) -> list[int]:
    """
    heappush will add a new item at the end/bottom of the heap (really just a list)
    and then it will bump its way upward. It will stop if it is at the top (index 0)
    or if the parent node is of bigger value.
    """
    heap.append(item)
    _shift_down(heap, len(heap)-1, 0)
    
    return heap

def heappop(heap: list[int]) -> int:
    if len(heap) == 1:
        return heap.pop() 
    min_val = heap[0]
    heap[0] = heap.pop()
    _shift_up(heap, 0, len(heap))
    
    return min_val











