def dodaj(a, nowe_zadanie):
    """Dodaje nowy element do listy"""

    a.append(nowe_zadanie)


def usun(lista, elem):
    """Usuwa z listy element o podanym indexie"""

    lista.pop(elem)


def done(lista):
    str_pom=''
    n = int(input('Podaj wykonane zadanie'))
    print('nie skonczone')


def drukuj():
    """Drukuje naglowek i zawartosc pliku ToDo.txt"""

    print('-- LISTA ZADAŃ DO ZROBIENIA --')
    with open('ToDo.txt') as plik :
        print(plik.read())


def odczyt():
    """Wczytuje i formatuje zawartosc pliku ToDo.txt do listy i zwraca ta liste"""

    file_cont = []
    str_pom = ''
    with open('ToDo.txt') as plik :
        file_cont = plik.readlines()
    for i in range(len(file_cont)):
        str_pom = file_cont[i]
        str_pom = str_pom[4:-1]
        file_cont[i] = str_pom
    return file_cont


def zapis(temp_list):
    """Formatuje zawartosc listy i zapisuje do pliku ToDo.txt"""

    with open('ToDo.txt','w') as plik :
        for p in range(len(temp_list)):
            linijka = '{} - {}\n'.format(p,temp_list[p])
            plik.write(linijka)


def slownik(polecenie):
    """Odczytuje z klawiatury wpisane polecenie i je wykonuje jesli jest w slowniku"""

    if polecenie in ['dodaj','DODAJ','add','ADD']:
        nowe_zadanie = input('Wpisz nowe zadanie: \n')
        dodaj(lista, nowe_zadanie)
        zapis(lista)
    if polecenie in ['usun','USUN','del','DEL']:
        elem = int(input('Podaj element do usuniecia: \n'))
        usun(lista, elem)
        zapis(lista)
    if polecenie in ['done']:
        done(lista)
    return

"""------------------"""
lista = odczyt()
polecenie = ''
while polecenie not in ['EXIT','exit']:
    slownik(polecenie)
    drukuj()
    polecenie = input('dodaj, usun, EXIT: ')
