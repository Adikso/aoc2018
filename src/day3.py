import re
import numpy


def solve(cuts: list):
    fabric = numpy.zeros((1000, 1000))

    for (id, left, top, width, height) in cuts:
        fabric[left:left + width, top:top + height] += 1

    found_id = -1
    for (id, left, top, width, height) in cuts:
        if (fabric[left:left + width, top:top + height] == 1).all():
            found_id = id

    return (fabric > 1).sum(), found_id


def main():
    with open('../input/day3.txt', 'r') as f:
        cuts = [tuple(map(int, re.findall(r"[\d]+", line))) for line in f]

    print("Part One: %d\nPart Two: %d" % solve(cuts))


if __name__ == '__main__':
    main()
