import ply.lex as lex

class LexerClass:
    def __init__(self):
        self.lexer = lex.lex(module=self)

    tokens = (
            "ID",
            "ASSING",
            "NUMBER",
            "PLUS"
    )

    t_PLUS = r'\+'

    def test(self, data):
        self.lexer.input(data)
        for token in self.lexer:
            print(token)