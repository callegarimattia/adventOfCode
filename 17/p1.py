import sys
import heapq

D = open(sys.argv[1]).read().strip()
G = [[int(c) for c in line] for line in D.split("\n")]
R = len(G)
C = len(G[0])

DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def show(G):
    for line in G:
        print(line)


def dijkstra(G, part2):
    Q = [(0, (0, 0), -1, -1)]
    D = {}
    while Q:
        (dist, point, dir, count) = heapq.heappop(Q)
        if (point, dir, count) in D:
            continue
        D[(point, dir, count)] = dist
        for i, (dx, dy) in enumerate(DIR):
            x, y = point
            xx, yy = x + dx, y + dy
            n_dir = i
            n_count = 1 if n_dir != dir else count + 1
            part1_check = n_count <= 3
            part2_check = n_count <= 10 and (n_dir == dir or count >= 4 or count == -1)
            valid = part1_check if not part2 else part2_check
            if 0 <= xx < R and 0 <= yy < C and valid and ((n_dir + 2) % 4 != dir):
                if ((xx, yy), n_dir, n_count) in D:
                    continue
                heapq.heappush(Q, (dist + G[xx][yy], (xx, yy), n_dir, n_count))
    return D


def solve(part2=False):
    show(G)
    ans = 1e10
    D = dijkstra(G, part2)
    for k, v in D.items():
        point, _, _ = k
        if point == (R - 1, C - 1):
            ans = min(ans, v)
    print(ans)


solve()
solve(True)
