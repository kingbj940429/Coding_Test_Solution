''' 1010번 다리놓기 '''

import math

T = int(input())

for _ in range(T):
    N, M = map(int,input().split())

    result = math.factorial(M) // (math.factorial(M-N) * math.factorial(N))
    print(result)
