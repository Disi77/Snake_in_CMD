from random import randrange
from os import system, name


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def nakresli_mapu(velikost, had, ovoce):
    '''
    Funkce nakreslí pole dané velikosti, kde:
        --> na souřadnicích hada zakreslí "x"
        --> na souřadnicích hlavy hada zakreslí "o"
        --> na souřadnicích ovoce zakreslí '♫'
        --> na ostatních souřadnicích zakreslí "."
    '''
    for x in range(velikost[0]):
        for y in range(velikost[1]):
            if x == had[-1][0] and y == had[-1][1]:
                print('o', end=' ')
            elif (x, y) in had:
                print('x', end=' ')
            elif (x, y) in ovoce:
                print('♫', end=' ')
            else:
                print('.', end=' ')
        print()


def pohyb(velikost, had, smer, ovoce):
    '''
    Funkce pohyb vloží do seznamu souradnic další bod.
    Funkce také zkontroluje, zda směr, který uživatel vložil, je možný:
      --> Had nesmí vyjet ven z pole ("x")
      --> Had nesmí kousat sám sebe ("ham")
    '''
    x = had[-1][0]
    y = had[-1][1]

    if smer == 'd' and y == (velikost[1]-1):
        return
    elif smer == 'a' and y == 0:
        return
    elif smer == 'w' and x == 0:
        return
    elif smer == 's' and x == (velikost[0]-1):
        return
    if smer == 'd':
        y += 1
    elif smer == 'a':
        y += -1
    elif smer == 'w':
        x += -1
    elif smer == 's':
        x += 1
    if (x, y) in had:
        print('   !!!   Auvajs, to bolí kanibale.   !!!   ')
        return
    else:
        had.append((x, y))
    if (x, y) in ovoce:
        del ovoce[ovoce.index((x, y))]
    else:
        del had[0]


def ovoce_pole(ovoce, had, tah, velikost):
    if len(ovoce) == 0 or tah % 10 == 0:
        while True:
            x = randrange(velikost[0])
            y = randrange(velikost[1])
            if (x, y) not in had:
                ovoce.append((x, y))
                break


def ano_ne(question):
    '''
    Funkce, která chce po uživateli ano (vrátí True) nebo ne (vrátí False).
    '''
    while True:
        answer = input(question)
        if answer.lower().strip() == 'ano' or answer.lower().strip() == 'a':
            return True
        elif answer.lower().strip() == 'ne' or answer.lower().strip() == 'n':
            return False
        else:
            print('Nerozumím! Odpověz "ano" nebo "ne".')


def uzivatel_zada_pismeno():
    '''
    Uživatel zadá písmeno pro směr, kterým se má had posunout.
    '''
    while True:
        pismeno = input('''Kam se chceš posunout? Napiš W↑ S↓ D→ A←.
Pro ukončení napiš Q -->  ''')
        pismeno = pismeno.lower()
        if pismeno in ['w', 's', 'd', 'a', 'q']:
            return pismeno


def vypis_intro():
    with open('snake.txt', encoding='utf-8') as napis:
        text = napis.read()
    print(text)
    input('Zmáčkni ENTER a pokračuj')


def vypis_hru(velikost, had, ovoce):
    clear()
    print('''Hrajeme hada, můžeš se posouvat na čtyři světové strany:
    W = ↑ (nahoru)
    S = ↓ (dolů)
    D = → (vpravo)
    A = ← (vlevo).''')
    nakresli_mapu(velikost, had, ovoce)


def hra():
    vypis_intro()

    # Na začátku si nastavím výchozí mapu a vytisknu na obrazovku
    had = [(0, 0), (1, 0), (2, 0)]
    ovoce = []
    tah = 1
    velikost = (15, 15)
    ovoce_pole(ovoce, had, tah, velikost)
    vypis_hru(velikost, had, ovoce)

    # pak samotná hra
    while True:
        smer = uzivatel_zada_pismeno()
        if smer == 'q':
            print('To je konec hry.')
            break
        pohyb(velikost, had, smer, ovoce)
        ovoce_pole(ovoce, had, tah, velikost)
        vypis_hru(velikost, had, ovoce)
        print('Had je dlouhý {} polí.'.format(len(had)))
        tah += 1


hra()
