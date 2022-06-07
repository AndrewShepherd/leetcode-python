class TextEditor:

    def __init__(self):
        self.cursor_pos = 0
        self.text = ""

    def addText(self, text: str) -> None:
        ## inserts (not overwrites)
        self.text = self.text[:self.cursor_pos] + text + self.text[self.cursor_pos:]
        self.cursor_pos += len(text)

    def deleteText(self, k: int) -> int:
        result = min(self.cursor_pos, k)
        new_cursor_pos = max(self.cursor_pos - k, 0)
        self.text = self.text[:new_cursor_pos] + self.text[self.cursor_pos:]
        self.cursor_pos = new_cursor_pos
        return result


    def cursorLeft(self, k: int) -> str:
        self.cursor_pos = max(self.cursor_pos-k, 0)
        return self.text[max(0, self.cursor_pos-10):self.cursor_pos]

    def cursorRight(self, k: int) -> str:
        self.cursor_pos = min(self.cursor_pos+k, len(self.text))
        return self.text[max(0, self.cursor_pos-10):self.cursor_pos]


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)