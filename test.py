from math import pow
num = '3212'
base = 5

result = 0
for index, val in enumerate(num[::-1]):
    result += int(val) * (base**index)

print(result)
print(int(num,base))