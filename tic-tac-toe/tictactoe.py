import sys


class BoardPrinter:

    symbols = {True: 'O', False: 'X', None: ' '}

    def write_board(self, board, output=sys.stdout):
        self.write_slice(board[0:3], output)
        self.write_line(output)
        self.write_slice(board[3:6], output)
        self.write_line(output)
        self.write_slice(board[6:9], output)

    def write_line(self, output):
        output.write('-+-+-\n')

    def write_slice(self, row, output):
        chars = [self.symbols[char] for char in row]
        output.write('{}|{}|{}\n'.format(*chars))


class PositionEvaluator:

    def is_winner(self, board, player):
        winning_seq = tuple([player] * 3)
        return board[0:3] == winning_seq\
                or board[3:6] == winning_seq\
                or board[6:9] == winning_seq\
                or board[0:7:3] == winning_seq\
                or board[1:8:3] == winning_seq\
                or board[2:9:3] == winning_seq\
                or board[0:9:4] == winning_seq\
                or board[2:7:2] == winning_seq


class Move:

    def __init__(self, move, board, outcome=0):
        self.move = move
        self.board = board    
        self.outcome = outcome


class MoveFinder:

    evaluator = PositionEvaluator()

    cache = {}

    def find_moves(self, board, player):
        key = (board, player)
        if key not in self.cache:
            moves = []
            for pos in range(9):
                if board[pos] is None:
                    new_board = board[:pos] + (player,) + board[pos + 1:]
                    if self.evaluator.is_winner(new_board, player):
                        moves.append(Move(pos, new_board, 1))
                    else:
                        outcomes = self.find_moves(new_board, not player)
                        if outcomes:
                            moves.append(Move(pos, new_board, -outcomes[0].outcome))
                        else:
                            moves.append(Move(pos, new_board, 0))
            self.cache[key] = sorted(moves, key=lambda move: (-move.outcome, move.move))
        return self.cache[key]
