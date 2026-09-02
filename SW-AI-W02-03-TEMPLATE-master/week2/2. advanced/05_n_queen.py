def n_queens(n: int) -> int:
    cols = [0] * n
    count = 0
   
    def place(row):  ###가로 row 세로 c
        nonlocal count

        if row == n:
            count += 1
            return

        for c in range(n):
            safe = True

            for i in range(row):
                
                if cols[i] == c:  # 같은 열 검사
                    safe = False
                    break

                if abs(cols[i] - c) == abs(i - row):  # 대각선 검사
                    safe = False
                    break

            if safe:
                cols[row] = c
                place(row + 1)
                cols[row] = 0
    place(0)
    return count
    
if __name__ == "__main__":
    print("[테스트] N=1 ~ N=8 에 대한 가능한 배치의 수")
    for n in range(1, 9):
        print(f"  N={n}: {n_queens(n)}")
