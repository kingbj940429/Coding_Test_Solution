''' 5568번 카드 놓기 '''

from itertools import permutations, combinations

if __name__ == "__main__":
    N = int(input())
    K = int(input())

    datas = [input() for _ in range(N)]

    permus = list(permutations(datas,K))
    result = []
    for per in permus:
        result.append("".join(per))
    result = set(result)
    print(len(result))
    

