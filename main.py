# Импортируем модуль случайного выбора

import random

# Функция для проверки числовое ли значение введено 

def pwd_lenghtf():
    while True:
        try:
            our_case = int(input("Введите длину пароля:"))
            break
        except:
            print('Введите число.')
    return our_case
        
# Функция для проверки нужные ли нам значения введены

def true_or_False(text):
    while True:
        try:
            our_case = input(text + '( да = y , нет = n)')
            if our_case == 'y' or our_case == 'n':
                break
            else:
                print('Введите "y" если да, или "n" если нет.')
        except:
            print('Введите "y" если да, или "n" если нет.')
    return our_case


# Инициализируем наши переменные

pwd_lenght = pwd_lenghtf()
pwd_digits = true_or_False('Включить числа?')
pwd_upercase = true_or_False('Включить верхний регистр?')
pwd_lowercase = true_or_False('Включить нижний регистр?')
pwd_punctuation = true_or_False('Включить знаки "!#$%&*+-=?@^_"?')

# Добавляем общие словари, пулл выбора и новый пароль.

digits = '1234567890'
upercase = 'ABCDEFGHIGKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghigklmnopqrstuvwxyz'
punctuation = '!#$%&*+-=?@^_'

new_password = ''

pull = ''

# Заполняем пулл доступными символами в зависимости от выбора

if pwd_digits == 'y':
    pull += digits
if pwd_upercase == 'y':
    pull += upercase
if pwd_lowercase == 'y':
    pull+= lowercase
if pwd_punctuation == 'y':
    pull+= punctuation

# Перебираем наш пул, в зависимости от длины нужного пароля и составляем его, затем выводим на экран.
 
for i in range(pwd_lenght):
    new_password += pull[random.randint(0, len(pull)-1)]

print("Ваш новый пароль: " + new_password)