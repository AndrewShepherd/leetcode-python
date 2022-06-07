import unittest

from text_editor import TextEditor

class TestSolution(unittest.TestCase):

    def test_1(self):
        textEditor = TextEditor()
        textEditor.addText("leetcode");
        self.assertEqual(
            textEditor.deleteText(4),
            4
        )
        textEditor.addText("practice")
        self.assertEqual(
            textEditor.cursorRight(3),
            "etpractice"
        )
        self.assertEqual(
            textEditor.cursorLeft(8),
            "leet"
        )
        self.assertEqual(
            textEditor.deleteText(10),
            4
        )
        self.assertEqual(
            textEditor.cursorLeft(2),
            ""
        )
        self.assertEqual(
            textEditor.cursorRight(6),
            "practi"
        )

    def test_2(self):
        textEditor = TextEditor()
        textEditor.addText("bxyackuncqzcqo");
        self.assertEqual(
            textEditor.cursorLeft(12),
            "bx"
        )
        self.assertEqual(
            textEditor.deleteText(3),
            2
        )
        self.assertEqual(
            textEditor.cursorLeft(5),
            ""
        )
        textEditor.addText("osdhyvqxf")
        self.assertEqual(
            textEditor.cursorRight(10),
            "yackuncqzc"
        )

try:
    unittest.main()
except SystemExit:
    None
