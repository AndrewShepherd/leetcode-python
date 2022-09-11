import unittest
from number_of_weak_characters import Solution




class TestSolution(unittest.TestCase):
    def test_0(self):
        s = Solution()
        result = s.numberOfWeakCharacters([[2,2],[3,3]])
        self.assertEqual(1, result)

    def test_1(self):
        s = Solution()
        result = s.numberOfWeakCharacters([[5,5],[6,3],[3,6]])
        self.assertEqual(0, result)

try:
    unittest.main()
except SystemExit:
    None


