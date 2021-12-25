def obliczFunkcjeLiniowa(a, b):
    if (a == 0) or (b == 0):
        print('To funkcja stała!')
        return False

    print(f'Funkcja: f(x) = {a}x + {b}')
    print(f'x = {-1 * (b / a)}')
    if (a > 0):
        print('Funkcja jest rosnąca')
    elif (a == 0):
        print('Funkcja jest stała')
    else:
        print('Funkcja jest malejąca')
    return True

def main():
    a = float(input('Podaj a: '))
    b = float(input('Podaj b: '))
    obliczFunkcjeLiniowa(a, b)
    return 0

if __name__ == '__main__':
    main()
