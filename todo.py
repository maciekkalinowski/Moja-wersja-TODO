

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
    """Drukuje naglowek i sformatowaną zawartosc pliku ToDo2.txt """

    print('-- LISTA ZADAŃ DO ZROBIENIA --')
    i=0
    with open('ToDo2.txt') as plik :
        for linijka in plik:
            linijka = '{} ----- {}'.format(i,linijka)
            i += 1
            print(linijka, end='')



def odczyt():
    """Wczytuje zawartosc pliku ToDo2.txt do listy i zwraca ta liste"""

    file_cont = []
    str_pom = ''
    with open('ToDo2.txt') as plik :
        file_cont = plik.readlines()
    return file_cont



def zapis(temp_list):
    """Zapisuje zawartosc listy do pliku ToDo2.txt"""

    with open('ToDo2.txt','w') as plik :
        for p in range(len(temp_list)):
            #linijka = temp_list[p]
            plik.write(temp_list[p])





def slownik(polecenie):
    """Odczytuje z klawiatury wpisane polecenie i je wykonuje jesli jest w slowniku"""

    if polecenie in ['dodaj','DODAJ','add','ADD']:
        nowe_zadanie = input('Wpisz nowe zadanie: \n') +'\n'
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
