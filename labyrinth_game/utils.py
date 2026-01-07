from typing import List, Tuple

def print_maze(maze: List[List[str]]) -> None:
    for row in maze:
        print("".join(row))

def find_player(maze: List[List[str]]) -> Tuple[int, int]:
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == "P":
                return i, j
    raise ValueError("Player not found")