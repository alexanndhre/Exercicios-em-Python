import math
import os
import random
import re
import sys

def MiniMaxSum(arr):
    lista_ord = sorted(arr)
    menores = sum(lista_ord[:4])
    maiores = sum(lista_ord[-4:])
    return print(maiores,menores)

arr = list(map(int, input("Informe uma lista de números separados por espaço:").rstrip().split()))
MiniMaxSum(arr)

