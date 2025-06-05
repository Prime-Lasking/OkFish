from Evaluation import *
import chess
board = chess.Board()
while not board.is_game_over():
    print(board)
    print('--------------------')
    if board.turn:
        move = best_move(board)
        print(move)
        with open("Chessfile.txt", "a") as f:
            f.write(str(board.san(move)))
            f.write('|')
        board.push(move)

    else:
        move = get_human_move(board)
        print(move)
        with open("Chessfile.txt", "a") as f:
            f.write(str(board.san(move)))
            f.write('|')
        board.push(move)


print(board)
with open("Chessfile.txt", "a") as f:
    f.write('   \n')
print("Game Over")
print(board.result())
print(board.outcome())


