from algorithm import create_game_tree
import sys


def start_game():
    sys.setrecursionlimit(11000)
    boardSize = 3
    gameTree = create_game_tree(boardSize)
    #print(len(gameTree.children))


if __name__ == "__main__":
    start_game()
