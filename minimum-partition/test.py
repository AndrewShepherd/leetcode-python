import unittest
from minimum_partition import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        s = "165462"
        k = 60
        self.assertEqual(4, Solution().minimumPartition(s, k))

    def test_2(self):
        s = "238182"
        k = 5
        self.assertEqual(-1, Solution().minimumPartition(s, k))


try:
    unittest.main()
except SystemExit:
    None


