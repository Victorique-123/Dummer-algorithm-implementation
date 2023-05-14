import sys
import random
import os
import math
import numpy as np
import itertools
from scipy.special import comb
from itertools import product
import time
from itertools import combinations
from random import choice

def get_P_tau(n, t):
    p_and_tau = []
    for tau_p in range(t+1):
      for p in range(n-1):      
        if (comb(p+1,(tau_p+1))>comb(n-p-1,t-(tau_p+1))) and (comb(p,tau_p)<=comb(n-p,t-tau_p)):
          p_and_tau.append((p,tau_p))
    p_and_tau=list(set(p_and_tau))
    return p_and_tau

def binary_to_int(binary_row):
    binary_str = ''.join(str(bit) for bit in binary_row[:3])
    return int(binary_str, 2)

def binary_addition(a, b):
    return [ai ^ bi for ai, bi in zip(a, b)]

def process_array(array, n, k):
    array = np.array(array)
    result = set()
    i = 0
    
    array = array[np.lexsort(array[:, :n - k + 1].T[::-1])]
    
    while i < len(array):
        temp = []
        group_start = i

        while i + 1 < len(array) and (array[i, :n - k] == array[i + 1, :n - k]).all():
            i += 1
        group_end = i
        
        for r1 in range(group_start, group_end + 1):
          for r2 in range(r1, group_end + 1):
            if array[r1, n - k] == 0 and array[r2, n - k] == 1:
              addition_result = binary_addition(array[r1, -n:], array[r2, -n:])
              result.add(tuple(addition_result))
        i += 1

    return np.array([list(r) for r in result])


def find_e(s, w, H):
  k,n = H.shape
  c_full=[]
  for t in range(1, w + 1):
      p_and_tau = get_P_tau(n, t)
      for x in p_and_tau:
        p, tau_p = x
        H0 = H[:, :p]
        H1 = H[:, p:]
        num_p = list(range(p))
        comb_tau = list(itertools.combinations(num_p,tau_p))

        num_n_p = list(range(n-p))
        comb_t_tau = list(itertools.combinations(num_n_p, t-tau_p))

        Z0 = []
        for i in comb_tau:
          e_0 = np.zeros(p)
          e_0[list(i)] = 1
          v0 = np.mod(np.dot(e_0, H0.T),2).astype(int)
          ax = np.concatenate((v0, [0], e_0, np.zeros(n-p)))
          Z0.append(ax)

        Z1 = []
        for i in comb_t_tau:
          e_1 = np.zeros(n-p)
          e_1[list(i)]=1
          v1=np.mod(np.dot(e_1, H1.T),2).astype(int)
          bx=np.concatenate((np.mod(v1+s,2), [1], np.zeros(p),e_1))
          Z1.append(bx)
        Z = np.array(Z0 + Z1).astype(int)
        Z = np.array(sorted(Z, key=binary_to_int)).astype(int)
        box=process_array(Z, n, k)
        if len(box)!=0:
          return box
  return c_full