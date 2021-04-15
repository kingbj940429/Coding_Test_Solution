''' 1453번 피시방 알바 '''

if __name__ == "__main__":
    N = int(input())
    people = list(map(int, input().split()))
    
    posi = []
    cnt = 0
    for per in people:
        if(per not in posi):
            posi.append(per)
        else:
            cnt += 1
    print(cnt)



