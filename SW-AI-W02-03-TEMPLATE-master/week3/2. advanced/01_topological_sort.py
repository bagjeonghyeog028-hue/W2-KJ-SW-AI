from collections import deque

def topological_sort(vertices, edges):
    graph = [[] for _ in range(vertices)]
    indegree = [0] * (vertices)  #1

    for u, vertices_node in edges:
        graph[u].append(vertices_node)    #노드 범위 수정시 #(1,2)번에 +1 2번에 1, 붙이기.
        indegree[vertices_node] += 1
    queue = deque()

    for i in range(vertices):  #2
        if indegree[i] == 0:
            queue.append(i)
    result = []

    while queue:
        now = queue.popleft()
        result.append(now)

        for next_node in graph[now]:
            indegree[next_node] -= 1

            if indegree[next_node] == 0:
                queue.append(next_node)

    if len(result) != vertices:
        return []

    return result


# 테스트 케이스
if __name__ == "__main__":
    # 과목 선수과목 예제
    vertices = 4
    edges = [
        (0, 1),  # 0 → 1
        (0, 2),  # 0 → 2
        (1, 3),  # 1 → 3
    ]
    
    print("=== 위상 정렬 ===")
    print("과목 관계:")
    print("  0(기초) → 1(중급) → 3(고급)")
    print("  0(기초) → 2(응용)")
    print()
    
    result = topological_sort(vertices, edges)
    print(f"수강 순서: {result}")
