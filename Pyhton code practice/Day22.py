def numCells(grid):
    n = len(grid)
    m = len(grid[0])
    count = 0

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    for i in range(n):
        for j in range(m):
            dominant = True

            for dx, dy in directions:
                ni, nj = i + dx, j + dy

                if 0 <= ni < n and 0 <= nj < m:
                    if grid[i][j] <= grid[ni][nj]:
                        dominant = False
                        break

            if dominant:
                count += 1

    return count