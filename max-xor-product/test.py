import unittest

from max_xor_product import Solution


class TestSolution(unittest.TestCase):

    def test_5(self):
        sol = Solution()
        a = 12
        b = 5
        n = 4
        result = sol.maximumXorProduct(a, b, n)
        self.assertEqual(98, result)

    def test_1(self):
        sol = Solution()
        a = 6
        b = 7
        n = 5
        result = sol.maximumXorProduct(a, b, n)
        self.assertEqual(930, result)

    def test_2(self):
        sol = Solution()
        a = 1
        b = 6
        n = 3
        result = sol.maximumXorProduct(a, b, n)
        self.assertEqual(12, result)

    def test_3(self):
        sol = Solution()
        a = 0
        b = 3
        n = 1
        result = sol.maximumXorProduct(a, b, n)
        self.assertEqual(2, result)   

    def test_4(self):
        sol = Solution()
        a = 0
        b = 4
        n = 0   
        result = sol.maximumXorProduct(a, b, n)
        self.assertEqual(0, result)     

    def test_4(self):
        sol = Solution()
        a = 0
        b = 6
        n = 1   
        result = sol.maximumXorProduct(a, b, n)
        self.assertEqual(7, result)    

    def test_6(self):
        sol = Solution()
        a = 534496118388925
        b = 712958946092406
        n = 6
        result = sol.maximumXorProduct(a, b, n)
        self.assertEqual(816614199, result)    

    def test_0(self):
        sol = Solution()
        a = 648899250667091
        b = 408304371447992
        n = 0
        result = sol.maximumXorProduct(a, b, n)
        self.assertEqual(186813737, result)   

try:
    unittest.main()
except SystemExit:
    None











