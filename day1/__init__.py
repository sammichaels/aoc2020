import datetime
import operator
from functools import reduce
from itertools import combinations
from pathlib import Path
from typing import List


def part1(exp: List) -> str:
    """Specifically, they need you to find the two entries that sum to 2020
    and then multiply those two numbers together."""

    for a in exp:
        for b in exp[1:]:
            if a + b == 2020:
                return f'Found: {a * b}'


def part2(exp: List) -> str:
    """They offer you a second one if you can find three numbers
    in your expense report that meet the same criteria."""

    for a in exp:
        for b in exp[1:]:
            for c in exp[2:]:
                if a + b + c == 2020:
                    return f'Found: {a * b * c}'


def newpart(exp: List, depth: int) -> str:
    """After peeking at other solutions, the best thing to do is use itertools/functools.
    Interesting that a depth of 2 is slower using this method."""

    for e in combinations(exp, depth):
        if sum(e) == 2020:
            return f'Found {reduce(operator.mul, e)}'


if __name__ == '__main__':
    explist = [int(e) for e in Path('input.txt').open('r').readlines()]
    start = datetime.datetime.utcnow()
    print(part1(explist))
    end = datetime.datetime.utcnow() - start
    print(f'Run time: {end.total_seconds()}')

    start = datetime.datetime.utcnow()
    print(part2(explist))
    end = datetime.datetime.utcnow() - start
    print(f'Run time: {end.total_seconds()}')

    start = datetime.datetime.utcnow()
    print(newpart(explist, 2))
    end = datetime.datetime.utcnow() - start
    print(f'Run time: {end.total_seconds()}')

    start = datetime.datetime.utcnow()
    print(newpart(explist, 3))
    end = datetime.datetime.utcnow() - start
    print(f'Run time: {end.total_seconds()}')

# EOF
