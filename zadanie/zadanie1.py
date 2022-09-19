#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    U = []
    D = []
    V = []
    S = []
    for i in range(7):
        if i == 0:
            print('Понедельник')
        elif i == 1:
            print('Вторник')
        elif i == 2:
            print('Среда')
        elif i == 3:
            print('Четверг')
        elif i == 4:
            print('Пятница')
        elif i == 5:
            print('Суббота')
        else:
            print('Воскресенье')

        U.append(int(input('Введите значение утренней температуры: ')))
        D.append(int(input('Введите значение дневной  температуры: ')))
        V.append(int(input('Введите значение вечерней температуры: ')))
        print('\n')

        S.append(int((U[i] + D[i] + V[i])/3))

    sr_temp = 0
    for i in S:
        sr_temp += i
    sr_temp += sr_temp / 7

    print('Средние температуры за утро, день и вечер соответственно: ', S)