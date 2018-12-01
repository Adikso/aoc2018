from functools import reduce


def part_one(freqs: list):
    return reduce(lambda a, b: a + b, freqs)


def part_two(freqs: list):
    freq = 0
    prev_freqs = set()

    while True:
        for diff in freqs:
            freq += diff

            if freq in prev_freqs:
                return freq

            prev_freqs.add(freq)


def main():
    with open('../input/day1.txt', 'r') as f:
        freqs = [int(i) for i in f.readlines()]

    print("Part One: %d" % part_one(freqs))
    print("Part Two: %d" % part_two(freqs))


if __name__ == "__main__":
    main()
