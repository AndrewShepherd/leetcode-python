import unittest
import big_input
import big_input_2
import big_input_3
from construct_string_with_minimal_cost import Solution

class TestSolution(unittest.TestCase):

    def test_5(self):
        target = big_input_2.target
        words = big_input_2.words
        costs = big_input_2.costs
        sol = Solution()
        output = sol.minimumCost(target, words, costs)
        self.assertEqual(output, 23797) # not definitive

    def test_6(self):
        target = big_input_3.target
        words = big_input_3.words
        costs = big_input_3.costs
        sol = Solution()
        output = sol.minimumCost(target, words, costs)
        self.assertEqual(None, 3571) # not definitive

    def test_4(self):
        target = big_input.target
        words = big_input.words
        costs = big_input.costs
        sol = Solution()
        output = sol.minimumCost(target, words, costs)
        self.assertEqual(output, 3571) # not definitive

    def test_2(self):
        target = "abcdef"
        words = ["abdef","abc","d","def","ef"]
        costs = [100,1,1,10,5]
        sol = Solution()
        output = sol.minimumCost(target, words, costs)
        self.assertEqual(output, 7)

    def test_1(self):
        target = "aaaa"
        words = ["z","zz","zzz"]
        costs = [1,10,100]
        sol = Solution()
        output = sol.minimumCost(target, words, costs)
        self.assertEqual(output, -1)


    def test_3(self):
        target = "wvgafw"
        words = ["wvgafw","w"]
        costs = [1,2]
        sol = Solution()
        output = sol.minimumCost(target, words, costs)
        self.assertEqual(output, 1)







try:
    unittest.main()
except SystemExit:
    None
















