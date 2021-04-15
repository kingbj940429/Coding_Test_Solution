''' 2607번 비슷한 단어 '''

n = int(input()) 
words= [] 
for _ in range(n): 
    word = input() 
    words.append(word) 

first_word = [0 for i in range(32)] 

ans = 0 
for i in range(len(words)): 
    word = [0 for j in range(32)] 
    # 첫번째 단어 
    if i ==0 : 
        for c in words[i]: 
            first_word[ord(c)%65] += 1 
    else: 
        for c in words[i]: 
            word[ord(c)%65] += 1 
            
    if ''.join(str(word)) == ''.join(str(first_word)): 
        ans +=1 
        continue; 
    # 기존 문자를 빼는경우 
    for j in range(32): 
        if word[j] >=1: 
            word[j] -= 1 
            if ''.join(str(word)) == ''.join(str(first_word)): 
                ans +=1 
                continue 
            word[j] +=1 
    for j in range(32): 
        word[j] += 1 
        if ''.join(str(word)) == ''.join(str(first_word)): 
            ans +=1 
            continue 
        word[j] -=1  
    for j in range(32): 
        if word[j] >= 1: 
            word[j] -= 1 # 다른문자로 대체 
            for k in range(32): 
                if k != j: 
                    word[k] +=1 
                    if ''.join(str(word)) == ''.join(str(first_word)): 
                        ans +=1 
                        continue 
                    word[k] -=1 
            word[j] +=1 
print(ans)
