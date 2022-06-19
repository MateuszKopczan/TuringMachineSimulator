Program symuluje działanie Maszyny Turinga w oparciu o:
    - dane z przygotowanych plików txt znajdujących się w katalogu ExerciseData
    - dane wprowadzane przez użytkownika w konsoli

Opis działania programu:
    - program po uruchomieniu wyświetla menu z dostępnymi funkcjami symulatora - są to:
        - wczytanie danych z przygotowanych plików,
        - wczytanie danych od użytkownika w konsoli,
    - głowica maszyny znajduje się zawsze na pierwszym niepustym znaku,
    - symulator może nieoczekiwanie zakończyć pracę, gdy wykryje zapętlenie lub trafi na znak spoza alfabetu,
    - po zakończeniu pracy program zapisuje wszystko do pliku "resultOfSimulationMT.txt"

Informacje dodatkowe:
    - wczytywanie danych przez użytkownika jest zabezpieczone - uniemożliwia wprowadzenie złośliwych danych w celu zakłócenia pracy symulatora
    - program wyświetla menu i rozwiązania dopóki użytkownik nie przerwie jego pracy poprzez wpisanie słowa exit.