# zadanie 1

liczby = []

while True:
    text = input(f"podaj liczbe calkowita lub stop: ")
    if text.lower()== "stop":
        break
    try:
        liczba = int(text)
        liczby.append(liczba)
    except ValueError:
        print(f"error {text} nie jest calkowita liczba ")

# zadanie 2
def average(lista_liczb: list) -> float:
    if not lista_liczb:
        return 0.0
    suma= sum(lista_liczb)
    return suma/ len(lista_liczb)

# zadanie 3
def parzyste(lista_liczb: list) -> float:
    l_parzyste= []
    for liczba in lista_liczb:
        if liczba%2 == 0:
            l_parzyste.append(liczba)
    return l_parzyste


print("wczytane liczby: ", liczby)
srednia = average(liczby)
print(f"srednia arytmetyczna wynosi: {srednia}")
lista_parzyste= parzyste(liczby)
print(f"wybrane liczby parzyste to: {lista_parzyste}")