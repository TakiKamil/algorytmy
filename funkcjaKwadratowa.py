import math

def obliczFunkcjeKwadratowa(a, b, c):
    if (a == 0):
        print('To nie jest funkcja kwadratowa!')
        return False

    print(f'Funkcja: f(x) = {a}x^2 + {b}x + {c}')
    delta = b**2 - (4 * a * c)
    print(f'Delta: {delta}')
    if (delta < 0):
        print('Brak rozwiązań dla tej funkcji')
        return False
    elif(delta == 0):
        x0 = (-1 * b) / (2 * a)
        print(f'Jeden wynik: {x0}')
        return True
    x1 = (-1 * b - math.sqrt(delta)) / (2 * a)
    x2 = (-1 * b + math.sqrt(delta)) / (2 * a)
    print(f'Dwa wyniki: \nx1 = {x1}\nx2 = {x2}')
    return True

def main():
    a = float(input('Podaj a: '))
    b = float(input('Podaj b: '))
    c = float(input('Podaj c: '))
    obliczFunkcjeKwadratowa(a, b, c)
    return 0

if __name__ == '__main__':
    main()
