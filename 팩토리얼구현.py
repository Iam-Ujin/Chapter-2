n = int(input())

# for문을 활용한 팩토리얼 구현
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i

    return result

# 재귀함수를 이용한 팩토리얼 구현
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


print("반복적 구현: ", factorial_iterative(n))
print("재귀적 구현: ", factorial_recursive(n))