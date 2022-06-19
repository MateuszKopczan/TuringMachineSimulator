from datetime import datetime
import time


class TuringMachine:

    def checkInstruction(self, currentState, currentChar):
        for it in self.data.instructions[currentState]:
            if it.currentChar == currentChar:
                return it

    def printPointer(self, number, state, instruction):
        result = ""
        for i in range(number):
            result += " "
        result += "|"
        tmp = "Stan: " + str(state)
        result += tmp.center(10)
        result += str(instruction)
        self.lines.append(result)
        print(result)

    def currentWord(self, word):
        tmp = []
        for it in word:
            tmp.append(it)
        return "".join(tmp)

    def changeChar(self, word, index, newChar):
        tmp = []
        for i in range(len(word)):
            if i == index:
                tmp.append(newChar)
            else:
                tmp.append(word[i])
        return "".join(tmp)

    def printWord(self, word):
        print("___" + word + "___")
        self.lines.append("___" + word + "___" + "\n")

    def saveToFile(self):
        file = open("resultOfSimulationMT.txt", "a")
        now = datetime.now()
        file.write("-------------------------------------------------".center(50))
        file.write("\nData uruchomienia symulatora: " + now.strftime("%d/%m/%Y %H:%M:%S" + "\n\n"))
        file.write("Słowo początkowe: " + self.data.word + "\n")
        for it in self.lines:
            file.write(it + "\n")
        file.write("-------------------------------------------------".center(50))
        file.close()
        print("Wynik działania symulatora został zapisany do pliku resultOfSimulationMT.txt")

    def run(self, data):
        start = time.time()
        self.lines = []
        self.data = data
        self.lines.append(self.data.description + "\n")
        print(self.data.description)
        word = self.currentWord(self.data.word)

        currentState = int(self.data.initialState)
        i = 0
        while True:
            if self.data.word[i] == '_':
                i += 1
            else:
                break
        counter = 0
        while True:
            counter += 1
            if counter > (len(self.data.word) * 1000):
                print("Maszyna prawdopodobnie została zapętlona w instrukcji '" + str(instruction) + "' i niespodziewanie zakończyła swoją pracę.")
                self.lines.append("Maszyna prawdopodobnie została zapętlona i niespodziewanie zakończyła swoją pracę.")
                return

            if i >= len(word) or i < 0:
                instruction = self.checkInstruction(currentState, '_')
            else:
                if word[i] not in self.data.alphabet:
                    print("Maszyna napotkała znak spoza podanego alfabetu i nieoczekiwanie zakończyła swoją pracę.")
                    self.lines.append("Maszyna napotkała znak spoza podanego alfabetu i nieoczekiwanie zakończyła swoją pracę.")
                    return
                instruction = self.checkInstruction(currentState, word[i])
            self.printPointer(i + 3, currentState, instruction)

            self.printWord(word)

            word = self.changeChar(word, i, instruction.newChar)
            if instruction.move == 'l':
                currentState = int(instruction.nextState)
                i -= 1
            elif instruction.move == "s":
                self.printPointer(i + 3, instruction.nextState, instruction)
                self.printWord(word)
                print("Symulator kończy pracę w stanie: " + instruction.nextState)
                self.lines.append("Symulator kończy pracę w stanie: " + instruction.nextState)
                break
            elif instruction.move == "r":
                i += 1
                currentState = int(instruction.nextState)

        diff = time.time() - start
        tmp = "_"
        for it in word:
            if it != "_":
                tmp += it
        tmp += "_"
        print("Koniec działania symulatora.")
        print("Słowo po zakończeniu pracy symulatora: " + tmp)
        print("\nPodsumowanie:")
        print("\tLiczba kroków wykonanych przez symulator: " + str(counter))
        print("\tCzas wykonania programu: " + "{:.4f}".format(diff))

        self.lines.append("Słowo po zakończeniu pracy symulatora: " + tmp)
        self.lines.append("Koniec działania symulatora.")
        self.lines.append("\nPodsumowanie:")
        self.lines.append("\tLiczba kroków wykonanych przez symulator: " + str(counter))
        self.lines.append("\tCzas wykonania programu: " + "{:.4f}".format(diff))
        self.saveToFile()
