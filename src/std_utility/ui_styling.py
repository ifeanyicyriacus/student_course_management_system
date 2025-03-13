class StringFormatting:
    def __init__(self, text: str):
        self._texts:[str] = [text]
        self._index:int = 0

    def bold(self):
        self._texts[self._index] = "\033[1m" + self._texts[self._index] + "\033[0m"
        return self

    def italic(self):
        self._texts[self._index] = "\033[3m" + self._texts[self._index] + "\033[0m"
        return self

    def underline(self):
        self._texts[self._index] = "\033[4m" + self._texts[self._index] + "\033[0m"
        return self

    def strikethrough(self):
        self._texts[self._index] = "\033[9m" + self._texts[self._index] + "\033[0m"
        return self

    def red(self):
        self._texts[self._index] = "\033[31m" + self._texts[self._index] + "\033[0m"
        return self

    def green(self):
        self._texts[self._index] = "\033[32m" + self._texts[self._index] + "\033[0m"
        return self

    def blue(self):
        self._texts[self._index] = "\033[34m" + self._texts[self._index] + "\033[0m"
        return self

    def yellow(self):
        self._texts[self._index] = "\033[33m" + self._texts[self._index] + "\033[0m"
        return self

    def cyan(self):
        self._texts[self._index] = "\033[36m" + self._texts[self._index] + "\033[0m"
        return self

    def magenta(self):
        self._texts[self._index] = "\033[35m" + self._texts[self._index] + "\033[0m"
        return self

    def white(self):
        self._texts[self._index] = "\033[37m" + self._texts[self._index] + "\033[0m"
        return self

    def bg_red(self):
        self._texts[self._index] = "\033[41m" + self._texts[self._index] + "\033[0m"
        return self

    def bg_green(self):
        self._texts[self._index] = "\033[42m" + self._texts[self._index] + "\033[0m"
        return self

    def bg_yellow(self):
        self._texts[self._index] = "\033[43m" + self._texts[self._index] + "\033[0m"
        return self

    def bg_blue(self):
        self._texts[self._index] = "\033[44m" + self._texts[self._index] + "\033[0m"
        return self

    def bg_magenta(self):
        self._texts[self._index] = "\033[45m" + self._texts[self._index] + "\033[0m"
        return self

    def bg_cyan(self):
        self._texts[self._index] = "\033[46m" + self._texts[self._index] + "\033[0m"
        return self

    def bg_white(self):
        self._texts[self._index] = "\033[47m" + self._texts[self._index] + "\033[0m"
        return self

    def br(self):
        self._texts[self._index] = self._texts[self._index] + "\n"
        return self

    def print(self):
        print(self.__str__())

    def __str__(self):
        result:str = ""
        for text in self._texts:
            result += text
        return result

    def append(self, text: str):
        self._texts.append(text)
        self._index += 1
        return self

class CursorMovement:
    def __init__(self):
        self._cursor = ""

    def move_cursor_up(self):
        self._cursor += "\033[A"
        return self

    def move_cursor_down(self):
        self._cursor += "\033[B"
        return self

    def move_cursor_right(self):
        self._cursor += "\033[C"
        return self

    def move_cursor_left(self):
        self._cursor += "\033[D"
        return self

    def __str__(self):
        return self._cursor
