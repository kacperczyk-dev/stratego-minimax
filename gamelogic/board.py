
class Board(object):

    def __init__(self, size, who, move=-1):
        self.size = size
        self.availableMoves = []
        self.playerOneScore = 0
        self.playerTwoScore = 0
        self.who = who
        self.lastMove = move
        if move == -1:
            self.board = [[0 for i in range(size)] for j in range(size)]
            self.init_available_moves()

    @classmethod
    def from_board(cls, board, move):
        size = board.size
        who = 1 if board.who == 2 else 2
        newBoard = cls(size, who, move)
        newBoard.board = [x[:] for x in board.board]
        newBoard.board[move[0]][move[1]] = 1
        newBoard.availableMoves = [x[:] for x in board.availableMoves]
        #PRINT----------------------------------------------
        #print(len(newBoard.availableMoves))
        #---------------------------------------------------
        return newBoard

    def make_next_move(self):
        if len(self.availableMoves) > 0:
            return self.availableMoves.pop()
        else:
            return []

    def init_available_moves(self):
        for i in range(self.size):
            for j in range(self.size):
                self.availableMoves.append([i, j])