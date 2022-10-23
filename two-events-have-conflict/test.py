import unittest

from have_conflict import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, event1, event2, expected_result):
        sol= Solution()
        result = sol.haveConflict(event1, event2)
        self.assertEqual(result, expected_result)


    def test_1(self):
        self.run_test(event1 = ["01:15","02:00"], event2 = ["02:00","03:00"], expected_result=True)

    def test_2(self):
        self.run_test(event1 = ["01:00","02:00"], event2 = ["01:20","03:00"], expected_result=True)

    def test_3(self):
        self.run_test(["10:00","11:00"], event2 = ["14:00","15:00"], expected_result=False)

try:
    unittest.main()
except SystemExit:
    None










