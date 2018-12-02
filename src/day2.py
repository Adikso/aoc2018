from collections import Counter


def part_one(ids: list):
    twice_counts = 0
    three_counts = 0

    for id in ids:
        c = Counter(id)

        three_counts += 1 if 3 in c.values() else 0
        twice_counts += 1 if 2 in c.values() else 0

    return twice_counts * three_counts


def part_two(ids: list):
    for id in ids:
        for cid in ids:
            if id == cid:
                continue

            diff = [i for i in range(len(id)) if id[i] != cid[i]]

            if len(diff) == 1:
                return id[:diff[0]] + id[diff[0] + 1:]

    return None


def main():
    with open('../input/day2.txt', 'r') as f:
        ids = [line.rstrip() for line in f]

    print("Part One: %d" % part_one(ids))
    print("Part Two: %s" % part_two(ids))


if __name__ == '__main__':
    main()
