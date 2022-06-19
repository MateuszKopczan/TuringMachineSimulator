class Instruction:

    def __init__(self, currentChar, nextState, newChar, move):
        self.currentChar = currentChar
        self.nextState = nextState
        self.newChar = newChar
        self.move = move

    def __str__(self):
        if self.move == 'r':
            tmp = "->"
        elif self.move == 'l':
            tmp = "<-"
        else:
            tmp = "-"
        text = "Obecny znak: " + str(self.currentChar) + " Następny stan: " + str(self.nextState) + " Nowy znak: " + str(self.newChar) + " Kierunek ruchu: " + tmp
        return text
