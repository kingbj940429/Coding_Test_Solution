''' 5437번 LCM '''
from math import gcd

def  lcd(a,b):
    return a*b//gcd(a,b)

N = int(input())

for _ in range(N):
    a,b = map(int,input().split())
    print(lcd(a,b))

