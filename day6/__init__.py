"""This file is part of Advent of Code 2020.

Coded by: Samuel Michaels (samuel.michaels@protonmail.com)
6 December 2020

NO COPYRIGHT
This work is dedicated to the public domain.  All rights have been
waived worldwide under copyright law, including all related and
neighboring rights, to the extent allowed by law.

You may copy, modify, distribute, and perform the work, even for
commercial purposes, all without asking permission.  See the
accompanying COPYRIGHT document."""

from pathlib import Path


def part1(answers: list[str]) -> int:
    questions = []
    qsum = 0
    for a in answers:
        if a == '\n':
            qsum += len(questions)
            questions.clear()
        else:
            a = a.rstrip()
            questions += [q for q in a if q not in questions]
    return qsum + len(questions)


def part2(answers: list[str]) -> int:
    questions = []
    qsum = 0
    for a in answers:
        if a == '\n':
            qsum += len(set.intersection(*questions))
            questions.clear()
        else:
            a = a.rstrip()
            questions += [set(a)]
    return qsum + len(set.intersection(*questions))


if __name__ == '__main__':
    data = Path('input.txt').open('r').readlines()
    print(f'Sum any: {part1(data)}')
    print(f'Sum all: {part2(data)}')

# EOF
