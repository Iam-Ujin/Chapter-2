'''
학생 수 n
학생의 이름 + 점수
모든 학생의 이름을 성적이 낮은 순으로 출력
성적이 동일한 학생들의 순서는 자유롭게
입력
2
홍길동 95
이순신 77
출력
이순신 홍길동
'''

n = int(input())
array = []

for _ in range(n):
    name, score = input().split()
    array.append((name, int(score)))

array = sorted(array, key= lambda x:x[1])
answer = [(i + 1, x[0], x[1] + 5) for i, x in enumerate(array)]
print(answer)
for elem in array:
    print(elem[0], end=' ')