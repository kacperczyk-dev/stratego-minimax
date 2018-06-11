from algorithm import minimax
import sys


def start_game():
    sys.setrecursionlimit(11000)
    boardSize = 3
    root = minimax(boardSize)
    print(len(root.children))


if __name__ == "__main__":
    start_game()
