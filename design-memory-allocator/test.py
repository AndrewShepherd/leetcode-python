import unittest
from design_memory_allocator import Allocator


class TestSolution(unittest.TestCase):
    def test_1(self):
        loc = Allocator(10); # Initialize a memory array of size 10. All memory units are initially free.
        self.assertEqual(0, loc.allocate(1, 1)) # The leftmost block's first index is 0. The memory array becomes [1,_,_,_,_,_,_,_,_,_]. We return 0.
        self.assertEqual(1, loc.allocate(1, 2)) # The leftmost block's first index is 1. The memory array becomes [1,2,_,_,_,_,_,_,_,_]. We return 1.
        self.assertEqual(2, loc.allocate(1, 3)) # The leftmost block's first index is 2. The memory array becomes [1,2,3,_,_,_,_,_,_,_]. We return 2.
        self.assertEqual(1, loc.free(2)) # Free all memory units with mID 2. The memory array becomes [1,_, 3,_,_,_,_,_,_,_]. We return 1 since there is only 1 unit with mID 2.
        self.assertEqual(3, loc.allocate(3, 4)) # The leftmost block's first index is 3. The memory array becomes [1,_,3,4,4,4,_,_,_,_]. We return 3.
        self.assertEqual(1, loc.allocate(1, 1)) # The leftmost block's first index is 1. The memory array becomes [1,1,3,4,4,4,_,_,_,_]. We return 1.
        self.assertEqual(6, loc.allocate(1, 1)) # The leftmost block's first index is 6. The memory array becomes [1,1,3,4,4,4,1,_,_,_]. We return 6.
        self.assertEqual(3, loc.free(1)); # Free all memory units with mID 1. The memory array becomes [_,_,3,4,4,4,_,_,_,_]. We return 3 since there are 3 units with mID 1.
        self.assertEqual(-1, loc.allocate(10, 2)); # We can not find any free block with 10 consecutive free memory units, so we return -1.
        self.assertEqual(0, loc.free(7)); # Free all memory units with mID 7. The memory array remains the same since there is no memory unit with mID 7. We return 0.

    def test_2(self):
        # ["Allocator","allocate","allocate","allocate","allocate","free","free","free","allocate","allocate","allocate","allocate","free","free","free","free","free","free","free","allocate","free","free","allocate","free","allocate","allocate","free","free","free","allocate","allocate","allocate","allocate","free","allocate","free","free","allocate","allocate","allocate","allocate","allocate","allocate","allocate","free","free","free","free"]
        # [[50],[12,6],[28,16],[17,23],[50,23],[6],[10],[10],[16,8],[17,41],[44,27],[12,45],[33],[8],[16],[23],[23],[23],[29],[38,32],[29],[6],[40,11],[16],[22,33],[27,5],[3],[10],[29],[16,14],[46,47],[48,9],[36,17],[33],[14,24],[16],[8],[2,50],[31,36],[17,45],[46,31],[2,6],[16,2],[39,30],[33],[45],[30],[27]]
        loc = Allocator(50)
        inputs = [[12,6],[28,16],[17,23],[50,23],[6],[10],[10],[16,8],[17,41],[44,27],[12,45],[33],[8],[16],[23],[23],[23],[29],[38,32],[29],[6],[40,11],[16],[22,33],[27,5],[3],[10],[29],[16,14],[46,47],[48,9],[36,17],[33],[14,24],[16],[8],[2,50],[31,36],[17,45],[46,31],[2,6],[16,2],[39,30],[33],[45],[30],[27]]

        # The 19th is bad
        loc.allocate(12, 6) # 0
        loc.allocate(28, 16) # 12
        loc.allocate(17, 23) # -1
        loc.allocate(50, 23) # -1
        loc.free(6) # 0
        loc.free(10) # 0
        loc.free(10) # 0
        loc.allocate(16, 8) # 0
        loc.allocate(17, 41)
        loc.allocate(44, 27)
        loc.allocate(12, 45)
        loc.free(33)  #12
        loc.free(8)
        loc.free(16)
        loc.free(23)
        loc.free(23)
        loc.free(23)
        loc.free(29) # 18
        self.assertEqual(12, loc.allocate(38, 32))

        for i in inputs:
            if len(i) == 2:
                loc.allocate(i[0], [1])
            else:
                loc.free(i[0])

try:
    unittest.main()
except SystemExit:
    None




