#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    li = []
    pr = 1
    s = 0
    f = True
    fn = -1
    ln = -1

    n = int(input('Введите количество чисел в списке: '))
    print('Введите числа в список: ')
    for i in range(n):
        li.append(int(input()))
        if (i + 1) % 2 == 0:
            pr *= li[i]
        if li[i] == 0:
            if f:
                fn = i
                f = False
            ln = i

    if fn != -1 and ln != -1:
        for i in range(fn, ln):
            s += li[i]
    print('Произведение элементов списка с четными номерами = ', pr)
    print('Сумму элементов списка, расположенных между первым и '
          'последним нулевыми элементами', s)

    li.sort(reverse=True)
    print('Отсортированный список: ', li)