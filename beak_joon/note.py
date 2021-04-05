''' 연습장 '''

from math import gcd
'''최대공약수'''

def gcd_custom(x, y):
    while y:
        x, y = y, x%y
    return x

print(gcd_custom(18, 24))
print(gcd(18, 24))


''' 최소공배수 '''

def lcm(x, y):
    return x*y // gcd(x,y)

print(lcm(18,24))

def lcms(arr):
    while True:
        arr.append(lcm(arr.pop(), arr.pop()))
        if(len(arr)) == 1:
            return arr[0]

print(lcms([2,4,6,8]))


