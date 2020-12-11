"""This file is part of Advent of Code 2020.

Coded by: Samuel Michaels (samuel.michaels@protonmail.com)
11 December 2020

NO COPYRIGHT
This work is dedicated to the public domain.  All rights have been
waived worldwide under copyright law, including all related and
neighboring rights, to the extent allowed by law.

You may copy, modify, distribute, and perform the work, even for
commercial purposes, all without asking permission.  See the
accompanying COPYRIGHT document."""

from collections import deque
from pathlib import Path


def part1(s: list[str]) -> int:
    cols = len(s[0])
    rows = len(s)
    seats = []
    [seats.extend(list(x)) for x in s]
    changes = True
    while changes:
        oldseats = seats.copy()
        changes = False
        for pos in range(cols * rows):
            r = pos // cols
            c = pos % cols
            if oldseats[pos] == '.':
                continue
            occ = 0
            if oldseats[pos] == 'L':
                # ROW ABOVE
                if r > 0:
                    if c > 0:
                        if oldseats[((r - 1) * cols) + c - 1] == '#':
                            occ += 1
                    if oldseats[((r - 1) * cols) + c] == '#':
                        occ += 1
                    if c < cols - 1:
                        if oldseats[((r - 1) * cols) + c + 1] == '#':
                            occ += 1
                # THIS ROW
                if c > 0:
                    if oldseats[pos - 1] == '#':
                        occ += 1
                if c < cols - 1:
                    if oldseats[pos + 1] == '#':
                        occ += 1
                # ROW BELOW
                if r < rows - 1:
                    if c > 0:
                        if oldseats[((r + 1) * cols) + c - 1] == '#':
                            occ += 1
                    if oldseats[((r + 1) * cols) + c] == '#':
                        occ += 1
                    if c < cols - 1:
                        if oldseats[((r + 1) * cols) + c + 1] == '#':
                            occ += 1
                if occ == 0:
                    seats[pos] = '#'
                    changes = True
            occ = 0
            if oldseats[pos] == '#':
                # ROW ABOVE
                if r > 0:
                    if c > 0:
                        if oldseats[((r - 1) * cols) + c - 1] == '#':
                            occ += 1
                    if oldseats[((r - 1) * cols) + c] == '#':
                        occ += 1
                    if c < cols - 1:
                        if oldseats[((r - 1) * cols) + c + 1] == '#':
                            occ += 1
                # THIS ROW
                if c > 0:
                    if oldseats[pos - 1] == '#':
                        occ += 1
                if c < cols - 1:
                    if oldseats[pos + 1] == '#':
                        occ += 1
                # ROW BELOW
                if r < rows - 1:
                    if c > 0:
                        if oldseats[((r + 1) * cols) + c - 1] == '#':
                            occ += 1
                    if oldseats[((r + 1) * cols) + c] == '#':
                        occ += 1
                    if c < cols - 1:
                        if oldseats[((r + 1) * cols) + c + 1] == '#':
                            occ += 1
                if occ >= 4:
                    seats[pos] = 'L'
                    changes = True
    return seats.count('#')


def part2(s: list[str]) -> int:
    cols = len(s[0])
    rows = len(s)
    seats = []
    [seats.extend(list(x)) for x in s]
    changes = True
    while changes:
        oldseats = seats.copy()
        changes = False
        for pos in range(cols * rows):
            r = pos // cols
            c = pos % cols
            if oldseats[pos] == '.':
                continue
            occ = 0
            if oldseats[pos] == 'L':
                # ROW ABOVE
                if r > 0:
                    if c > 0:
                        rt = r
                        ct = c
                        while rt > 0 and ct > 0:
                            if oldseats[((rt - 1) * cols) + ct - 1] == '#':
                                occ += 1
                                break
                            elif oldseats[((rt - 1) * cols) + ct - 1] == 'L':
                                break
                            rt -= 1
                            ct -= 1
                    rt = r
                    while rt > 0:
                        if oldseats[((rt - 1) * cols) + c] == '#':
                            occ += 1
                            break
                        elif oldseats[((rt - 1) * cols) + c] == 'L':
                            break
                        rt -= 1
                    if c < cols - 1:
                        rt = r
                        ct = c
                        while rt > 0 and ct < cols - 1:
                            if oldseats[((rt - 1) * cols) + ct + 1] == '#':
                                occ += 1
                                break
                            elif oldseats[((rt - 1) * cols) + ct + 1] == 'L':
                                break
                            rt -= 1
                            ct += 1
                # THIS ROW
                if c > 0:
                    ct = c
                    pt = pos
                    while ct > 0:
                        if oldseats[pt - 1] == '#':
                            occ += 1
                            break
                        elif oldseats[pt - 1] == 'L':
                            break
                        ct -= 1
                        pt -= 1
                if c < cols - 1:
                    ct = c
                    pt = pos
                    while ct < cols - 1:
                        if oldseats[pt + 1] == '#':
                            occ += 1
                            break
                        elif oldseats[pt + 1] == 'L':
                            break
                        ct += 1
                        pt += 1
                # ROW BELOW
                if r < rows - 1:
                    if c > 0:
                        ct = c
                        rt = r
                        while ct > 0 and rt < rows - 1:
                            if oldseats[((rt + 1) * cols) + ct - 1] == '#':
                                occ += 1
                                break
                            elif oldseats[((rt + 1) * cols) + ct - 1] == 'L':
                                break
                            ct -= 1
                            rt += 1
                    rt = r
                    while rt < rows - 1:
                        if oldseats[((rt + 1) * cols) + c] == '#':
                            occ += 1
                            break
                        elif oldseats[((rt + 1) * cols) + c] == 'L':
                            break
                        rt += 1
                    if c < cols - 1:
                        rt = r
                        ct = c
                        while rt < rows - 1 and ct < cols - 1:
                            if oldseats[((rt + 1) * cols) + ct + 1] == '#':
                                occ += 1
                                break
                            elif oldseats[((rt + 1) * cols) + ct + 1] == 'L':
                                break
                            rt += 1
                            ct += 1
                if occ == 0:
                    seats[pos] = '#'
                    changes = True
            occ = 0
            if oldseats[pos] == '#':
                # ROW ABOVE
                if r > 0:
                    if c > 0:
                        rt = r
                        ct = c
                        while rt > 0 and ct > 0:
                            if oldseats[((rt - 1) * cols) + ct - 1] == '#':
                                occ += 1
                                break
                            elif oldseats[((rt - 1) * cols) + ct - 1] == 'L':
                                break
                            rt -= 1
                            ct -= 1
                    rt = r
                    while rt > 0:
                        if oldseats[((rt - 1) * cols) + c] == '#':
                            occ += 1
                            break
                        elif oldseats[((rt - 1) * cols) + c] == 'L':
                            break
                        rt -= 1
                    if c < cols - 1:
                        rt = r
                        ct = c
                        while rt > 0 and ct < cols - 1:
                            if oldseats[((rt - 1) * cols) + ct + 1] == '#':
                                occ += 1
                                break
                            elif oldseats[((rt - 1) * cols) + ct + 1] == 'L':
                                break
                            rt -= 1
                            ct += 1
                # THIS ROW
                if c > 0:
                    ct = c
                    pt = pos
                    while ct > 0:
                        if oldseats[pt - 1] == '#':
                            occ += 1
                            break
                        elif oldseats[pt - 1] == 'L':
                            break
                        ct -= 1
                        pt -= 1
                if c < cols - 1:
                    ct = c
                    pt = pos
                    while ct < cols - 1:
                        if oldseats[pt + 1] == '#':
                            occ += 1
                            break
                        elif oldseats[pt + 1] == 'L':
                            break
                        ct += 1
                        pt += 1
                # ROW BELOW
                if r < rows - 1:
                    if c > 0:
                        ct = c
                        rt = r
                        while ct > 0 and rt < rows - 1:
                            if oldseats[((rt + 1) * cols) + ct - 1] == '#':
                                occ += 1
                                break
                            elif oldseats[((rt + 1) * cols) + ct - 1] == 'L':
                                break
                            ct -= 1
                            rt += 1
                    rt = r
                    while rt < rows - 1:
                        if oldseats[((rt + 1) * cols) + c] == '#':
                            occ += 1
                            break
                        elif oldseats[((rt + 1) * cols) + c] == 'L':
                            break
                        rt += 1
                    if c < cols - 1:
                        rt = r
                        ct = c
                        while rt < rows - 1 and ct < cols - 1:
                            if oldseats[((rt + 1) * cols) + ct + 1] == '#':
                                occ += 1
                                break
                            elif oldseats[((rt + 1) * cols) + ct + 1] == 'L':
                                break
                            rt += 1
                            ct += 1
                if occ >= 5:
                    seats[pos] = 'L'
                    changes = True
    return seats.count('#')


if __name__ == '__main__':
    data = list(map(str.rstrip, Path('input.txt').open('r').readlines()))
    testdata = ['L.LL.LL.LL',
                'LLLLLLL.LL',
                'L.L.L..L..',
                'LLLL.LL.LL',
                'L.LL.LL.LL',
                'L.LLLLL.LL',
                '..L.L.....',
                'LLLLLLLLLL',
                'L.LLLLLL.L',
                'L.LLLLL.LL']
    print(f'Occupied: {part1(data)}')
    print(f'Occupied: {part2(data)}')

# EOF
