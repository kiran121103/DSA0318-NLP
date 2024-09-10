class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        return self.expression()

    def expression(self):
        node = self.term()
        while self.current_token() == '+':
            self.consume('+')
            node = ('+', node, self.term())
        return node

    def term(self):
        node = self.factor()
        while self.current_token() == '*':
            self.consume('*')
            node = ('*', node, self.factor())
        return node

    def factor(self):
        if self.current_token() == '(':
            self.consume('(')
            node = self.expression()
            self.consume(')')
            return node
        else:
            return self.number()

    def number(self):
        token = self.current_token()
        self.consume(token)
        return ('number', token)

    def current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        else:
            return None

    def consume(self, token):
        if self.current_token() == token:
            self.pos += 1
        else:
            raise Exception(f"Expected {token}, got {self.current_token()}")
tokens = ['2', '*', '(', '3', '+', '4', ')']
parser = Parser(tokens)
parse_tree = parser.parse()
print(parse_tree)
