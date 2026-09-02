def rotate_matrix_90(matrix):
    n = len(matrix)  # 행렬의 크기 (3x3 행렬이므로 n = 3)
    
    # 회전된 결과를 담을 3x3 크기의 0으로 채워진 2차원 리스트 생성
    # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    result = [[0] * n for _ in range(n)]
    
    # 2차원 배열 전체를 순회 (i: 행 인덱스, j: 열 인덱스)
    for i in range(n):
        for j in range(n):
            # 시계 방향으로 90도 회전시키는 핵심 공식:
            # 원본 matrix[i][j]의 값이 회전 후 result[j][n-1-i] 위치로 이동함
            result[j][n - 1 - i] = matrix[i][j]
            
    # 90도 회전이 완료된 새로운 행렬을 반환
    return result

def print_matrix(matrix):
    # 2차원 리스트의 각 행(row)을 한 줄씩 출력해주는 함수
    for row in matrix:
        print(row)
            




# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1: 3x3 배열
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("원본 배열:")
    print_matrix(matrix1)
    print("\n회전 후:")
    rotated1 = rotate_matrix_90(matrix1)
    print_matrix(rotated1)
    print()
    
    # 테스트 케이스 2: 4x4 배열
    matrix2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    
    print("원본 배열:")
    print_matrix(matrix2)
    print("\n회전 후:")
    rotated2 = rotate_matrix_90(matrix2)
    print_matrix(rotated2)


