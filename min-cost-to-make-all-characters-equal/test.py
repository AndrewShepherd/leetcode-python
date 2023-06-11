import unittest


from minimum_cost import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        input = "0011"
        result = s.minimumCost(input)
        self.assertEqual(2, result)

    def test_0(self):
        s = Solution()
        input = "010101"
        result = s.minimumCost(input)
        self.assertEqual(9, result)

try:
    unittest.main()
except SystemExit:
    None








