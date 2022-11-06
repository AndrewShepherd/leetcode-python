import unittest

from most_popular_video_creator import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, creators, ids, views, expected_result):
        sol= Solution()
        result = sol.mostPopularCreator(creators, ids, views)
        self.assertEqual(result, expected_result)

    def test_3(self):
        self.run_test(creators = ["alice","bob","alice","chris"], ids = ["one","two","three","four"], views = [5,10,5,4], expected_result=[["alice","one"],["bob","two"]])

    def test_1(self):
        self.run_test(creators = ["alice","alice","alice"], ids = ["a","b","c"], views = [1,2,2], expected_result=[["alice","b"]])


try:
    unittest.main()
except SystemExit:
    None












