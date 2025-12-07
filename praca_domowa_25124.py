# zadanie 4

liczba1 = float(input('Podaj pierwszą liczbę: '))
liczba2 = float(input('Podaj drugą liczbę: '))
print('Wybierz operację porównania:')
print('1. Większa niż')
print('2. Mniejsza niż')
print('3. Równa się')
print('4. Nie równa się')

wybor = input('Podaj numer operacji (lub wpisz "exit" aby zakończyć): ')

if wybor == 'exit':
    pass 
elif wybor == '1':
    wynik = liczba1 > liczba2
    print(f"Wynik porównania: {wynik}")
elif wybor == '2':
    wynik = liczba1 < liczba2
    print(f"Wynik porównania: {wynik}")
elif wybor == '3':
    wynik = liczba1 == liczba2
    print(f"Wynik porównania: {wynik}")
elif wybor == '4':
    wynik = liczba1 != liczba2
    print(f"Wynik porównania: {wynik}")
else:
    print('Nieprawidłowy wybór. Spróbuj ponownie.')
    print('Wynik porównania: {}'.format("Brak"))
    
