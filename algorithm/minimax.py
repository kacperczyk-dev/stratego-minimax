from gamelogic import Board
from utils import TreeNode


def create_game_tree(size, root=None, depth=0, max_depth=0):
    if root is None:
        board = Board(size, 0)
        board.init_available_moves_and_board()
        root = TreeNode(board)
        create_game_tree(size, root, depth)
    else:
        #print('depth= ', depth)
        #print(len(root.data.availableMoves))
        print(root.data.playerMax, root.data.playerMin)
        board = root.data
        nextMove = board.make_next_move()
        if nextMove:
            create_game_tree(size, root.add_child(TreeNode(Board.from_board(board, nextMove))), depth+1)
        else:
            if root.parent:
                create_game_tree(size, root.parent, depth-1)
    return root


def minimax(root):
    return 111


def get_max(list_of_states):
    return 1


def get_min(list_of_states):
    return 0