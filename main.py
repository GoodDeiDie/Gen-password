import random


pwd_lenght = int(input("Введите длину пароля:"))
pwd_digits = input('Включить числа? ( да = y , нет = n)')
pwd_upercase = input('Включить верхний регистр? ( да = y , нет = n)')
pwd_lowercase = input('Включить нижний регистр? ( да = y , нет = n)')
pwd_punctuation = input('Включить знаки "!#$%&*+-=?@^_"? ( да = y , нет = n)')


digits = '1234567890'
upercase = 'ABCDEFGHIGKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghigklmnopqrstuvwxyz'
punctuation = '!#$%&*+-=?@^_'

new_password = ''

pull = ''

if pwd_digits == 'y':
    pull += digits
if pwd_upercase == 'y':
    pull += upercase
if pwd_lowercase == 'y':
    pull+= lowercase
if pwd_punctuation == 'y':
    pull+= punctuation

for i in range(pwd_lenght):
    new_password += pull[random.randint(0, len(pull)-1)]

print("Ваш новый пароль: " + new_password)