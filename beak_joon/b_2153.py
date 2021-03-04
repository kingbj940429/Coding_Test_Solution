''' 2153번 소수 단어 '''
import math
# 소수 판별 함수(에라토스테네스의 체)
def is_prime_number(n):
    # 2부터 n까지의 모든 수에 대하여 소수 판별
    array = [True for i in range(n+1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)

    # 에라토스테네스의 체
    for i in range(2, int(math.sqrt(n)) + 1): #2부터 n의 제곱근까지의 모든 수를 확인하며
        if array[i] == True: # i가 소수인 경우(남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    return [ i for i in range(2, n+1) if array[i] ]

# N이 1,000,000 이내로 주어지는 경우 활용할 것 => 이론상 400만번 정도 연산이고 메모리도 충분함

def alphas():
    start = ord("a") 
    end = ord("z")
    result_dic = {}
    for i in range(0, end-start + 1):
        result_dic[chr(ord("a") + i)] = i+1

    start = ord("A") 
    end = ord("Z")
    for i in range(0, end-start + 1):
        result_dic[chr(ord("A") + i)] = i+1+26

    return result_dic

if __name__ == "__main__":
    result_dic = alphas()
    result_sum = 0
    input_data = input()
    
    for val in input_data:
        result_sum += (result_dic.get(val))
        
    if(result_sum in is_prime_number(result_sum) or result_sum == 1):
        print("It is a prime word.")
    else:
        print("It is not a prime word.")
    