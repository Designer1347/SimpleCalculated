import math

def calc(a , b , c):
    '''Это мой калькулятор.
Он умеет вычислять , практически все , что вам нужно!
Введите одну из преложенных ниже операций избегая пробелов , и соблюдая раскладку!!!'''
    if a == '+':
        print('Сумма равна ' + str( b + c))
    elif a == '-':
        print('Разность равна ' + str( b - c))
    elif a == '*':
        print('Произведение равно ' +str( a * b))
    elif a == '**':
        s = input('Какое число? ( F / S )')
        g = float(input('В какую степень? '))
        if s == 'F':
            res = b ** g
            print('Результат : ' + str(res))
        elif s == 'S':
            res = c ** g
            print('Результат: ' + str(res))
    elif a == '/':
        print('Частное ' +str( b / c ))
    elif a == '//':
        print('Целая часть частного равна ' +str( b // c) + ' Остаток равен ' + str ( b % c))
    elif a == 'Сравн':
        if b > c:
            print('Число ' + str(b) + ' Больше числа ' + str(c))
        elif b == c:
            print('Числа ' + str(b) + ' и ' + str(c) + ' равны')
        else:
            print('Число ' + str(b) + ' меньше числа ' +str(c) )
    elif a == 'Фк':
        s = input('Какое число? ( F / S )')
        if s == 'F':
            print('Факториал числа ' + str(b) + ' равен ' + str(math.factorial(b)))
        elif s == 'S':
            print('Факториал числа ' + str(c) + ' равен ' + str(math.factorial(c)))
    elif a == 'Лг':
        s = int(input('Введите основание логарифма '))
        g = int(input('Введите подлогарифмическое число'))
        log = math.log(g, s)
        print('Логарифм числа ' + str(g) + ' по основанию ' + str(s) + ' равен ' + str(log))
    elif a == 'Кор':
        s = input('Какое число? ( F / S )')
        if s == 'F':
            print('Корень числа ' + str(b) + ' равен ' + str(math.sqrt(b)))
        elif s == 'S':
            print('Корень числа ' + str(c) + ' равен ' + str(math.sqrt(c)))
    else :
        print('Попробуйте еще раз! Обратите внимание на регистр и раскладку!!!')
        print()
    print('Работа законченна! Спасибо за использование моего калькулятора!')
print(calc.__doc__)
print()
calc((input('Что делаем?( + , - , * , ** , / , // , Сравн ,Лг , Фк)')) ,
     float(input('Введите 1-е число ')) ,
     float(input('Введите 2-е число ')))
