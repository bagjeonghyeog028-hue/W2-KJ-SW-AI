def fibonacci_memo(n, memo=None):
    if memo is None:  # TODO: memo가 None이면 빈 딕셔너리로 초기화
        memo = {}
    if n in memo:  # TODO: 이미 계산한 값이 memo에 있으면 반환
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 2,memo) + fibonacci_memo(n - 1,memo)
    return memo[n]
    
    # TODO: 재귀 호출하여 계산하고 memo에 저장
    


# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    print("=== 피보나치 수열 (메모이제이션) ===")
    for i in range(11):
        result = fibonacci_memo(i)
        print(f"fib({i}) = {result}")
    print()
    
    # 테스트 케이스 2: 큰 수도 빠르게 계산
    print("=== 큰 수 계산 ===")
    n = 50
    result = fibonacci_memo(n)
    print(f"fib({n}) = {result}")
    print()
    
    # 비교: Week1의 재귀 방식은 fib(50)을 계산하기 어려움
    print("참고: 일반 재귀는 fib(40)도 몇 초 걸리지만")
    print("메모이제이션은 fib(100)도 순식간에 계산!")


