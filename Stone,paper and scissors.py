import random

word = input('Введите свое слово: ')

list1 = ['Камень', 'Ножницы', 'Бумага']
word2 = random.randint(0, len(list1) - 1)
print('Компьютер выбирает: ', list1[word2])

if word == list1[word2]:
    print('Играем снова!')
elif (word == 'Камень' and list1[word2] == 'Ножницы') or (word == 'Бумага' and list1[word2] == 'Камень') or (word == 'Ножницы' and list1[word2] == 'Бумага'):
    print('Вы выиграли!')
elif (word == 'Камень' and list1[word2] == 'Бумага') or (word == 'Бумага' and list1[word2] == 'Ножницы') or (word == 'Ножницы' and list1[word2] == 'Камень'):
    print('Вы проиграли!')