import unittest
from minimum_amount_of_time_to_collect_garbage import Solution




class TestSolution(unittest.TestCase):


    def test_2(self):
        s = Solution()
        result = s.garbageCollection(["G","P","GP","GG"], [2,4,3])
        self.assertEqual(21, result)

    def test_1(self):
        s = Solution()
        result = s.garbageCollection(["MMM","PGM","GP"], [3,10])
        self.assertEqual(37, result)

try:
    unittest.main()
except SystemExit:
    None
