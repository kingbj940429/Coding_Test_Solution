# ''' 1919번 애너그램 만들기 '''

if __name__ == "__main__":
    A = list(input())
    B = list(input())
    cnt = 0

    start = ord("a")
    end = ord("z")

    for i in range(start, end + 1):
        cnt += abs(A.count(chr(i)) - B.count(chr(i)))

    print(cnt)

