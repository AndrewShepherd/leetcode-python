import unittest

from alice_and_bob_playing_flower_game import Solution


class TestSolution(unittest.TestCase):



    def test_1(self):
        sol = Solution()
        n = 3
        m = 2
        result = sol.flowerGame(n, m)
        self.assertEqual(3, result)

    def test_2(self):
        sol = Solution()
        n = 1
        m = 1
        result = sol.flowerGame(n, m)
        self.assertEqual(0, result)





try:
    unittest.main()
except SystemExit:
    None

















