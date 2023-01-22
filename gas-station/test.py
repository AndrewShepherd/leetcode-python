import unittest
from gas_station import Solution
import large_input


class TestSolution(unittest.TestCase):

    def test_0(self):
        gas = [5,1,2,3,4]
        cost = [4,4,1,5,1]
        self.assertEqual(4, Solution().canCompleteCircuit(gas, cost))


    def test_3(self):
        gas = large_input.gas
        cost = large_input.cost
        self.assertEqual(-1, Solution().canCompleteCircuit(gas, cost))


    def test_4(self):
        gas = [1,2,3,4,5]
        cost = [3,4,5,1,2]
        self.assertEqual(3, Solution().canCompleteCircuit(gas, cost))

    def test_2(self):
        gas = [2,3,4]
        cost = [3,4,3]
        self.assertEqual(-1, Solution().canCompleteCircuit(gas, cost))

try:
    unittest.main()
except SystemExit:
    None




