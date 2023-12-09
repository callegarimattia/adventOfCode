D = open("day9/input.txt").read().strip()
H = [L.split() for L in D.split("\n")]
for i in range(len(H)):
    H[i] = [int(h) for h in H[i]]


def get_diff(h, q):
    ds = []
    for i in range(len(h) - 1):
        ds.append(h[i + 1] - h[i])
    if all(d == 0 for d in ds):
        return ds, q
    else:
        q.append(ds)
        return get_diff(ds, q)


def calc(h, q):
    ds, q = get_diff(h, q)
    s = 0
    for t in q:
        s += t[-1]
    s += h[-1]
    return s


def calc2(h, q):
    ds, q = get_diff(h, q)
    s = 0
    for t in q[::-1]:
        s = t[0] - s
        print(s, t)
    s = h[0] - s
    return s


def solve(part2):
    s = 0
    for h in H:
        q = []
        s += calc(h, q) if not part2 else calc2(h, q)
    return s


print(solve(False))
print(solve(True))
