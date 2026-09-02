import heapq

def process_emergency_room(patients):
    heap = []
    for name, priority in patients:
        heapq.heappush(heap, (priority, name))
    processed = []

    while heap:
        priority, name = heapq.heappop(heap)
        print(f"처리: {name} (우선순위: {priority})")  ##f
        processed.append((name))
        
    return processed
    
# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    patients1 = [
        ("김철수", 3),
        ("이영희", 1),
        ("박민수", 2)
    ]
    print("=== 응급실 환자 처리 ===")
    result1 = process_emergency_room(patients1)
    print(f"처리 순서: {result1}")
    print()
    
    # 테스트 케이스 2
    patients2 = [
        ("환자A", 5),
        ("환자B", 1),
        ("환자C", 3),
        ("환자D", 2)
    ]
    print("=== 응급실 환자 처리 ===")
    result2 = process_emergency_room(patients2)
    print(f"처리 순서: {result2}")


