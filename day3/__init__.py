"""This file is part of Advent of Code 2020.

Coded by: Samuel Michaels (samuel.michaels@protonmail.com)
3 December 2020

NO COPYRIGHT
This work is dedicated to the public domain.  All rights have been
waived worldwide under copyright law, including all related and
neighboring rights, to the extent allowed by law.

You may copy, modify, distribute, and perform the work, even for
commercial purposes, all without asking permission.  See the
accompanying COPYRIGHT document."""

import operator
from functools import reduce
from pathlib import Path
from typing import List, Tuple


def part1(smap: List[str], right: int, down: int) -> int:
    repeatlen = len(smap[0].rstrip())
    maplen = len(smap)
    rpos = 0
    dpos = 0
    trees = 0
    while dpos < maplen - down:
        rpos += right
        dpos += down
        if smap[dpos][rpos % repeatlen] == '#':
            trees += 1
    return trees


def part2(smap: List[str], slopes: Tuple) -> int:
    trees = [part1(smap, s[0], s[1]) for s in slopes]
    return reduce(operator.mul, trees)


if __name__ == '__main__':
    sledmap = Path('input.txt').open('r').readlines()
    print(f'Trees: {part1(sledmap, 3, 1)}')
    print(f'Trees: {part2(sledmap, ((1,1),(3,1),(5,1),(7,1),(1,2)))}')

# EOF
