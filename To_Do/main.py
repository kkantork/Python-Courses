
from aplikacja import Application


if __name__ == '__main__':
    aplikacja = Application()
    while True:
        print('Co chcesz zrobić? [w-wypisz, d-dodaj, z-zrobione, e-exit]:')
        polecenie = input('Napisz "w", "d", "z", "u", lub "e": ')
        if polecenie == 'w':
            aplikacja.wypisz()
        elif polecenie == 'd':
            aplikacja.dodaj()
        elif polecenie == 'z':
            aplikacja.oznacz_jako_zrobione()
        elif polecenie == 'u':
            aplikacja.usun_zadanie()
        elif polecenie == 'e':
            print("Dzięki, kończę działanie!")
            break
        # można też quit()
        else:
            print('Nie rozumiem...')
