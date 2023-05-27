import random
numbers_of_symbols = int(input('Введите количество символов в пароле: '))
str_of_symbols = ('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz12345678909')
list_of_symbols = list(str_of_symbols)
password = []
def generator_of_passwors():
    for i in list_of_symbols:
        symbol = random.randint(0, len(list_of_symbols) - 1)
        password.append(list_of_symbols[symbol])
        if len(password) ==numbers_of_symbols:
            break
    print("Ваш пароль:")
    print(''.join(password))
generator_of_passwors()