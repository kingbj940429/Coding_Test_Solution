''' 5622번 다이얼 '''

dial = [
     []
    ,[]
    ,['A','B','C']
    ,['D','E','F']
    ,['G','H','I']
    ,['J','K','L']
    ,['M','N','O']
    ,['P','Q','R','S']
    ,['T','U','V']
    ,['W','X','Y','Z']
    ]

input_data = list(input())
result = 0
for i in input_data:
    for j in range(len(dial)):
        if i in dial[j]:
            result += (j+1)
print(result)
