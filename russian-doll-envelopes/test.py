import unittest

from russian_doll_envelopes import Solution
from large_testcase import large_testcase

class TestSolution(unittest.TestCase):

    def run_test(self, envelopes, exprectedResult):
        s = Solution()
        result = s.maxEnvelopes(envelopes)
        self.assertEqual(result, exprectedResult)

    def test_one(self):
        self.run_test([[5,4],[6,4],[6,7],[2,3]], 3)

    def test_two(self):
        self.run_test([[1,1],[1,1],[1,1]], 1)

    def test_three(self):
        self.run_test(large_testcase, 127) 

try:
    unittest.main()
except SystemExit:
    None
