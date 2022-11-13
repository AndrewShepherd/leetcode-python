import unittest
from search_in_sorted_array_ii import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        result = s.search([1,3,1,1], 0)
        self.assertEqual(False, result)


try:
    unittest.main()
except SystemExit:
    None




