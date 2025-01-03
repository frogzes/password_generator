import random

password = ''
i = 0
password_lenght = int(input('Please enter a number for lenght of password: '))

for i in range(password_lenght):
    a = random.randint(0, 9)
    password = password + str(a)

print(password)