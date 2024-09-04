class FSM:
    def __init__(self):
        self.state = 'START'

    def transition(self, char):
        if self.state == 'START':
            if char in 'sxz' or char.endswith(('sh', 'ch')):
                self.state = 'ADD_ES'
            else:
                self.state = 'ADD_S'
        elif self.state == 'ADD_ES':
            self.state = 'END'
        elif self.state == 'ADD_S':
            self.state = 'END'

    def pluralize(self, noun):
        for char in noun:
            self.transition(char)
        if self.state == 'ADD_ES':
            return noun + 'es'
        elif self.state == 'ADD_S':
            return noun + 's'
        else:
            return noun

fsm = FSM()
nouns = ['cat', 'dog', 'box', 'bush', 'church']
plurals = [fsm.pluralize(noun) for noun in nouns]

print("Nouns:", nouns)
print("Plurals:", plurals)
