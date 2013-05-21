#!/usr/bin/env python3

import tictactoe as t3


if __name__ == '__main__':
    finder = t3.MoveFinder()
    printer = t3.BoardPrinter()

    start_boards = [
            (True, None, None, None, None, None, None, None, None),
            (None, True, None, None, None, None, None, None, None),
            (None, None, None, None, True, None, None, None, None)]
    print('optimal responses to different starting moves:')
    for start_board in start_boards: 
        results = finder.find_moves(start_board, False)
        boards = [res.board for res in results if res.outcome >= 0]
        valid_responses = [None] * 9
        for pos in range(9):
            pos_values = {board[pos] for board in boards if board[pos] is not None}
            if pos_values:
                valid_responses[pos] = next(iter(pos_values))
        printer.write_board(valid_responses)

        print()
