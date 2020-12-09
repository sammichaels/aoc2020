"""This file is part of Advent of Code 2020.

Coded by: Samuel Michaels (samuel.michaels@protonmail.com)
8 December 2020

NO COPYRIGHT
This work is dedicated to the public domain.  All rights have been
waived worldwide under copyright law, including all related and
neighboring rights, to the extent allowed by law.

You may copy, modify, distribute, and perform the work, even for
commercial purposes, all without asking permission.  See the
accompanying COPYRIGHT document."""

from pathlib import Path
from enum import IntEnum
from typing import Union


class CPUInstr(IntEnum):
    NOP = 0
    ACC = 1
    JMP = 2


# translation from text to op code
cpu_instr = {'nop': CPUInstr.NOP,
             'acc': CPUInstr.ACC,
             'jmp': CPUInstr.JMP}


class NXMemoryError(Exception):
    """Raised when program counter goes into no-execute memory"""
    pass


class CPU:
    __slots__ = ('_ram', '_memory', '_accumulator', '_pc', '_op_table', '_pgmsize')

    def __init__(self, ram: int = 2**17):
        assert isinstance(ram, int)
        if ram & (ram - 1) != 0:
            raise ValueError('ram size must be a power of 2')
        self._ram = ram
        self._memory = [0 for _ in range(self._ram)]
        self._accumulator = 0
        self._pc = 0
        self._pgmsize = 0
        self._op_table = {CPUInstr.ACC: self._op_acc,
                          CPUInstr.JMP: self._op_jmp}

        self.reset()

    def reset(self) -> None:
        self._accumulator = 0
        self._pc = 0

    def load_string(self, s: Union[list[str], str]) -> None:
        if isinstance(s, str):
            s = s.split('\n')
        elif not isinstance(s, list):
            raise TypeError('argument must be of type str')
        mem = 0
        for line in s:
            line = line.split(' ')
            op = line[0]
            arg = line[1]
            self._memory[mem] = cpu_instr.get(op, 0)
            mem += 1
            self._memory[mem] = int(arg)
            mem += 1
        self._pgmsize = (len(s) * 2) - 1

    def accumulator(self) -> int:
        return self._accumulator

    def pc(self) -> int:
        return self._pc

    def pgm_size(self) -> int:
        return self._pgmsize

    def peek(self, pos: int) -> int:
        if not 0 <= pos < self._ram:
            raise ValueError(f'peek outside of memory range 0 - {self._ram - 1}, got {pos}')
        return self._memory[pos]

    def poke(self, pos: int, val: int) -> None:
        if not 0 <= pos < self._ram:
            raise ValueError(f'poke outside of memory range 0 - {self._ram - 1}, got {pos}')
        self._memory[pos] = val

    def _op_acc(self) -> None:
        self._accumulator += self._memory[self._pc]
        self._pc += 1

    def _op_jmp(self) -> None:
        self._pc += ((self._memory[self._pc] - 1) * 2) + 1

    def step(self) -> None:
        if self._pc > self._pgmsize:
            raise NXMemoryError
        op = CPUInstr(self._memory[self._pc])
        self._pc += 1
        opfunc = self._op_table.get(op, None)
        if callable(opfunc):
            opfunc()
        else:
            # nop or unknown
            self._pc += 1


def part1(cpu: CPU) -> int:
    visited = []
    while cpu.pc() not in visited:
        visited.append(cpu.pc())
        cpu.step()
    return cpu.accumulator()


def part2(cpu: CPU) -> int:
    pos = 0
    while pos <= cpu.pgm_size():
        cpu.reset()
        if cpu.peek(pos) == CPUInstr.NOP:
            cpu.poke(pos, CPUInstr.JMP)
        elif cpu.peek(pos) == CPUInstr.JMP:
            cpu.poke(pos, CPUInstr.NOP)
        else:
            pos += 2
            continue
        try:
            part1(cpu)
        except NXMemoryError:
            # program has terminated
            return cpu.accumulator()
        # undo
        if cpu.peek(pos) == CPUInstr.NOP:
            cpu.poke(pos, CPUInstr.JMP)
        elif cpu.peek(pos) == CPUInstr.JMP:
            cpu.poke(pos, CPUInstr.NOP)
        pos += 2
    return 0


if __name__ == '__main__':
    data = list(map(str.rstrip, Path('input.txt').open('r').readlines()))
    gamecpu = CPU()
    gamecpu.load_string(data)
    print(f'Accumulator: {part1(gamecpu)}')
    print(f'Accumulator: {part2(gamecpu)}')

# EOF
