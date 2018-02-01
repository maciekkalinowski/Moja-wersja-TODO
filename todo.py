def dodaj(a):
    nowe_zadanie = input('Wpisz nowe zadanie: \n')
    a.append(nowe_zadanie)


def usun(lista):
    lista.pop(int(input('Podaj zadanie do usuniecia: \n')))


def done(lista):
    str_pom=''
    n = int(input('Podaj wykonane zadanie'))
    print('nie skonczone')


def drukuj():
    print('-- LISTA ZADAŃ DO ZROBIENIA --')
    with open('ToDo.txt') as plik :
        print(plik.read())
    
        
def odczyt():
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
    with open('ToDo.txt','w') as plik :
        for p in range(len(temp_list)):
            linijka = '{} - {}\n'.format(p,temp_list[p])
            plik.write(linijka)


def slownik(polecenie):
    if polecenie in ['dodaj','DODAJ','add','ADD']:
        dodaj(lista)
        zapis(lista)
    if polecenie in ['usun','USUN','del','DEL']:
        usun(lista)
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


