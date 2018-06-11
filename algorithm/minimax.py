from gamelogic import Board
from utils import TreeNode


def minimax(size, root=None, depth=0):
    if root is None:
        board = Board(size, 1)
        root = TreeNode(board)
        minimax(size, root, depth)
    else:
        print('depth= ', depth)
        #print(len(root.data.availableMoves))
        board = root.data
        nextMove = board.make_next_move()
        if nextMove:
            minimax(size, root.add_child(TreeNode(Board.from_board(board, nextMove))), depth+1)
        else:
            if root.parent:
                minimax(size, root.parent, depth+1)
    return root