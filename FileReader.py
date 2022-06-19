from Instruction import Instruction


class FileReader:

    def __init__(self, path, flag):
        if flag:
            self.path = path
            file = open(self.path)
            data = file.read().split('\n')
            file.close()
            self.readDescription(data[0])
            self.readStates(data[1])
            self.readAlphabet(data[2])
            self.readWordLength(data[3])
            self.readWord(data[4])
            self.readFinalState(data[5])
            self.readInitialState(data[6])
            self.readInstructions(data[8:])
        else:
            self.correctInput = True
            self.manualInput()

    def readDescription(self, data):
        self.description = data[7:-1]

    def readStates(self, data):
        self.states = data[7:].split(',')

    def readAlphabet(self, data):
        self.alphabet = data[9:].split(',')

    def readWordLength(self, data):
        self.wordLength = int(data[15:])

    def readWord(self, data):
        self.word = data[7:]

    def readFinalState(self, data):
        self.finalState = []
        for it in data[14:].split(","):
            self.finalState.append(it)

        self.numberOfStates = 0
        for it in self.states:
            if it not in self.finalState:
                self.numberOfStates += 1

    def readInitialState(self, data):
        self.initialState = data[17:]

    def readInstructions(self, data):
        self.instructions = [[] for i in range(self.numberOfStates)]
        stateCounter = -1
        for it in data:
            if len(it) < 8:
                stateCounter += 1
            else:
                it = it.strip()
                tmp = it.split(";")
                tmp1 = tmp[1].split(",")
                self.instructions[stateCounter].append(Instruction(tmp[0], tmp1[0], tmp1[1], tmp1[2]))

    def manualInput(self):
        self.description = input("Wprowadź opis zadania symulatora: ")

        while True:
            self.states = input("Wprowadź stany symulatora oddzielone przecinkiem np.: 0,1,2,a,n: ").split(",")
            if len(self.states) == 1 and self.states[0] == '':
                self.correctInput = False
                print("Wprowadzono niewłaściwe stany. Spróbuj ponownie.")
            else:
                break

        while True:
            self.alphabet = input("Wprowadź wszystkie znaki alfabetu oddzielone przecinkiem np.: 0,1,_: ").split(",")
            if len(self.alphabet) == 1 and self.alphabet[0] == '':
                self.correctInput = False
                print("Alfabet musi składać się z przynajmniej jednego znaku. Spróbuj ponownie.")
            else:
                break

        while True:
            try:
                self.wordLength = int(input("Wprowadź długość słowa: "))
            except ValueError:
                print("Długość słowa musi być liczbą całkowitą. Spróbuj ponownie.")
                self.correctInput = False
                continue
            self.word = input("Wprowadź słowo: ")
            if len(self.word) != self.wordLength:
                print("Wprowadzona długość słowa różni się od rzeczywistej długości. Spróbuj ponownie.")
                self.correctInput = False
            else:
                break

        while True:
            self.finalState = input("Wprowadź stany końcowe oddzielone przecinkiem np.: a,n: ").split(",")
            print(self.finalState)
            flag = True
            if len(self.finalState) == 0:
                print("Maszyna musi otrzymać przynajmniej jeden stan końcowy. Spróbuj ponownie.")
                self.correctInput = False
                flag = False
            for it in self.finalState:
                if it not in self.states:
                    print("Wprowadzony stan końcowy nie należy do stanów maszyny. Spróbuj ponownie.")
                    self.correctInput = False
                    flag = False
            if flag:
                break

        self.numberOfStates = 0
        for it in self.states:
            if it not in self.finalState:
                self.numberOfStates += 1
        if self.numberOfStates == 0:
            print("Nieoczekiwany błąd liczby stanów maszyny. Spróbuj ponownie.")
            self.correctInput = False
            return

        while True:
            self.initialState = input("Wprowadź stan początkowy działania maszyny: ")
            if len(self.initialState) == 0:
                print("Nie wprowadzono stanu początkowego. Spróbuj ponownie.")
                self.correctInput = False
            elif self.initialState not in self.states:
                print("Wprowadzony stan początkowy nie należy do stanów maszyny. Spróbuj ponownie.")
                self.correctInput = False
            else:
                break

        self.instructions = [[] for i in range(self.numberOfStates)]
        for it in self.states:
            if it not in self.finalState:
                print("Instrukcje wprowadzane są w formacie: napotkany znak;kolejny stan,nowy znak,kierunek; np.: 0;1,0,r;")
                print("Możliwe kierunki ruchu: r, l, s")
                print("Wprowadź instrukcję dla stanu " + it)
                for i in range(len(self.alphabet)):
                    while True:
                        instruction = input("Instrukcja " + str(i) + " dla stanu " + it + ":")
                        if not instruction.endswith(";"):
                            print("Błędna instrukcja. Spróbuj ponownie.")
                            continue
                        tmp = instruction.split(";")
                        tmp1 = tmp[1].split(",")
                        moves = ["l", "s", "r"]
                        if len(tmp[0]) == 0 or len(tmp1[0]) == 0 or len(tmp1[1]) == 0 or len(tmp1[2]) == 0:
                            print("Błędna instrukcja. Spróbuj ponownie.")
                            self.correctInput = False
                        elif tmp[0] not in self.alphabet or tmp1[1] not in self.alphabet:
                            print("Błędna instrukcja - wprowadzono znak spoza alfabetu. Spróbuj ponownie.")
                        elif tmp1[0] not in self.states:
                            print("Błędna instrukcja - wprowadzona niewłaściwy stan. Spróbuj ponownie.")
                        elif tmp1[2] not in moves:
                            print("Błędna instrukcja - wprowadzono niewłaściwy kierunek ruchu głowicy. Spróbuj ponownie.")
                        else:
                            self.instructions[int(it)].append(Instruction(tmp[0], tmp1[0], tmp1[1], tmp1[2]))
                            break
