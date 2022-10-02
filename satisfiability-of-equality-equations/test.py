import unittest


from satisfiability_of_equality_equations import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, input, expectedResult):
        sol= Solution()
        result = sol.equationsPossible(input)
        self.assertEqual(result, expectedResult)

    def test_1(self):
        self.run_test(
            ["a==b","b!=a"],
            False
        )

    def test_2(self):
        self.run_test(
            ["a==b","b==a"],
            True
        )

    def test_4(self):
        self.run_test(
            ["a!=a"],
            False
        )

    def test_3(self):
        self.run_test(
            ["h==j","c!=g","e==j","f!=e","g!=e","j==h","h!=e","j!=a"],
            False
        )
    
    def test_0(self):
        self.run_test(
            ["a==b","b!=c","c==a"],
            False
        )
try:
    unittest.main()
except SystemExit:
    None

