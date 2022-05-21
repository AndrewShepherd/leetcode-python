import unittest
from coin_change import Solution

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = Solution()
        # An non-optimal combination is 13*83 + 1*186 + 4*408 + 8*419
        # Maximising the larger coins does not necessarily create
        # the optimal number
        result = s.coinChange([186,419,83,408], 6249)
        self.assertEqual(20,result)

    def test_2(self):
        s = Solution()
        result = s.coinChange([461,307,4,97,352,446,479,243], 7265)
        # Don't know what the answer is
        # but it should not exceed the time limit
        self.assertEqual(16,result)

try:
    unittest.main()
except SystemExit:
    None