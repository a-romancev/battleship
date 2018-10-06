class ColoredText:
    Red = '\033[91m'
    Green = '\033[92m'
    Yellow = '\033[93m'
    Blue = '\033[94m'
    Magenta = '\033[95m'
    Cyan = '\033[96m'
    White = '\033[97m'
    Grey = '\033[90m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

    def __init__(self):
        self.text = ""

    def __str__(self):
        return self.text

    def default(self, t):
        self.text += t
        return self

    def red(self, t):
        self.text += self.Red + t + self.END
        return self

    def green(self, t):
        self.text += self.Green + t + self.END
        return self

    def yellow(self, t):
        self.text += self.Yellow + t + self.END
        return self

    def blue(self, t):
        self.text += self.Blue + t + self.END
        return self

    def magenta(self, t):
        self.text += self.Magenta + t + self.END
        return self

    def grey(self, t):
        self.text += self.Grey + t + self.END
        return self
