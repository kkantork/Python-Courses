from zadanie import Zadanie


class Application:
    def __init__(self):
        self.zadania = [Zadanie('zabierz skarpetki z wersalki'),
                        Zadanie('Umyj po sobie talerz')]

    def wypisz(self):
        for indeks, zadanie in enumerate(self.zadania):
            print(f'{indeks + 1}. ', zadanie.wypisz())

    def dodaj(self):
        nazwa = self.pobierz_nazwe_przypomnienia()
        zadanie = Zadanie(nazwa)
        self.zadania.append(zadanie)
        self.wypisz()

    def pobierz_nazwe_przypomnienia(self):
        jest_ok = False
        while not jest_ok:
            nazwa = input('Powiedz, co masz do zrobienia: ')
            if len(nazwa) > 3:
                jest_ok = True
        return nazwa

    def oznacz_jako_zrobione(self):
        indeks = self.pobierz_indeks()
        self.zadania[indeks - 1].ustaw_jako_zrobione()

    def usun_zadanie(self):
        indeks = self.pobierz_indeks()
        del self.zadania[indeks - 1]

    def pobierz_indeks(self) -> int:
        indeks = int(input('Które zadania dotyczy polecenie? '))
        jest_ok = False
        while not jest_ok:
            if indeks <= len(self.zadania):
                jest_ok = True
        return indeks
