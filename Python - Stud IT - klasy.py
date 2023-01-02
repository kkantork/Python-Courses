# just a test comment
from math import ceil
from copy import copy

class Adres:
    def __init__(self, ulica, numer, miasto):
        self.ulica = ulica
        self.numer = numer
        self.miasto = miasto

    def wyswietl_informacje(self):
        return f'Znajduje się w mieście: {self.miasto}, przy ulicy {self.ulica}, pod numerem {self.numer}'

class Student:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nazwa = imie + " " + nazwisko
        self.semestr = 1
        self.adres = None
    
    def ustaw_adres(self, adres: Adres):
        self.adres = adres


    def promuj(self, ilosc_semestrow=1):
        self.semestr += ilosc_semestrow

    @property
    def rok(self):
        return ceil(self.semestr / 2)
    
    def przedstaw_sie(self):
        return f'Nazywam się {self.imie} {self.nazwisko}'

#dataclasses



akademik = Adres(ulica = "Akademicka", numer = 13, miasto = "Jastrowie")


# przypisanie obiektu do zmiennej nie sprawia, że pracujemy na nowym obiekcie. Nadal operujemy na originalnej instancji. Aby stworzyć nowy, musimy go sklonować
jan = Student('Jan', 'Kowalski')
#jacek = jan
#jacek.imie = 'Jacek'

# klonowanie obiektu:
jacek = copy(jan)

print(jacek.nazwa, jacek.imie)
jacek.imie = 'Jacek'
print(jacek.przedstaw_sie())
print(jan.przedstaw_sie())
jacek.ustaw_adres(akademik)
jan.ustaw_adres(akademik)
print(jacek.adres.wyswietl_informacje())
print(jan.adres.wyswietl_informacje())

print(jacek)
print(jan)

# jan = Student('Jan', 'Kowalski')
# jan.promuj()
# jan.promuj()
# print(jan)
# print(jan.imie)
# print(jan.nazwa, jan.semestr)

# anna = Student('Anna', 'Jakaś')
# anna.promuj(10)
# print(anna)
# print(anna.imie, anna.semestr)
# print(anna.rok)

#kiedy chcemy requirements stworzyć:
#pip freeze > requirements.txt