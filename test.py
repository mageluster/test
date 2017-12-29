#!/usr/bin/python
from __future__ import print_function, division

def suma(x, y):
    """

    :param x:
    :param y:
    :return:
    """
    print('Suma to: ', end='')
    return x + y


def roznica(x, y):
    print('Odejmowanko to: ', end='')
    return x - y


def iloczyn(x, y):
    print('Mnozonko to: ', end='')
    return x * y


def iloraz(x, y):
    print('Dzielonko to: ', end='')
    return x / y


def inator():
    print('1. Dodawator\n2. Odejmowator\n3. Mnozator\n4. Podzielator')
    operacje = {
        1: suma,
        2: roznica,
        3: iloczyn,
        4: iloraz
    }
    dzialanie = None
    while dzialanie not in operacje:
        try:
            dzialanie = int(raw_input(('Co chcesz robic?: ')))
        except ValueError:
            print('Wybierz dzialanie z listy Dziadu!')

    x = None
    y = None
    while x is None:
        try:
            x = int(raw_input('podaj x: '))
        except ValueError:
            print('Ziomeczku tylko liczby calkowite')

    while y is None or (dzialanie == 4 and y == 0):
        try:
            y = int(raw_input('podaj y: '))
        except ValueError:
            print('Ziomeczku tylko liczby calkowite')

    print(operacje[dzialanie](x, y))



def main():
    print('Wieloinator 1.0')
    inator()

    while True:
        pytanie = raw_input('Ziomeczku czy kontynuowac? (y/n): ')
        if pytanie not in ['y', 'Y', 'n', 'N']:
            continue
        elif pytanie in ['y', 'Y']:
            inator()
        else:
            print('Nara Ziomeczku!')
            break

    # print('Suma to: {0}'.format(suma(x, y)))


if __name__ == "__main__":
    main()