from typing import List

from labyrinth_game.constants import EMPTY, MOVES, PLAYER, TREASURE, WALL
from labyrinth_game.utils import find_player

def move_player(maze: List[List[str]], direction: str) -> bool:
    if direction not in MOVES:
        return False

    x, y = find_player(maze)
    dx, dy = MOVES[direction]
    nx, ny = x + dx, y + dy

    if maze[nx][ny] == WALL:
        return False

    if maze[nx][ny] == TREASURE:
        maze[x][y] = EMPTY
        maze[nx][ny] = PLAYER
        return True

    maze[x][y] = EMPTY
    maze[nx][ny] = PLAYER
    return False