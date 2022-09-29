class Student:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nazwa = imie + " " + nazwisko
        self.semestr = 1
    def promuj(self, ilosc_semestrow=1):
        self.semestr += ilosc_semestrow


jan = Student('Jan', 'Kowalski')
jan.promuj()
jan.promuj()
print(jan)
print(jan.imie)
print(jan.nazwa, jan.semestr)

anna = Student('Anna', 'Jakaś')
anna.promuj(10)
print(anna)
print(anna.imie, anna.semestr)
