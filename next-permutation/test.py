import unittest
from next_permutation import Solution




class TestSolution(unittest.TestCase):


    def test_0(self):
        s = Solution()
        l = [1,1,5]
        s.nextPermutation(l)
        self.assertEqual([1,5,1], l)

    def test_1(self):
        s = Solution()
        l = [1,2]
        s.nextPermutation(l)
        self.assertEqual([2,1], l)

    def test_2(self):
        s = Solution()
        l = [1,3,2]
        s.nextPermutation(l)
        self.assertEqual([2,1,3], l)

    def test_3(self):
        s = Solution()
        l = [2,3,1]
        s.nextPermutation(l)
        self.assertEqual([3,1,2], l)

    def test_4(self):
        s = Solution()
        l = [5,1,1]
        s.nextPermutation(l)
        self.assertEqual([1,1,5], l)

try:
    unittest.main()
except SystemExit:
    None