
def solution(n):
    def DFS(row, cols, diag1, diag2):
        if row == n:
            return 1
        count = 0
        for col in range(n):
            if col not in cols and (row - col) not in diag1 and (row + col) not in diag2:
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                count += DFS(row + 1, cols, diag1, diag2)
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
        return count

    return DFS(0, set(), set(), set())