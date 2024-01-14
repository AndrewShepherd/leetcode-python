import unittest

from find_beautiful_indices import Solution


class TestSolution(unittest.TestCase):



    def test_0(self):
        sol = Solution()
        s = "isawsquirrelnearmysquirrelhouseohmy"
        a = "my"
        b = "squirrel"
        k = 15
        result = sol.beautifulIndices(s, a, b, k)
        self.assertEqual([16,33], result)

    def test_1(self):
        sol = Solution()
        s = "abcd"
        a = "a"
        b = "a"
        k = 4
        result = sol.beautifulIndices(s, a, b, k)
        self.assertEqual([0], result)

        
    def test_3(self):
        sol = Solution()
        s = "abcdzzzzabzzzzzcd"
        a = "ab"
        b = "cd"
        k = 2
        result = sol.beautifulIndices(s, a, b, k)
        self.assertEqual([0], result)

try:
    unittest.main()
except SystemExit:
    None














