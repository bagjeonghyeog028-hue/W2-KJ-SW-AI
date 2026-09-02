def manage_grades(students):
    if not students:
        return 0.0, [], 0

    average = sum(students.values()) / len(students)  # 1. 평균 점수 계산
    top_score = max(students.values())  # 2. 최고 점수 및 해당 학생 찾기
    top_student = [name for name, score in students.items() if score == top_score]
    return average, top_student, top_score

def find_student_score(students, name):
    return students.get(name)# 딕셔너리에서 key(이름)에 해당하는 value(점수) 반환 (없으면 None 반환)
    
# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    students1 = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "David": 95
    }
    
    print("=== 학생 성적 관리 ===")
    avg, top_name, top_score = manage_grades(students1)
    print(f"평균 점수: {avg}")
    print(f"최고 점수: {', '.join(top_name)} ({top_score}점)")
    print()
    
    # 테스트 케이스 2: 학생 조회
    print("=== 학생 점수 조회 ===")
    search_name = "Alice"
    score = find_student_score(students1, search_name)
    print(f"{search_name}의 점수: {score}")
    print()
    
    search_name2 = "Eve"
    score2 = find_student_score(students1, search_name2)
    print(f"{search_name2}의 점수: {score2}")


