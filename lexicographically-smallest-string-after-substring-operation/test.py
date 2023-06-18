import unittest


from smallest_string import Solution


class TestSolution(unittest.TestCase):

    def test_0(self):
        s = Solution()

        st = "acbbc"
        expected = "abaab"
        result = s.smallestString(st)
        self.assertEqual(result, expected)

    def test_1(self):
        s = Solution()

        st = "a"
        expected = "z"
        result = s.smallestString(st)
        self.assertEqual(result, expected)

try:
    unittest.main()
except SystemExit:
    None











