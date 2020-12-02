"""This file is part of Advent of Code 2020.

Coded by: Samuel Michaels (samuel.michaels@protonmail.com)
2 December 2020

NO COPYRIGHT
This work is dedicated to the public domain.  All rights have been
waived worldwide under copyright law, including all related and
neighboring rights, to the extent allowed by law.

You may copy, modify, distribute, and perform the work, even for
commercial purposes, all without asking permission.  See the
accompanying COPYRIGHT document."""

import re
from pathlib import Path
from typing import List


def part1(plist: List) -> List:
    occur_re = re.compile(r'^(\d+)-(\d+)$')
    validlist = []
    for p in plist:
        ch = p[1][0]                    # remove colon
        occur = occur_re.match(p[0])    # regex match
        occur_lower = int(occur[1])     # group 1 match
        occur_upper = int(occur[2])     # group 2 match
        occ = p[2].count(ch)            # str.count() for occurences
        if occur_lower <= occ <= occur_upper:
            validlist.append(p)
    return validlist


def part2(plist: List) -> List:
    occur_re = re.compile(r'^(\d+)-(\d+)$')
    validlist = []
    for p in plist:
        ch = p[1][0]                    # remove colon
        occur = occur_re.match(p[0])    # regex match
        occur_lower = int(occur[1])     # group 1 match
        occur_upper = int(occur[2])     # group 2 match
        if (p[2][occur_lower - 1] == ch) ^ (p[2][occur_upper - 1] == ch):
            validlist.append(p)
    return validlist


if __name__ == '__main__':
    passlist = [e.split(' ') for e in Path('input.txt').open('r').readlines()]
    valid = part1(passlist)
    print(f'Found {len(valid)} valid part 1 passwords.')

    valid = part2(passlist)
    print(f'Found {len(valid)} valid part 2 passwords.')

# EOF
