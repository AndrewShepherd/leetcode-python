import unittest
from longest_subsequence_with_limited_sum import Solution




class TestSolution(unittest.TestCase):


    def test_2(self):
        s = Solution()
        result = s.answerQueries([4,5,2,1], [3,10,21])
        self.assertEqual([2,3,4], result)

    def test_1(self):
        s = Solution()
        result = s.answerQueries([2,3,4,5], [1])
        self.assertEqual([0], result)

    def test_3(self):
        s = Solution()
        result = s.answerQueries([736411,184882,914641,37925,214915], [331244,273144,118983,118252,305688,718089,665450])
        self.assertEqual([2,2,1,1,2,3,3], result)

    def test_0(self):
        s = Solution()
        result = s.answerQueries([736411,184882,914641,37925,214915], [718089])
        self.assertEqual([3], result)

 

try:
    unittest.main()
except SystemExit:
    None