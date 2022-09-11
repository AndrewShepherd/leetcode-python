import unittest
from check_distances_between_same_letters import Solution




class TestSolution(unittest.TestCase):


    def test_1(self):
        s = Solution()
        result = s.checkDistances("abaccb", distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.assertEqual(True, result)

    def test_0(self):
        s = Solution()
        result = s.checkDistances(s = "aa", distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.assertEqual(False, result)
 

try:
    unittest.main()
except SystemExit:
    None

