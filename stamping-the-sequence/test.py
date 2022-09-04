import unittest
from stamping_the_sequence import Solution

class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        result = s.movesToStamp("abc", "ababc")
        self.assertEqual([0,2], result)

    def test_2(self):
        s = Solution()
        result = s.movesToStamp("abca", "aabcaca")
        self.assertEqual([0, 3, 1], result)

    def test_3(self):
        s = Solution()
        result = s.movesToStamp("atvbq", "aaatvatvbqbqbqq")
        self.assertEqual([10, 9, 0, 1, 2, 7, 5], result)

    def test_4(self):
        s = Solution()
        result = s.movesToStamp("ffc", "ffffcfffffffffc")
        self.assertEqual([0, 4, 2, 6, 8, 10, 12], result)

    def test_5(self):
        s = Solution()
        result = s.movesToStamp("voy", "vvyyvoyvvoyoyoy")
        self.assertEqual([], result)

    def test_6(self):
        s = Solution()
        result = s.movesToStamp("qxq", "qxqxqxqqxqxqqxqxqxqqxqxqqqxqqxqqqxqqxxqxqqxqqqxqqq")
        self.assertEqual([], result)



try:
    unittest.main()
except SystemExit:
    None

