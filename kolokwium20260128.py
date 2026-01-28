#zadanie 1
def NWD (a,b):
    while b != 0:
        c = a%b
        a = b
        b = c
    return a
a = 282
b = 78
print(NWD(a,b))

#zadanie 3 
#dodawanie liczby naturalnej
number = input('Podaj liczbe naturalna:')
sum = 0
for cyfra in number:
    cyfra = int(cyfra)
    sum = sum + cyfra
print(f"Suma cyfr w liczbie {number} wynosi {sum}")
                 

#zadanie 5
# silnia funkcja
def silnia(n):
  if n == 0:
    return 1
  else:
    return n * silnia(n-1)
liczba= int(input("Podaj liczbe: "))
print(silnia(liczba))

#zadanie 7
class Punkt:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def przesun(self, dx, dy):
    self.x += dx
    self.y += dy

  def odleglosc(self, inny):
        roznica_x = abs(self.x - inny.x)
        roznica_y = abs(self.y - inny.y)
        return max(roznica_x, roznica_y)


p1 = Punkt(1, 2)
p2 = Punkt(4, 6)

wynik = p1.odleglosc(p2)

print(f"Punkt 1: ({p1.x}, {p1.y})")
print(f"Punkt 2: ({p2.x}, {p2.y})")
print(f"Odleglosc Chebysheva: {wynik:.4f}")


 #zadanie 10
class UrzadzenieSieciowe:
    def __init__(self, ping: int, dane: str):
        self.ping = ping
        self.dane = dane

    @property
    def ping(self):
        return self._ping

    @ping.setter
    def ping(self, value):
        if not isinstance(value, int) or value < 0:
            raise AttributeError("Ping musi być liczba naturalna (całkowita dodatnia)")
        self._ping = value

    @property
    def dane(self):
        return self._dane

    @dane.setter
    def dane(self, value):
        if not isinstance(value, str) or not (10 <= len(value) <= 50):
            raise AttributeError("Dane musza byc tekstem o dlugosci od 10 do 50 znakow")
        self._dane = value

    def polacz(self):
        # klasa potomna
        raise NotImplementedError("Klasa potomna musi implementowac metode polacz()")


class NAS(UrzadzenieSieciowe):
    def __init__(self, ping: int, dane: str):
        super().__init__(ping, dane)

    def polacz(self, dane: str = None):
        if dane is None:
            return self.dane
        else:
            self.dane = dane
            return self.dane


class Drukarka(UrzadzenieSieciowe):
    def __init__(self, ping: int):
        #potrrzebny tylko ping
        super().__init__(ping, "Domyslne dane do wydruku")

    def polacz(self, dane: str):
        print("Drukowanie")
        print(f"{dane}")
        print("Koniec wydruku")


class Komputer(UrzadzenieSieciowe):
    def __init__(self, ping: int, dane: str):
        super().__init__(ping, dane)

    def polacz(self, inny_device: UrzadzenieSieciowe):
        # condition for ping
        if (self.ping + inny_device.ping) < 120:
            if isinstance(inny_device, Komputer):
                stare_moje = self.dane
                self.dane = inny_device.dane
                inny_device.dane = stare_moje
            else:
                return inny_device.polacz(self.dane)
        else:
            print("Nie mozna nawiazac polaczenia")

#sprawdzanie jako oddzielna komorka
pc1 = Komputer(30, "Dane Komputera pierwszego")
pc2 = Komputer(30, "Dane Komputera Drugiego")

pc1.polacz(pc2)

print(pc1.dane) 
print(pc2.dane) 