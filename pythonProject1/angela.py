import random

k = random.randint(1, 100)
count = 0
popytki = 0
print('Добро пожаловать в числовую угадайку')
limi = input('введите  сложность, "легко"или"сложно" ')
if limi == "легко":
    popytki = 10
else:
    popytki = 7




def is_valid(n):
    if n.isdigit() and 1 <= int(n) <= 100 and count <= popytki:
        return True
    else:
        return False


while True:
    n = input('Введите число от 1 до 100:')

    count += 1
    if is_valid(n) == True:
        n = int(n)
        print(n)


    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
    if n < k:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif n > k:
        print('Ваше число больше загаданного, попробуйте еще разок')
    else:
        print('Вы угадали, поздравляем!')
        print(count)
        break

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
