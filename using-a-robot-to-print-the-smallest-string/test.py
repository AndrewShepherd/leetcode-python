import unittest


from robot_with_string import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, pref, expectedResult):
        sol= Solution()
        result = sol.robotWithString(pref)
        self.assertEqual(result, expectedResult)

    def test_1(self):
        self.run_test(
            "zza",
            "azz"
        )

    def test_2(self):
        self.run_test(
            "bdda",
            "addb"
        )

    def test_3(self):
        self.run_test(
            "bddazza",
            "addbazz"
        )

    def test_4(self):
        self.run_test(
            "zzabdda",
            "addbazz"
        )

    def test_0(self):
        self.run_test(
            "bydizfve",
            "bdevfziy"
        )


try:
    unittest.main()
except SystemExit:
    None





