
class Board(object):

    def __init__(self, size, who, move=-1, depth=0):
        self.depth = depth
        self.size = size
        self.playerMax = 0
        self.playerMin = 0
        self.who = who
        self.lastMove = move
        self.board = []
        self.availableMoves = []

    @classmethod
    def from_board(cls, board, move):
        size = board.size
        who = 1 if board.who == 2 or board.who == 0 else 2
        newBoard = cls(size, who, move, board.depth+1)
        newBoard.board = [x[:] for x in board.board]
        newBoard.playerMax = board.playerMax
        newBoard.playerMin = board.playerMin
        newBoard.board[move[0]][move[1]] = who
        newBoard.availableMoves = [x[:] for x in board.availableMoves]
        newBoard.update_score_one()
        return newBoard

    def make_next_move(self):
        if len(self.availableMoves) > 0:
            return self.availableMoves.pop()
        else:
            return []

    def init_available_moves_and_board(self):
        for i in range(self.size):
            for j in range(self.size):
                self.availableMoves.append([i, j])
        self.board = [[0 for i in range(self.size)] for j in range(self.size)]


    #Add points for the last move to the existing score
    def update_score_one(self):
        row = self.lastMove[0]
        col = self.lastMove[1]
        points = 0

        #Horizontal
        if len([x for x in self.board[row] if x != 0]) == self.size:
            points += self.size

        #Vertical
        my_list = []
        for i in range(self.size):
            if self.board[i][col] != 0:
                my_list.append(1);
        if len(my_list) == self.size:
            points += self.size

        #Diagonal1
        my_list = []
        for i in range(self.size):
            if row + i < self.size and col + i < self.size:
                my_list.append(self.board[row+i][col+i])
            if row - i >= 0 and col - i >= 0:
                my_list.append(self.board[row-i][col-i])

        if len(my_list) == len([x for x in my_list if x != 0]):
            points += len(my_list)

        #Diagonal2
        my_list = []
        for i in range(self.size):
            if row + i < self.size and col - i >= 0:
                my_list.append(self.board[row + i][col - i])
            if row - i >= 0 and col + i < self.size:
                my_list.append(self.board[row - i][col + i])

        if len(my_list) == len([x for x in my_list if x != 0]):
            points += len(my_list)

        if self.who == 1:
            self.playerMax += points
        else:
            self.playerMin += points
