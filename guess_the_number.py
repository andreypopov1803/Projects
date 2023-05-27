from random import randint
number1 = int(input('Введите начальное число диапазона: '))
number2 = int(input('Введите конечное число диапазона: '))
number = int(input('Введите свое число: '))
def guess_the_number(number):
    n = randint(number1, number2)
    print(n)
    if n == number:
        print('Верно! Загаданное число было: ', n)
    else:
        print('К сожалению, вы не угадали. Загаданным числом было: ', n)
guess_the_number(number)