import unittest

from strange_printer import Solution


class TestSolution(unittest.TestCase):

    def test_2(self):
        s = Solution()
        input = "byrvzpjpnbwcgdiqmoydqkojfveyjehmueqbagdaspnqvwsvaucenswlvzpgpnjlwjuzhbncpwcyurynwbzwpvhnmmuujwubulro"
        result = s.strangePrinter(input)
        self.assertEqual(74, result)


    def test_1(self):
        s = Solution()
        input = "aaabbb"
        result = s.strangePrinter(input)
        self.assertEqual(2, result)

    def test_0(self):
        s = Solution()
        input = "aba"
        result = s.strangePrinter(input)
        self.assertEqual(2, result)

    def test_3(self):
        s = Solution()
        input = "iuhahfssjjycfnjpdyzgvmesdklgzhvpsmgdluwvrlijbynidsbxfrxvnxawolcmtiowrpqhalfklklnztnyndsnasgoajeyqkdo"
        result = s.strangePrinter(input)
        self.assertEqual(75, result)

    def test_4(self):
        s = Solution()
        input = "moiulcxajmhtxipdymndmvezgitoddbbapjhsyrkduimlxhcamfpdxaqqxdbmrfmrmdsdgeravgzxwpczgfhbxidembvwehtqlvo"
        result = s.strangePrinter(input)
        self.assertEqual(75, result)       
       

try:
    unittest.main()
except SystemExit:
    None





