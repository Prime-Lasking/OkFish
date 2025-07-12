from Evaluation import *
import chess
import sys
from tqdm import tqdm
games = 100
white_wins = 0
black_wins = 0
draws = 0
for _ in tqdm(range(games),file=sys.stdout,colour="green"):
    board = chess.Board()
    while not board.is_game_over():
        if board.turn:
            move = best_move(board,3)
            board.push(move)
        else:
            move = best_move(board,4)
            board.push(move)

    outcome = board.outcome()
    if outcome:
        if outcome.result() == "1-0":
            white_wins=white_wins + 1
        elif outcome.result() == "0-1":
            black_wins=black_wins + 1
        else:
            draws = draws + 1

print(f"Results after {games} games:")
print(f"White wins: {white_wins}")
print(f"Black wins: {black_wins}")
print(f"Draws: {draws}")
