import re


def display(points):
    x0 = min(p[0] for p in points)
    y0 = min(p[1] for p in points)

    x1 = max(p[0] for p in points)
    y1 = max(p[1] for p in points)

    if x1 - x0 > 80 or y1 - y0 > 80:
        return

    points = set((point[0], point[1]) for point in points)

    rows = []
    for y in range(y0, y1 + 1):
        row = ""
        for x in range(x0, x1 + 1):
            if (x, y) in points:
                row += "X"
            else:
                row += "."
        rows.append(row)

    return "\n".join(rows)


def solve(points):
    seconds = 0

    while True:
        for point in points:
            x, y, vX, vY = point
            point[0] += vX
            point[1] += vY

        seconds += 1
        output = display(points)

        if output:
            print("Second: %d" % seconds)
            print(output)
            print("=" * 100)


with open('../input/day10.txt', 'r') as f:
    points = [list(map(int, re.findall(r"[-]?[\d]+", line))) for line in f]

solve(points)
