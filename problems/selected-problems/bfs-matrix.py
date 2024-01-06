def route_exists(from_row, from_column, to_row, to_column, map_matrix):
    n = len(map_matrix)
    m = 0
    if map_matrix:
        m = len(map_matrix)
    start = (from_row, from_column)
    end = (to_row, to_column)
    seen = set()
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = []
    q.append(start)
    while q:
        pos = q.pop()
        if pos == end:
            return True
        for y, x in dirs:
            next = (pos[0] + y, pos[1] + x)
            if next not in seen and 0 <= next[0] < n and 0 <= next[1] < m:
                if map_matrix[next[0]][next[1]]:
                    q.append(next)
                seen.add(next)

    return False


if __name__ == '__main__':
    map_matrix = [
        [True, False, False],
        [True, True, False],
        [False, True, True]
    ]

    print(route_exists(0, 0, 2, 2, map_matrix))
