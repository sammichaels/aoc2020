"""This file is part of Advent of Code 2020.

Coded by: Samuel Michaels (samuel.michaels@protonmail.com)
9 December 2020

NO COPYRIGHT
This work is dedicated to the public domain.  All rights have been
waived worldwide under copyright law, including all related and
neighboring rights, to the extent allowed by law.

You may copy, modify, distribute, and perform the work, even for
commercial purposes, all without asking permission.  See the
accompanying COPYRIGHT document."""

from itertools import combinations
from pathlib import Path


def part1(nums: list[str], preamble: int) -> int:
    nums = list(map(int, nums))
    pos = preamble
    llen = len(nums)
    while pos <= llen:
        sums = list(map(sum, combinations(nums[pos - preamble:pos], 2)))
        if nums[pos] not in sums:
            return nums[pos]
        pos += 1
    return 0


def part2(nums: list[str], weak: int) -> int:
    nums = list(map(int, nums))
    maxpos = nums.index(weak)
    candidates = nums[0:maxpos]
    for pos in range(maxpos+1):
        for spos in range(pos + 1, maxpos+1, 1):
            if weak == sum(candidates[pos:spos]):
                return min(candidates[pos:spos]) + max(candidates[pos:spos])


if __name__ == '__main__':
    data = list(map(str.rstrip, Path('input.txt').open('r').readlines()))
    print(f'Weakness: {part1(data, 25)}')
    print(f'Weakness: {part2(data, part1(data, 25))}')
# EOF
