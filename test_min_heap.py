import unittest
from min_heap import heapify, heappop, heappush
import heapq
import random

class TestMinHeap(unittest.TestCase):
    def test_heappush(self):
        random.seed(10)
        for i in range(10):
            test_list = [random.randint(-100, 100) for i in range(10)]
            ans_list = test_list[:]
            heapq.heappush(ans_list, i)
            heappush(test_list, i)
            self.assertEqual(test_list, ans_list, "Error on heappush function")
        

    def test_heappop(self):
        test_heap_1 = [1]
        test_heap_2 = [1,6,2]

        
        self.assertEqual(heappop(test_heap_1), 1)
        self.assertEqual(heappop(test_heap_2), 1)
        self.assertEqual(test_heap_2, [2,6])


    def test_heapify(self):
        random.seed(10)
        for i in range(10):
            test_list = [random.randint(-100, 100) for i in range(10)]
            ans_list = test_list[:]
            heapq.heapify(ans_list)
            heapify(test_list)
            self.assertEqual(test_list, ans_list, "Error on heapify function")

