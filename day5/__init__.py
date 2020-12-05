"""This file is part of Advent of Code 2020.

Coded by: Samuel Michaels (samuel.michaels@protonmail.com)
5 December 2020

NO COPYRIGHT
This work is dedicated to the public domain.  All rights have been
waived worldwide under copyright law, including all related and
neighboring rights, to the extent allowed by law.

You may copy, modify, distribute, and perform the work, even for
commercial purposes, all without asking permission.  See the
accompanying COPYRIGHT document."""

from pathlib import Path


def part1(seats: list[str]) -> list[int]:
    seatlist = []
    """
    rows = frozenset(x for x in range(128))
    cols = frozenset(x for x in range(8))
    for s in seats:
        thisrow = list(rows)
        thiscol = list(cols)
        for ch in s:
            if ch == 'F':
                thisrow = thisrow[0:len(thisrow) // 2]
            elif ch == 'B':
                thisrow = thisrow[len(thisrow) // 2:]
            elif ch == 'R':
                thiscol = thiscol[len(thiscol) // 2:]
            elif ch == 'L':
                thiscol = thiscol[0:len(thiscol) // 2]
        seatlist.append(thisrow[0] * 8 + thiscol[0])
    """
    # original solution is above, then i realized this was binary
    for s in seats:
        row = int(s[0:7].replace('F', '0').replace('B', '1'), 2)
        col = int(s[7:].replace('L', '0').replace('R', '1'), 2)
        seatlist.append(row * 8 + col)
    return seatlist


def part2(seats: list[int]) -> int:
    seatset = set(seats)
    fullseatset = set(range(min(seats), max(seats), 1))
    return fullseatset.difference(seatset).pop()


if __name__ == '__main__':
    data = Path('input.txt').open('r').readlines()
    plane = part1(data)
    print(f'Highest seat id: {max(plane)}')
    print(f'Your seat: {part2(plane)}')

# EOF
