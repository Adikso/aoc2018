def display(track, carts):
    w = max(len(line) for line in track)
    h = len(track)

    rows = []
    for y in range(h):
        row = []
        for x in range(w):
            l = track[y][x] if track[y][x] else " "

            for cart in carts:
                if cart[0] == (y, x):
                    l = cart[1]

            row.append(l)
        rows.append("".join(row))

    print("\n".join(rows))


def solve(track, carts):
    dirs = {
        "/": {
            ">": "^",
            "<": "v",
            "^": ">",
            "v": "<"
        },
        "\\": {
            ">": "v",
            "<": "^",
            "^": "<",
            "v": ">"
        }
    }

    cross = {
        0: {
            ">": "^",
            "<": "v",
            "^": "<",
            "v": ">"
        },
        1: {
            ">": ">",
            "<": "<",
            "^": "^",
            "v": "v"
        },
        2: {
            ">": "v",
            "<": "^",
            "^": ">",
            "v": "<"
        }
    }

    while True:
        carts = sorted(carts, key = lambda x: x[0])
        for cart in carts[:]:
            y, x = cart[0]

            if cart[1] == ">":
                x += 1
            elif cart[1] == "<":
                x -= 1
            elif cart[1] == "v":
                y += 1
            elif cart[1] == "^":
                y -= 1

            for c in carts:
                if c == cart:
                    continue

                if c[0] == (y, x):
                    print("CRASHED AT %d %d" % (x, y))
                    carts.remove(cart)
                    carts.remove(c)
                    # return

            if track[y][x] == "+":
                cart[1] = cross[cart[2]][cart[1]]
                cart[2] = (cart[2] + 1) % 3
            elif track[y][x] in ["/", "\\"]:
                cart[1] = dirs[track[y][x]][cart[1]]

            cart[0] = (y, x)

        if len(carts) == 1:
            print(carts[0])
            return

        # display(track, carts)


def parse(lines):
    width = max(len(line) for line in lines)
    height = len(lines)

    track = []
    carts = []

    for y in range(height):
        track.append([""] * width)
        for x in range(len(lines[y])):
            track[y][x] = lines[y][x]

            if lines[y][x] in [">", "<", "^", "v"]:
                carts.append([(y, x), lines[y][x], 0])
                track[y][x] = "-"

    return track, carts


def main():
    with open('/storage/emulated/0/qpython/day7.txt', 'r') as f:
        lines = [x.rstrip() for x in f.readlines()]

    track, carts = parse(lines)
    solve(track, carts)


if __name__ == '__main__':
    main()
