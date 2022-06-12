import unittest
from min_heap import heappop, heappush

class TestMinHeap(unittest.TestCase):
    def test_heappush(self):
        # Test adding new elements to heap
        test_heap_1 = []
        test_heap_2 = [1, 3, 9, 7, 5]
        for num in [2,3,4,7,6,5,1]:
            heappush(test_heap_1, num)
        heappush(test_heap_2, 4)
        
        
        
        self.assertEqual(test_heap_1, [1,3,2,7,6,5,4], "Error on heappush function")
        self.assertEqual(test_heap_2, [1, 3, 4, 7, 5, 9], "Error on heappush function")

    def test_heappop(self):
        test_heap_1 = [1]
        test_heap_2 = [1,6,2]

        
        self.assertEqual(heappop(test_heap_1), 1)
        self.assertEqual(heappop(test_heap_2), 1)
        self.assertEqual(test_heap_2, [2,6])
