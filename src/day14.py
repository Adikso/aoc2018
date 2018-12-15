from blist import blist


def part_one(amount):
    amount = int(amount)
    e1 = 0
    e2 = 1
    recipes = [3, 7]

    for i in range(amount + 6):
        n = recipes[e1] + recipes[e2]

        if n > 9:
            recipes.append(int(n / 10))

        recipes.append(int(n % 10))

        e1 = (e1 + recipes[e1] + 1) % len(recipes)
        e2 = (e2 + recipes[e2] + 1) % len(recipes)

    return "".join([str(x) for x in recipes[amount:amount + 10]])


def part_two(scores):
    scores = [int(x) for x in scores]

    e1 = 0
    e2 = 1
    recipes = blist([3, 7])

    while recipes[-len(scores):] != scores and recipes[-len(scores)-1:-1] != scores:
        n = recipes[e1] + recipes[e2]

        if n > 9:
            recipes.append(int(n / 10))

        recipes.append(int(n % 10))

        e1 = (e1 + recipes[e1] + 1) % len(recipes)
        e2 = (e2 + recipes[e2] + 1) % len(recipes)

    if recipes[-len(scores):] == scores:
        return len(recipes) - len(scores)

    if recipes[-len(scores) - 1:-1] == scores:
        return len(recipes) - len(scores) - 1


def main():
    with open('../input/day14.txt', 'r') as f:
        amount = f.readline().strip()

    print("Part One: %s" % part_one(amount))
    print("Part Two: %d" % part_two(amount))


if __name__ == '__main__':
    main()
