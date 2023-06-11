import unittest


from count_of_integers import Solution


class TestSolution(unittest.TestCase):

    def test_0(self):
        s = Solution()

        num1 = "1000000007"
        num2 = "2000000014"
        min_sum = 1
        max_sum = 400

        expected = 1 # WHAT!?!?
        result = s.count(num1, num2, 1, 400)
        self.assertTrue(result < 1000000007)
        self.assertEqual(result, expected)


    def test_1(self):
        s = Solution()
        num1 = "1"
        num2 = "12"
        min_sum = 1
        max_sum = 8
        result = s.count(num1, num2, min_sum, max_sum)
        self.assertEqual(11, result)

    def test_2(self):
        s = Solution()
        num1 = "1"
        num2 = "5"
        min_sum = 1
        max_sum = 5
        result = s.count(num1, num2, min_sum, max_sum)
        self.assertEqual(5, result)

try:
    unittest.main()
except SystemExit:
    None











