def is_palindrome(s):
    #문자열 s에서 글자를 하나씩 꺼내(c), 알파벳이나 숫자일 때만(isalnum) 가져와서 소문자로 바꾸고(lower), 그 결과들을 모아서 s에 새 리스트로 저장한다."
    s = [c.lower() for c in s if c.isalnum()]

    # 변환된 리스트(s)가 뒤집은 리스트(s[::-1])와 동일한지 비교 후.(True/False)를 반환.
    return s == s[::-1]

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    test1 = "A man, a plan, a canal: Panama"
    result1 = is_palindrome(test1)
    print(f"입력: \"{test1}\"")
    print(f"회문 여부: {result1}")
    print()
    
    # 테스트 케이스 2
    test2 = "race a car"
    result2 = is_palindrome(test2)
    print(f"입력: \"{test2}\"")
    print(f"회문 여부: {result2}")
    print()
    
    # 테스트 케이스 3
    test3 = "Was it a car or a cat I saw?"
    result3 = is_palindrome(test3)
    print(f"입력: \"{test3}\"")
    print(f"회문 여부: {result3}")
    print()
    
    # 테스트 케이스 4
    test4 = "Madam"
    result4 = is_palindrome(test4)
    print(f"입력: \"{test4}\"")
    print(f"회문 여부: {result4}")


