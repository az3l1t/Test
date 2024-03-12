# print(2)
# 37 Вариант
from itertools import product
from math import floor,ceil

def main(PHI):
    psi = {5*p for p in PHI if p < -60}
    omega = {floor(p/2) for p in PHI if (p>=-7) ^ (p<=96)}
    ksi = {abs(p) for p in psi if p<-2 or p >=11}
    epsilon = {ceil(w/9) - abs(w) for w in omega if (w>=-29) ^ (w<=51)}
    total = 0
    for o,k in product(epsilon,ksi):
        total += 2*o-k
    return len(epsilon)-total