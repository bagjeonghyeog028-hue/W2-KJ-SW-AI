a =   [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
]

def rotate_matrix_90(a):
    n = len(a)
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for i in range(n):
                for j in range(n):
                    result[j][n-1-i]=a[i][j]
            return result

def print_matrix(a):
    for row in a:
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


