import heapq
#이진 힙
INF = float('inf')  #or `NaN = float('nan')`

def dijkstra(n: int, edges: list, start: int) -> list:

    #n: 정점 수 (정점 번호 0 ~ n-1)
    #edges: (u, v, w) 형식 방향 간선 리스트
    #start: 출발 정점
    #반환: 길이 n 의 거리 리스트 (도달 불가 = float('inf'))

    # TODO: 인접 리스트 graph 구성 (graph[u] = [(v, w), ...])
    # TODO: dist 를 INF 로 초기화하고 dist[start] = 0
    # TODO: 우선순위 큐(heapq)로 BFS-like 최단경로 탐색
    # TODO: dist 반환
    
    graph
#무방향 그래프: 정점 u와 v가 연결되어 있다면, u의 리스트에 v를 추가하고, v의 리스트에도 u를 추가합니다.
#방향 그래프: 정점 u에서 v로 가는 간선만 있다면, u의 리스트에만 v를 추가합니다.
#가중치 그래프: 연결된 정점 번호와 함께 간선의 가중치(Cost)를 쌍(Pair)이나 객체 형태로 함께 저장합니다.

def _format(dist):
    return [('INF' if x == INF else x) for x in dist]  #출력 표기를 위한 헬퍼: float('inf') 는 'INF' 로 보여줌


if __name__ == "__main__":
    print("[테스트 1] 예시 그래프 (5개 정점)")
    n = 5
    edges = [
        (0, 1, 4),
        (0, 2, 1),
        (2, 1, 2),
        (2, 3, 5),
        (1, 3, 1),
        (3, 4, 3),
    ]
    print(f"  n={n}, start=0")
    print(f"  최단 거리: {_format(dijkstra(n, edges, 0))}")
    print()

    print("[테스트 2] 정점 1개")
    print(f"  n=1, edges=[], start=0")
    print(f"  최단 거리: {_format(dijkstra(1, [], 0))}")
    print()

    print("[테스트 3] 도달 불가능한 정점 포함")
    n = 4
    edges = [(0, 1, 5)]
    print(f"  n={n}, edges={edges}, start=0")
    print(f"  최단 거리: {_format(dijkstra(n, edges, 0))}")
    print()

    print("[테스트 4] 동일한 거리의 두 경로 (둘 다 7)")
    n = 4
    edges = [(0, 1, 3), (1, 3, 4), (0, 2, 5), (2, 3, 2)]
    print(f"  n={n}, edges={edges}, start=0")
    print(f"  최단 거리: {_format(dijkstra(n, edges, 0))}")
    print()

    print("[테스트 5] 0 가중치 간선 포함")
    n = 3
    edges = [(0, 1, 0), (1, 2, 0), (0, 2, 5)]
    print(f"  n={n}, edges={edges}, start=0")
    print(f"  최단 거리: {_format(dijkstra(n, edges, 0))}")
