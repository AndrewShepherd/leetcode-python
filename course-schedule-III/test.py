from course_schedule_III import Solution
from large_test_case import large_input_1, large_input_2, large_input_3
from other_solution import scheduleCourse
import unittest

class TestSolution(unittest.TestCase):




    def test_5(self):
        s = Solution()
        result = s.scheduleCourse(large_input_2)
        self.assertEqual(result, 208)


    def test_0(self):
        s = Solution()
        result = s.scheduleCourse(large_input_3)
        self.assertEqual(result, 3999)

    def test_4(self):
        s = Solution()
        result = s.scheduleCourse(large_input_1)
        self.assertEqual(result, 9931) # I don't know what it is

    def test_1(self):
        s = Solution()
        result = s.scheduleCourse([[100,200],[200,1300],[1000,1250],[2000,3200]])
        self.assertEqual(3, result)
        otherResult = scheduleCourse([[100,200],[200,1300],[1000,1250],[2000,3200]])
        self.assertEqual(otherResult, 3)

    def test_long_then_short(self):
        courses = [(2, 1), (3, 10)]
        otherResult = scheduleCourse(courses)
        self.assertEqual(otherResult, 1)


    def test_2(self):
        s = Solution()
        result = s.scheduleCourse([[1,2]])
        self.assertEqual(1, result)

    def test_3(self):
        s = Solution()
        result = s.scheduleCourse([[3,2],[4,3]])
        self.assertEqual(0, result)

try:
    unittest.main()
except SystemExit:
    None