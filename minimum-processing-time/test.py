import unittest

from min_processing_time import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        processor_time = [121,99]
        tasks = [287,315,293,260,333,362,69,233]
        result = s.minProcessingTime(processor_time, tasks)
        self.assertEqual(461, result)

try:
    unittest.main()
except SystemExit:
    None









