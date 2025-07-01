from longest_common_prefix import Solution
import unittest

class TestSolution(unittest.TestCase):
    def test_1(self):
        words = ["jump","run","run","jump","run"]
        expected_result = [3,0,0,3,3]

        sol = Solution()
        result = sol.longestCommonPrefix(words)
        self.assertEqual(expected_result, result)

    def test_2(self):
        words = ["dog","racer","car"]
        expected_result = [0,0,0]

        sol = Solution()
        result = sol.longestCommonPrefix(words)
        self.assertEqual(expected_result, result)

    def test_0(self):
        words = ["fb","bdaac","ee","defed","fdd","df","cbadc","b","f","bede","ff"]
        expected_result = [0,0,0,0,1,0,0,0,1,1,0]

        sol = Solution()
        result = sol.longestCommonPrefix(words)
        self.assertEqual(expected_result, result)



try:
    unittest.main()
except SystemExit:
    None


