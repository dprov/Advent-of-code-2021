from typing import List, Union

import numpy as np


def read_file_lines(path: str) -> List[str]:
    with open(path) as f:
        data = f.read()
        return data.split("\n")
