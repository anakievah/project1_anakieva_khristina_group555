from labyrinth_game.constants import (
    QUIT,
)
from labyrinth_game.player_actions import move_player
from labyrinth_game.utils import print_maze

def main() -> None:
    maze = [
        list("########"),
        list("#P     #"),
        list("# ###T #"),
        list("#   #  #"),
        list("### #E##"),
        list("#      #"),
        list("########"),
    ]

    print("Лабиринт сокровищ")
    print("Управление: w a s d, выход — q")

    while True:
        print_maze(maze)
        command = input("Ход: ").lower()

        if command == QUIT:
            print("Выход из игры")
            break

        found = move_player(maze, command)
        if found:
            print("Сокровище найдено!")
            break

if __name__ == "__main__":
    main()