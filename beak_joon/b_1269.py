''' 1269번 대칭 차집합 '''

if __name__ == "__main__":
    N, M = map(int,input().split())

    A = list(input().split())
    B = list(input().split())

    A_set = set(A)
    B_set = set(B)

    A_B = A_set - B_set
    B_A = B_set - A_set

    result = len(A_B) + len(B_A)
    print(result)