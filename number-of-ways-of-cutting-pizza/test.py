import unittest
from number_of_ways_of_cutting_pizza import Solution

class TestSolution(unittest.TestCase):

    def test_1(self):
        pizza = [".A..A","A.A..","A.AA.","AAAA.","A.AA."]
        k = 5
        output = 153
        s = Solution()
        self.assertEqual(output, s.ways(pizza, k))

    def test_2(self):
        pizza = ["A..","AAA","..."]
        k = 3
        output = 3
        s = Solution()
        self.assertEqual(output, s.ways(pizza, k))





try:
    unittest.main()
except SystemExit:
    None












