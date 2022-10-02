import unittest

from palindrome_pairs import Solution, makeCompressedWord, getPrefixBeforePalindromes, getSufixAfterPalindromes
import large_testcase
import large_testcase2

class TestSolution(unittest.TestCase):

    def run_test(self, input, expectedResult):
        sol= Solution()
        result = sol.palindromePairs(input)
        self.assertEqual(sorted(result), sorted(expectedResult))

    def test_6(self):
        sol= Solution()
        result = sol.palindromePairs(large_testcase.large_dataset)

    def test_5(self):
        self.run_test(
            ["a", "aba"],
            []
        )

    def test_7(self):
        self.run_test(
            ["a","abc","aba",""],
            [[0,3],[3,0],[2,3],[3,2]]
        )

    def test_9(self):
        aaba = makeCompressedWord("abaa")
        # This revealed a flaw in the algorithm. It would see the 'aa' in the middle as one item
        abaabaa = makeCompressedWord("abaabaa")
        suffixes = list(getSufixAfterPalindromes(abaabaa))
        self.assertTrue(
            aaba in suffixes
        )
        self.run_test(
            ["bb","bababab","baab","abaabaa","aaba","","bbaa","aba","baa","b"],
            [[0,5],[0,9],[9,0],[5,0],[1,5],[5,1],[2,5],[8,2],[5,2],[4,3],[7,4],[4,8],[6,0],[7,5],[5,7],[8,9],[9,5],[5,9]]
        )

    def test_8(self):
        sssll = makeCompressedWord("sssll")
        ss = makeCompressedWord("sll")
        suffixes = list(getSufixAfterPalindromes(sssll))
        self.assertTrue(ss in suffixes)
        

        self.run_test(
            ["lls","sssll"],
            [[0,1]]
        )

    def test_11(self):
        self.run_test(
            ["","abcbbba"],
            []
        )

    def test_0(self):
        smaller = [large_testcase2.input[0], large_testcase2.input[48]]
        self.run_test(
            smaller,
            [[0, 1]]
        )

        self.run_test(
            large_testcase2.input,
            [[0,48],[1,48],[8,1],[2,48],[30,2],[2,5],[38,4],[5,42],[43,5],[5,30],[6,9],[43,6],[44,7],[30,8],[8,14],[48,8],[8,95],[95,9],[30,9],[48,9],[48,12],[14,42],[42,14],[15,24],[5,15],[18,59],[14,18],[19,42],[19,14],[14,19],[42,19],[22,43],[42,24],[30,48],[42,30],[30,51],[31,55],[32,8],[32,11],[42,32],[32,44],[35,42],[35,30],[37,35],[38,51],[38,2],[38,93],[39,48],[65,39],[40,42],[51,40],[40,95],[40,65],[41,59],[5,41],[43,48],[48,43],[44,42],[11,44],[95,44],[44,32],[45,2],[65,45],[48,49],[51,42],[48,51],[51,30],[67,52],[55,48],[43,55],[55,43],[48,55],[57,48],[57,43],[55,57],[57,55],[43,57],[48,57],[17,58],[59,48],[42,59],[98,62],[8,65],[65,30],[42,65],[65,40],[66,55],[96,66],[67,40],[67,32],[51,67],[78,48],[65,86],[30,88],[89,42],[5,91],[93,55],[30,93],[93,35],[95,48],[14,95],[95,51],[95,8],[96,48],[40,96],[97,42],[57,97],[97,30],[8,98],[98,2]]
        )

    def test_12(self):
        input = ["baaabab","aaaaba","babbb","b","babaaab","baabaa","ba","ababa","abbaaa","aababaaa","aabba","ababaaab","babab","bb","aa","aaaaabba","abba","babbbaa","baaba","aaabb"]
        self.run_test(
            [input[18], input[6]],
            []
        )

        self.run_test(
            [input[19], input[8]],
            [[0, 1]]
        )
        self.run_test(
            input,
            [[6,0],[0,4],[13,2],[4,0],[5,3],[14,5],[6,3],[7,6],[19,8],[8,16],[14,8],[8,10],[16,10],[0,11],[6,12],[13,3],[3,13],[8,15],[16,15],[13,19]]
        )

    def test_12(self):
        input = ["","adijdce","i","egjgc","jcjcj","f","hfcbdah","bhb","afie","fegc","fcbeg","fihbaga","ehgffg","gjih","ejdejg","gj","a","fbh","hg","addi"]
        self.run_test(
            [input[14], input[15]],
            []
        )

        self.run_test(
            ["","adijdce","i","egjgc","jcjcj","f","hfcbdah","bhb","afie","fegc","fcbeg","fihbaga","ehgffg","gjih","ejdejg","gj","a","fbh","hg","addi"],
            [[2,0],[0,2],[4,0],[0,4],[5,0],[0,5],[7,0],[0,7],[16,0],[0,16]]
        )

    def test_10(self):
        self.run_test(
            ["abcd","dcba","lls","s","sssll"],
            [[0,1],[1,0],[3,2],[2,4]]
        )

    def test_2(self):
        self.run_test(
            ["bat","tab","cat"],
            [[0,1],[1,0]],
        )

    def test_3(self):
        self.run_test(
            ["a",""],
            [[0,1],[1,0]],
        )

    def test_4(self):
        self.run_test(
            ["a","b","c","ab","ac","aa"],
            [[3,0],[1,3],[4,0],[2,4],[5,0],[0,5]]
        )

try:
    unittest.main()
except SystemExit:
    None

