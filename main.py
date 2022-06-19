from FileReader import FileReader
from TuringMachine import TuringMachine

turingMachine = TuringMachine()

print("Symulator Maszyny Turinga".center(50))
print("Wprowadź 0, jeśli chcesz wprowadzić dane do symulatora samodzielnie")
print("1. Negacja liczby w systemie binarnym")
print("2. Dodawanie liczb w systemie unarnym")
print("3. Następnik liczby w systemie binarnym")
print("4. Sprawdzenie czy długość słowa jest podzielna przez 3")
print("5. Sprawdzenie czy podane słowo jest palindromem")
print("6. Sprawdzenie czy liczba jest postaci 0w1w, gdzie w należy do (0 U 1)*")
print("7. Sprawdzenie czy liczba jest postaci w01w, gdzie w należy do (0 U 1)*")
print("8. Sprawdzenie czy słowo składa sie z 0 i 1 zapisanych naprzemiennie")
print("9. Sprawdzenie czy liczba binarna składa sie z takiej samej liczby 0 i 1")
print("10. Sprawdzenie czy słowo należy do języka O^n1^n , n>0")
print("11. Sprawdzenie czy słowo należy do języka: b^n a(cb)^k , n > 0, k >= 0")
print("Wpisz exit, aby zakończyć działanie symulatora")


while True:
    exercise = input("Wprowadź numer zadania, którego symulacje chcesz zobaczyć: ")

    if 1 <= int(exercise) < 12:
        filename = "ExerciseData/DaneMT_" + exercise + ".txt"
        inputData = FileReader(filename, True)
        turingMachine.run(inputData)
    elif int(exercise) == 0:
        inputData = FileReader("", False)
        if inputData.correctInput:
            print(inputData.correctInput)
            turingMachine.run(inputData)
    elif exercise == "exit":
        break
    else:
        print("Wprowadzono niewłaściwy numer zadania. Sprobuj ponownie.")

print("Działania symulatora Maszyny Turinga zostało zakończone")
