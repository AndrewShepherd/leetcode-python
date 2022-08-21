import unittest


from construct_smallest_number_from_di_string import Solution

class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        pattern = "IIIDIDDD"
        output = "123549876"
        self.assertEqual(output, s.smallestNumber(pattern))

    def test_2(self):
        s = Solution()
        pattern = "DDD"
        output = "4321"
        self.assertEqual(output, s.smallestNumber(pattern))


try:
    unittest.main()
except SystemExit:
    None
