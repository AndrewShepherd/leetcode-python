import unittest

from sum_of_number_and_its_reverse import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, num: int, expected_result):
        sol= Solution()
        result = sol.sumOfNumberAndReverse(num)
        self.assertEqual(result, expected_result)


    def test_1(self):
        self.run_test(443, True)

    def test_2(self):
        self.run_test(63, False)

    def test_0(self):
        self.run_test(181, True)

    def test_4(self):
        self.run_test(9779, True)

    def test_5(self):
        self.run_test(3923, False)

    def test_6(self):
        self.run_test(4103, True)




try:
    unittest.main()
except SystemExit:
    None









