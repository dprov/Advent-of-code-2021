import copy
from dataclasses import dataclass
from enum import Enum
from typing import List, Type

import utils.io


class Position:
    x: int = 0
    depth: int = 0
    aim: int = 0


class Direction(Enum):
    Forward = "forward"
    Up = "up"
    Down = "down"


@dataclass
class Move:
    direction: Direction
    distance: int

    def apply(self, pos: Position) -> Position:
        out_pos = copy.deepcopy(pos)
        if self.direction == Direction.Forward:
            out_pos.x += self.distance
            out_pos.depth += out_pos.aim * self.distance
        elif self.direction == Direction.Down:
            out_pos.aim += self.distance
        elif self.direction == Direction.Up:
            out_pos.aim -= self.distance
        else:
            NotImplementedError()
        return out_pos


@dataclass
class WrongMove(Move):
    def apply(self, pos: Position) -> Position:
        out_pos = copy.deepcopy(pos)
        if self.direction == Direction.Forward:
            out_pos.x += self.distance
        elif self.direction == Direction.Down:
            out_pos.depth += self.distance
        elif self.direction == Direction.Up:
            out_pos.depth -= self.distance
        else:
            NotImplementedError()
        return out_pos


@dataclass
class Submarine:
    # position: Position = field(default_factory=lambda: Position())
    position = Position()

    def move(self, moves: List[Move]) -> None:
        for move in moves:
            # self.position =
            self.position = move.apply(self.position)

    def get_position_score(self) -> int:
        return self.position.x * self.position.depth


def parse_input(path: str, move_type: Type = Move) -> List[Move]:
    data = utils.io.read_file_lines(path)
    data = [line.split(" ") for line in data]

    return [move_type(direction=Direction(line[0]), distance=int(line[1])) for line in data]


def solve_submarine_motion(move_type: Type = Move) -> int:
    moves = parse_input("input/day2", move_type=move_type)
    submarine = Submarine()
    submarine.move(moves)
    return submarine.get_position_score()


if __name__ == "__main__":
    print("Part I")
    print(solve_submarine_motion(WrongMove))

    print("Part II")
    print(solve_submarine_motion(Move))
