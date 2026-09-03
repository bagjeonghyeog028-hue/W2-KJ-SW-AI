def create_graph(vertices, edges, directed=False):    # 정점 수만큼 빈 리스트 생성 (인접 리스트)
    graph = {i: [] for i in range(vertices)}    # 간선 정보 추가 graph의 i []생성 및 내용인 vertices 추가
    for u, v in edges:
        graph[u].append(v)
        if not directed:
            graph[v].append(u)  # 무방향 그래프일 경우 반대 방향도 추가
    return graph



# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1: 무방향 그래프
    vertices = 4
    edges = [(0, 1), (0, 2), (1, 2), (2, 3)]
   
    print("=== 무방향 그래프 ===")
    graph = create_graph(vertices, edges, directed=False)
    for vertex, neighbors in graph.items():
        print(f"{vertex} → {neighbors}")
    print()
   
    # 테스트 케이스 2: 방향 그래프
    print("=== 방향 그래프 ===")
    graph_directed = create_graph(vertices, edges, directed=True)
    for vertex, neighbors in graph_directed.items():
        print(f"{vertex} → {neighbors}")


