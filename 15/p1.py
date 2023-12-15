import sys

D = open(sys.argv[1]).read()


def h(word, p2=False):
    res, i = 0, 0
    while i < len(word):
        if word[i] in ["=", "-"] and p2:
            break
        val = ord(word[i])
        res += val
        res *= 17
        res %= 256
        i += 1
    return (res, word[i]) if p2 else res


HMAP = {}


def f(word):
    key, op = h(word, 1)
    label, value = word.split(op)
    if op == "-":
        if key in HMAP.keys():
            lenses = HMAP[key]
            if label in lenses.keys():
                del lenses[label]
    if op == "=":
        if key in HMAP.keys():
            lenses = HMAP[key]
            if label in lenses.keys():
                lenses[label] = (value, lenses[label][1])
            else:
                orders = [lenses[label][1] for label in lenses.keys()]
                if len(orders) == 0:
                    order = 0
                else:
                    order = max(orders) + 1
                lenses[label] = (value, order)
        else:
            lenses = {}
            lenses[label] = (value, 0)
            HMAP[key] = lenses


def score():
    ans = 0
    for key in HMAP.keys():
        box = key + 1
        lenses = [HMAP[key][lense] for lense in HMAP[key]]
        lenses = sorted(lenses, key=lambda x: x[1])
        order = 0
        for lense in lenses:
            order += 1
            print(box, order, lense)
            ans += box * order * int(lense[0])
    return ans


def solve():
    print(sum([h(word) for word in D.split(",")]))
    for word in D.split(","):
        f(word)
    for key in HMAP.keys():
        print(HMAP[key])
    print(score())


solve()
