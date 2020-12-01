from pathlib import Path


def part1():
    """Specifically, they need you to find the two entries that sum to 2020
    and then multiply those two numbers together."""
    exp = [int(e) for e in Path('input.txt').open('r').readlines()]

    shouldbreak = False

    for a in exp:
        for b in exp[1:]:
            if a + b == 2020:
                print(f'Found: {a * b}')
                shouldbreak = True
        if shouldbreak:
            break


def part2():
    """They offer you a second one if you can find three numbers
    in your expense report that meet the same criteria."""
    exp = [int(e) for e in Path('input.txt').open('r').readlines()]

    shouldbreak = False

    for a in exp:
        for b in exp[1:]:
            for c in exp[2:]:
                if a + b + c == 2020:
                    print(f'Found: {a * b * c}')
                    shouldbreak = True
            if shouldbreak:
                break
        if shouldbreak:
            break


if __name__ == '__main__':
    part1()
    part2()

# EOF
