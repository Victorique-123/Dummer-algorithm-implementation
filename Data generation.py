#!/usr/bin/env python3.5
#Как использовать:
#Использование функции main(n,seed) требует ввода двух значений, n - длина кода, seed - случайное натуральное число, различные семена могут генерировать различные наборы данных для экспериментов.
#Функция возвращает три значения, где w - максимальный вес вектора ошибок, H - случайная проверочная матрица размером (k,n) Скорость кода R=0.5, а s - случайный синдром.

import random
import math
import numpy as np

def dGV(n, k):
    d = 0
    aux = 2**(n-k)
    b = 1
    while aux >= 0:
        aux -= b
        d += 1
        b *= (n-d+1)
        b /= d
    return d 
    
def recover_matrices(half_ht):
    n = 2 * len(half_ht)
    k = n // 2
    # Construct the complete check matrix H
    h = np.hstack((half_ht.T, np.eye(k, dtype=int)))
    return h
    
def main(n, seed):
    w = math.ceil(1.05 * dGV(n,n//2))
    random.seed(seed)
    n = n
    seed = seed
    half_ht=[]
    line = ""
    for i in range(n-n//2):
        for j in range(n//2):
            line += str(random.randint(0,1))
        arr = [int(c) for c in line]
        line = ""
        half_ht.append(arr)
    line = ""

    for j in range(n//2):
        line += str(random.randint(0,1))
    s = [int(c) for c in line]
    H=recover_matrices(np.array(half_ht))
    return w,H,s
