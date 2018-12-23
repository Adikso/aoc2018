import numpy


def parse(lines):
    area = numpy.zeros((len(lines) + 2, len(lines[0]) + 2))

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "|":
                area[y + 1, x + 1] = 2
            elif lines[y][x] == "#":
                area[y + 1, x + 1] = 1
    return area


def display(area):
    rows = []
    for y in range(area.shape[0]):
        row = []
        for x in range(area.shape[1]):
            if area[y, x] == 2:
                row.append("|")
            elif area[y, x] == 1:
                row.append("#")
            else:
                row.append(".")
        rows.append("".join(row))

    print("\n".join(rows))
    print("=============")


def count(area, x, y):
    counts = {0: 0, 1: 0, 2: 0}

    counts[area[y - 1, x]] += 1
    counts[area[y + 1, x]] += 1
    counts[area[y, x + 1]] += 1
    counts[area[y, x - 1]] += 1
    counts[area[y - 1, x - 1]] += 1
    counts[area[y - 1, x + 1]] += 1
    counts[area[y + 1, x - 1]] += 1
    counts[area[y + 1, x + 1]] += 1

    return counts

def solve(area, target, f=0):
    history = []
    counter = 0
    start = 0
    seq = []
    seqr = []

    for m in range(f, target):
        next = area.copy()
        for y in range(1, area.shape[0] - 1):
            for x in range(1, area.shape[1] - 1):
                counts = {0: 0, 1: 0, 2: 0}

                counts[area[y - 1, x]] += 1
                counts[area[y + 1, x]] += 1
                counts[area[y, x + 1]] += 1
                counts[area[y, x - 1]] += 1
                counts[area[y - 1, x - 1]] += 1
                counts[area[y - 1, x + 1]] += 1
                counts[area[y + 1, x - 1]] += 1
                counts[area[y + 1, x + 1]] += 1

                if area[y, x] == 0 and counts[2] >= 3:
                    next[y, x] = 2

                if area[y, x] == 2 and counts[1] >= 3:
                    next[y, x] = 1

                if area[y, x] == 1:
                    if counts[1] >= 1 and counts[2] >= 1:
                        next[y, x] = 1
                    else:
                        next[y, x] = 0

        area = next
        if f == 0:
            if area.tostring() in history:
                if len(seq) != 0 and seq[counter] == area.tostring():
                    if counter == 0:
                        start = len(seq)
                    counter += 1

                seq.append(area.tostring())
                seqr.append(area)
            else:
                counter = 0
                seq = []
                seqr = []
                start = 0
                history.append(area.tostring())

            if start != 0 and start == counter:
                xd = m + len(seqr[:start]) * int((target - m) / len(seqr[:start])) + 1
                return solve(area, target, xd)

    return (area == 2).sum() * (area == 1).sum()


def main():
    with open('../input/day18.txt', 'r') as f:
        lines = [x.strip() for x in f.readlines()]

    print("Part One: %d" % solve(parse(lines), 10))
    print("Part Two: %d" % solve(parse(lines), 1000000000))


if __name__ == '__main__':
    main()
