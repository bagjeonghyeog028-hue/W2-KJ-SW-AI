def dfs(graph, start, visited=None):
    # TODO: visited가 None이면 초기화
    if visited is None:
        visited = []
    # TODO: 현재 정점 방문
    if start not in visited:    
        visited.append(start)
        for neighbor in graph[start]:    # TODO: 인접한 정점들에 대해 재귀 
            if neighbor not in visited:  ## 방문하지 않은 정점이면 재귀 호출
                dfs(graph, neighbor, visited)
    return visited

        
# 테스트 케이스
if __name__ == "__main__":
    # 그래프 생성
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    
    print("=== DFS (깊이 우선 탐색) ===")
    result = dfs(graph, 0)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")


