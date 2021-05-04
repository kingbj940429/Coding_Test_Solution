''' 1251번 단어 나누기 '''
'''
1. 가장 빠른 알파벳 3개를 고른다.
2. 3개의 알파벳 기준으로 문자열을 3등분으로 나눈다.
3. 3등분한 문자열을 뒤집고 합친다.
'''
s = input()
li = []
for i in range(len(s)-2):
    for j in range(i+1, len(s)-1):
        for k in range(j+1, len(s)):
            t = s[:j][::-1] + s[j:k][::-1] + s[k:][::-1]
            li.append(t)
print(min(li))

