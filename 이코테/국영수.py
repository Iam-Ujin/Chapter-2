'''
학생 n명의 이름과 국어, 영어, 수학 점수
1. 국어 점수가 감소하는 순서로
2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
3.국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로(아스키코드에서 대문자는 소문자보다 작으므로 사전순으로 앞)
'''

n = int(input())
array = []

for _ in range(n):
    name, kor, eng, math = input().split()
    array.append((name, int(kor), int(eng), int(math)))