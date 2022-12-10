from typing import List

import utils


def parse_input(path: str) -> List[int]:
    readings = utils.io.read_file_lines(path)
    return [int(line) for line in readings]


def count_deeper_readings(readings: List[int], win_len: int = 1) -> int:
    # The difference of adjacent sliding windows will differ only by
    # (last - first) elements (i.e. those that are part of just 1 window)

    # Ends where sliding window is incomplete + beginning where there is no previous
    # data are ignored
    is_deeper = [r2 > r1 for r1, r2 in zip(readings[:-win_len], readings[win_len:])]
    return sum(is_deeper)


if __name__ == "__main__":
    readings = parse_input("input/day1")

    print("Part I")
    print(count_deeper_readings(readings, win_len=1))

    print("Part II")
    print(count_deeper_readings(readings, win_len=3))
