"""This file is part of Advent of Code 2020.

Coded by: Samuel Michaels (samuel.michaels@protonmail.com)
4 December 2020

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

REQUIRED_FIELDS = (('byr', re.compile(r'^(19[2-8][0-9]|199[0-9]|200[0-2])$')),
                   ('iyr', re.compile(r'^(201[0-9]|2020)$')),
                   ('eyr', re.compile(r'^(202[0-9]|2030)$')),
                   ('hgt', re.compile(r'^((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)$')),
                   ('hcl', re.compile(r'^#[0-9a-f]{6}$')),
                   ('ecl', re.compile(r'^(amb|blu|brn|gry|grn|hzl|oth)$')),
                   ('pid', re.compile(r'^\d{9}$')))


def part1(passports: List[str]) -> List[dict]:
    pplist = []
    for pp in passports:
        pp = pp.replace('\n', ' ').split(' ')
        thisdict = {}
        valid = True
        for field in pp:
            fsplit = field.split(':')
            thisdict[fsplit[0]] = fsplit[1]
        for req in REQUIRED_FIELDS:
            if req[0] not in thisdict:
                valid = False
        if valid:
            pplist.append(thisdict)
    return pplist


def part2(passports: List[dict]) -> List[dict]:
    pplist = []
    for pp in passports:
        valid = True
        for req in REQUIRED_FIELDS:
            if not req[1].match(pp.get(req[0], '')):
                valid = False
        if valid:
            pplist.append(pp)
    return pplist


if __name__ == '__main__':
    data = ''.join(Path('input.txt').open('r').readlines()).split('\n\n')
    p1 = part1(data)
    print(f'Valid passports: {len(p1)}')
    print(f'Valid passports: {len(part2(p1))}')

# EOF
