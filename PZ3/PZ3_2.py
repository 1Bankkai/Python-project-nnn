
a = input('Введите 1 число -')
b = input('Введите 2 число -')
n = input('Введите 3 число -')

while type(a) != int and type(b) != int and type(n) != int:
    try:
        a = int(a)
        b = int(b)
        n = int(n)
    except ValueError:
        print('Вы ввели не числа!')
        a = input('Введите 1 число -')
        b = input('Введите 2 число -')
        n = input('Введите 3 число -')

if (a <= b <= n) or (n <= b <= a):
    print(b)
elif (b <= a <= n) or (n <= a <= b):
    print(a)
elif (a <= n <= b) or (b <= n <= a):
    print(n)


