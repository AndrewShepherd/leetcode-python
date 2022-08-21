import unittest

from tree_node import TreeNode

from amount_of_time_for_binary_tree_to_be_infected import Solution

class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        root = TreeNode(
            1,
            TreeNode(
                5,
                None,
                TreeNode(
                    4,
                    TreeNode(9),
                    TreeNode(2)
                )
            ),
            TreeNode(
                3,
                TreeNode(10),
                TreeNode(6)
            )
        )
        result = s.amountOfTime(root, 3)
        self.assertEqual(4, result)

try:
    unittest.main()
except SystemExit:
    None
