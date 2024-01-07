import time

class Guess:
    def __init__(self, board, code):
         self.board = board
         self.code = code

    def award_key_pegs(self, code):
            self.guess = self.board.board[self.board.current_row]
            code_copy = self.code[:]
            guess_copy = self.guess[:]
            position_pegs = 0
            non_position_pegs = 0
            keypegs_position = 0
            for index, guess in enumerate(guess_copy):
                 if guess == code_copy[index]:
                      position_pegs += 1
                      code_copy[index] = 'Checked sol.'
                      guess_copy[index] = 'Checked guess.'

            for index, guess in enumerate(guess_copy):   
               for i, p in enumerate(code_copy):
                    if p == guess:
                        non_position_pegs += 1
                        code_copy[i] = 'Checked solu.'
                        break

                      
     
            for i in range(position_pegs):
                self.board.key_pegs[self.board.current_row][keypegs_position] = 2
                keypegs_position += 1
            for j in range(non_position_pegs):
                self.board.key_pegs[self.board.current_row][keypegs_position] = 1
                keypegs_position += 1

            if self.board.key_pegs[self.board.current_row] == [2, 2, 2, 2]:
                 self.board.guessed = True
            elif self.board.current_row == self.board.num_rows-1:
                 self.board.game_over = True
            else:
                 self.board.current_row += 1
                 self.board.current_col = 0
            time.sleep(0.1)

