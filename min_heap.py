import heapq


# sift up the array
def _sift_up(heap: list[int], pos:int):
    newitem:int = heap[pos]
    endpos:int = len(heap)
    startpos:int = pos
    
    childpos:int = 2*pos+1
    while childpos < endpos:
        rightpos:int = childpos+1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos

        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos+1
    heap[pos] = newitem

    _sift_down(heap, startpos, pos)


# sift down the array
def _sift_down(heap: list[int], startpos:int, pos: int):
    newitem:int = heap[pos]

    while pos > startpos:
        parentpos = (pos-1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue

        break
    heap[pos] = newitem    
        

def heappush(heap: list[int], item: int) -> list[int]:
    """
    heappush will add a new item at the end/bottom of the heap (really just a list)
    and then it will bump its way upward. It will stop if it is at the top (index 0)
    or if the parent node is of bigger value.
    """
    heap.append(item)
    _sift_down(heap, 0, len(heap)-1)
    
    return heap

def heappop(heap: list[int]) -> int:
    if len(heap) == 1:
        return heap.pop() 
    min_val = heap[0]
    heap[0] = heap.pop()
    _sift_up(heap, 0)
    
    return min_val

def heapify(heap:list[int]):
    n = len(heap)

    for i in reversed(range(n//2)):
        _sift_up(heap, i)









