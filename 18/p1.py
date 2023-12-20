import sys
from tqdm import trange

D = open(sys.argv[1]).read().strip().split("\n")

DIRS = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (-1, 0),
    "D": (1, 0),
}

HEX_DIRS = {
    "0": "R",
    "1": "D",
    "2": "L",
    "3": "U",
}


def get_dirs(part2):
    if not part2:
        dirs, dists = [], []
        for line in D:
            data = line.split(" ")
            dirs.append(data[0])
            dists.append(int(data[1]))
    else:
        dirs, dists = [], []
        for line in D:
            data = line.split(" ")[-1]
            data = data[2:]  # ditch the #
            dist = data[:5]
            dists.append(int(dist, 16))
            dirs.append(HEX_DIRS[data[-2]])
    return dirs, dists


def get_verts(part2):
    dirs, dists = get_dirs(part2)
    V = [(0, 0)]
    x, y = 0, 0
    for i in trange(0, len(dirs)):
        dx, dy = DIRS[dirs[i]]
        for _ in range(dists[i]):
            x += dx
            y += dy
            V.append((x, y))
    return V


def shoelace(V):
    area = 0
    for i in trange(len(V)):
        area -= V[i][0] * V[(i + 1) % len(V)][1]
        area += V[i][1] * V[(i + 1) % len(V)][0]
    area //= 2
    return area


def solve(part2=False):
    V = get_verts(part2)
    A = shoelace(V)
    P = len(V) // 2 + 1
    print(A + P)


solve()
solve(True)
