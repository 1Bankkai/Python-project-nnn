n = input('Введите 3-х значное число -')
while type(n) !=int:
    try:
        n = int(n)
    except ValueError:
        print('Вы ввели не число')

if 100 <= n <= 999 and n % 2 == 1:
    print('Нечетное число')
else:
    print('не является нечетным(четное)')