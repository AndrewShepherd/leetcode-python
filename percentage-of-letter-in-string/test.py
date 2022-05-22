import unittest


from percentage_letter import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, s, o, expectedResult):
        sol= Solution()
        result = sol.percentageLetter(s, o)
        self.assertEqual(result, expectedResult)

    def test_one(self):
        self.run_test("foobar", "o", 33)

    def test_two(self):
        self.run_test("jjjj", "k", 0)

try:
    unittest.main()
except SystemExit:
    None
