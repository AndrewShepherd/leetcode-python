directions = (
    (-1, 0),
    (1, 0),
    (0, 1),
    (0, -1)
)


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        m = len(board)
        n = len(board[0])
        protected_coordinates = set()
        for r in range(m):
            if board[r][0] == 'O':
                protected_coordinates.add((r, 0))
            if board[r][n-1] == 'O':
                protected_coordinates.add((r, n-1))
        for c in range(n):
            if board[0][c] == 'O':
                protected_coordinates.add((0, c))
            if board[m-1][c] == 'O':
                protected_coordinates.add((m-1, c))
        to_do = list(protected_coordinates)
        while to_do:
            c = to_do.pop()
            for other in [(c[0] + d[0], c[1]+ d[1]) for d in directions]:
                if not 0 <= other[0] < m:
                    continue
                if not 0 <= other[1] < n:
                    continue
                if other in protected_coordinates:
                    continue
                if board[c[0]][c[1]] == 'X':
                    continue
                protected_coordinates.add(other)
                to_do.append(other)
        for r in range(1, m):
            for c in range(1, n):
                if not (r,c) in protected_coordinates:
                    board[r][c] = 'X'