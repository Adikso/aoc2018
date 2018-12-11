import numpy


def process(serial):
    cells = numpy.zeros((300, 300))
    for y in range(1, 301):
        for x in range(1, 301):
            rackId = x + 10
            cells[y - 1, x - 1] = int((rackId * y + serial) * rackId / 100) % 10 - 5

    return cells


def part_one(serial):
    cells = process(serial)

    top_val = 0
    top = (0, 0)

    for y in range(0, 300 - 2):
        for x in range(0, 300 - 2):
            sum = cells[y, x] + cells[y, x + 1] + cells[y, x + 2] + cells[y + 1, x] + cells[y + 1, x + 1] + \
                  cells[y + 1, x + 2] + cells[y + 2, x] + cells[y + 2, x + 1] + cells[y + 2, x + 2]
            if sum > top_val:
                top_val = sum
                top = (x + 1, y + 1)

    return top, top_val


# Bruteforce solution
def part_two(serial):
    cells = process(serial)

    top_val = 0
    top_size = 0
    top = (0, 0)

    for y in range(0, 300 - 2):
        print(y)
        for x in range(0, 300 - 2):
            s = 0
            for i in range(0, min(298 - x, 298 - y)):
                s += sum(c for c in cells[y + i, x:x+i+1]) + sum(c for c in cells[y:y+i, x + i])

                if s > top_val:
                    top_val = s
                    top_size = i
                    top = (x + 1, y + 1)

    return top, top_val, top_size + 1


def main():
    with open('../input/day11.txt', 'r') as f:
        serial = int(f.readline())

    print(part_one(serial))
    print(part_two(serial))


if __name__ == '__main__':
    main()
