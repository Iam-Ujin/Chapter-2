'''
정수 n이 입력되면 n시 59분 59초까지 3이 포함되는 경우의 수 출력
입력 5
출력 11475
'''

n = int(input())
result = 0
for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if "3" in str(i) + str(j) + str(k):
                result += 1

print(result)
