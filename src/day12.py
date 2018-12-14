import time


def solve(state, patterns, generation):
    prev_offset = 0
    offset = -5
    last = ""

    for j in range(1, generation + 1):
        next = list("." * len(state))

        for i in range(0, len(state)):
            if state[i:i + 5] in patterns.keys():
                next[i + 2] = "#" if patterns[state[i:i + 5]] else "."

        stripped = "".join(next).lstrip(".")
        prev_offset = offset

        offset -= 5 - (len(next) - len(stripped))
        state = "....." + stripped.rstrip(".") + "....."

        if state == last:
            prev_offset -= (abs(prev_offset) - abs(offset)) * (generation - j)
            break

        last = state

    offset = prev_offset
    sum = 0

    for i in range(len(next)):
        if next[i] == "#":
            sum += i + offset

    return sum


def main():
    start_time = time.time()
    with open('../input/day12.txt', 'r') as f:
        lines = [x.rstrip() for x in f.readlines()]

    initial = "....." + lines[0].split(": ")[1].strip() + "....."
    patterns = {}

    for i in range(2, len(lines)):
        entry = list(lines[i].split(" => "))
        patterns[entry[0]] = entry[1] == "#"

    print("Part One: %d" % solve(initial, patterns, 20))
    print("Part Two: %d" % solve(initial, patterns, 50000000000))
    print(time.time() - start_time)


if __name__ == '__main__':
    main()
