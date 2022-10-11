import unittest


from robot_with_string import Solution
from big_input import big_string

class TestSolution(unittest.TestCase):

    def run_test(self, pref, expectedResult):
        sol= Solution()
        result = sol.robotWithString(pref)
        self.assertEqual(result, expectedResult)

    def test_7(self):
        self.run_test(
            "zza",
            "azz"
        )

    def test_0(self):
        self.run_test(
            "bdda",
            "addb"
        )

    def test_3(self):
        self.run_test(
            "ibwqrkn",
            "biknrqw"
        )

    def test_6(self):
        self.run_test(
            "evokzbuginbpptrfaamp",
            "aafmprtppbnigubzkove"
        )

    def test_2(self):
        big_input = "erqzmzchvpblikmmwnqbrwvdiaomkvrtiuoshvumbjitswimabygncijmnvjdqmhkaasyekbcvwqdmovtsnehtljntoyqafizjigroixsdlnenlheeureaoivqkmpfznqqowgwguifsbizfhogwvuhinvzxbeeztpfmnmtdjchtewilspapiauiguvlnzmchayxojpqkehlytkurvnsaaqoshuxjuenrddupjljmjsnetlkrreqnojxlgluptprnluetvfsydjjxguttyztbmiulkhjwnfonmaomqbtryfgrhhzktgkqeylbqbopswjuoyzypdpjqzxeoauuxfmplcrbrrexsyrzjcoxsfcvxsynqvzyeamzgorpazmgupaitpffurhpjcyvjkhnitbuthpvjcgiacjvrhfjlvrsltmtflmgipkjxdlipfexhkcpvbcrxotypzrqavninsvmneygdvxqejeioaihlsxjmlyqqulgldasqnfhosfekqtjeoipoknslwdruglcntburhadgfeffbynmvldjmjfpdlijeghhlyepgttwzmlqyidsuhnrchlqfgplxoqfzqbuychvhnfeelgozqqjrcmggplmwokfhbyohnbpzbhrqwfiptuxansirzcmiphycaiuldozgliteabvjzthapvgbhgwkkubokxwdzsvsvnclqczhuoiojyytcxgcegvytzunskgszodwoooqkbhqokcbtnzvraxjjsznbxikjpqxdjdyxaxumsyhvbdrzqibotilbgxtafzheergfibtxrqnbeyatiyuhgshdenkilbwmavoeeqxvmjpvydyqfmnkhuyeivnbpevgskahdisxgtlcetkcwvtxteyqwdlzbvafisjdgvsfiutxmtqasmcateqizsqczsetipncfjzilkuhprqmwtrzljxweckqnoobacszbesczprzbqebcuvlgdtdylfxsxkxalcwscwslkuiluhlroaweofdmekucvzmcicfmpiaskslikckiepaiqdwfaacqsgecntdwtijjhzedijzvjlpmtmbpkvfukdywtwzmxcyguccmkevfpknecanvknyjcvtzitepcexhllmslwelnwcbqvjluigwugthzmbvywdytghmwfhwpsfjxqvqichjnwdwzyiqimpuualvnyxeiyjqhfkhwawocgodvcjqrtylakpnrjucsrqsiueuxxitstuownowbiipwhcfdcqekzbollbreettxzkbzofoerxfnclbqzvdtsdhblxaaioqotqavedvremjebfsyuqcgthrnzcpjqxdpmvuoqqwjbmqvlosgjhfnnzmefhtvwkolxwcthymaeaimjyplacknhihbjswoqgzuhftnxwaoasnbqyptvrhlrokuhqccmjnopkivtyqvfcpprtgkjugrrdqipirfvyerpsjoamnogrvaqljjmndumqtgqihtgxwgbvzldqzqbhhofxpwcdjnqlhmqoskrddxnlgewsgvoxrntyguslxcujcwaaetfrbipprmbqafftlkxzfbgeufajbwmrmarfocnyuiolwlhdmgjgqmugfzcsthoofbwdkktvychghrqpjalqhjfhjjhhrzlfndspxaiifykcculbvwiemgeccqhnqdyypisqwsqrsmpytepzvrqscmoxautkqlrjlwvlbhtyxhzujdhrlkvuqxjvioatpwdnahghphmrhqyifabwjfmiqfdcovnksgdtxpwymynbkwnogoqwcyssejeonmyahkhsfnvtlctaqxzoqbxyshxevp"
        self.run_test(
            big_input,
            None
        )
    
    def test_1(self):
        big_input = big_string
        self.run_test(
            big_input,
            None
        )

    def test_5(self):
        self.run_test(
            "bydizfve",
            "bdevfziy"
        )


try:
    unittest.main()
except SystemExit:
    None





