# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, вывести правильный ответ.

import random


def game():
    number = random.randint(1, 100)
    print("Игра ОТГАДАЙ ЧИСЛО ОТ 1 до 100 за 10 попыток")
    count = 0
    while True:
        count += 1
        if count > 10:
            print(f'вы проиграли, загаданное число {number}')
            break
        print(f'Попытка № {count}')
        user_number = int(input('введите число:  '))
        if user_number == number:
            print(f'Вы победили, загаданное число {number}')
            break
        elif number < user_number:
            print('Ваше число больше загаданного')
        else:
            print('ваше число меньше загадонного')


game()
