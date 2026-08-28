"""
[재귀 함수 - 팩토리얼과 피보나치 수열]

문제 설명:
- 재귀 함수를 사용하여 팩토리얼과 피보나치 수를 계산합니다.
- 재귀의 기본 개념인 base case와 recursive case를 이해합니다.

입력:
- n: 양의 정수

출력:
- 팩토리얼: n!
- 피보나치: n번째 피보나치 수

예제:
입력: n = 5
팩토리얼 출력: 120 (5! = 5 × 4 × 3 × 2 × 1)
피보나치 출력: 5 (0, 1, 1, 2, 3, 5)

힌트:
- 팩토리얼: n! = n × (n-1)!, 0! = 1
- 피보나치: fib(n) = fib(n-1) + fib(n-2), fib(0) = 0, fib(1) = 1
"""

def factorial(n):
    if n == 1 or n == 0:
        return 1
    for fact in range(n):
        return factorial(n-1) * n
    # TODO: base case를 작성하세요
    # n이 0이거나 1이면 1을 반환
    pass
    
    # TODO: recursive case를 작성하세요
    pass
fib = {}
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    if n not in fib:
        fib[n] = fibonacci(n-2) + fibonacci(n-1)
    return fib[n]


# 테스트 케이스
if __name__ == "__main__":
    # 팩토리얼 테스트
    print("=== 팩토리얼 계산 ===")
    for i in range(6):
        result = factorial(i)
        print(f"{i}! = {result}")
    print()
    
    # 피보나치 테스트
    print("=== 피보나치 수열 ===")
    for i in range(10):
        result = fibonacci(i)
        print(f"fib({i}) = {result}")
    print()
    
    # 추가 테스트
    print("=== 추가 테스트 ===")
    print(f"10! = {factorial(10)}")
    print(f"fib(15) = {fibonacci(15)}")


