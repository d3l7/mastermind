class Guess:
    def __init__(self, board):
         self.board = board

    def award_key_pegs(self, code):
            self.guess = self.board.board[self.board.current_row]
            position_pegs = 0
            non_position_pegs = 0
            no_pegs = 0
            keypegs_position = 0
            for value in self.guess:
                if value not in code:
                    no_pegs += 1
                elif (value in code) and (self.guess.index(value) == code.index(value)):
                    position_pegs += 1
                else:
                    non_position_pegs += 1
            
            for i in range(position_pegs):
                self.board.key_pegs[self.board.current_row][keypegs_position] = 2
                keypegs_position += 1
            for j in range(non_position_pegs):
                self.board.key_pegs[self.board.current_row][keypegs_position] = 1
                keypegs_position += 1

            if self.board.key_pegs[self.board.current_row] == [2, 2, 2, 2]:
                 self.board.guessed = True
            else:
                 self.board.current_row += 1
                 self.board.current_col = 0

