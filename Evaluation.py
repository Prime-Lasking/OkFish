import chess

# Define piece values
piece_values = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 100
}
def evaluation(board):
    check_mate = 0
    if board.is_checkmate():
        check_mate += float(math.inf)
    wp = len(board.pieces(chess.PAWN, chess.WHITE))
    bp = len(board.pieces(chess.PAWN, chess.BLACK))
    wn = len(board.pieces(chess.KNIGHT, chess.WHITE))
    bn = len(board.pieces(chess.KNIGHT, chess.BLACK))
    wb = len(board.pieces(chess.BISHOP, chess.WHITE))
    bb = len(board.pieces(chess.BISHOP, chess.BLACK))
    wr = len(board.pieces(chess.ROOK, chess.WHITE))
    br = len(board.pieces(chess.ROOK, chess.BLACK))
    wq = len(board.pieces(chess.QUEEN, chess.WHITE))
    bq = len(board.pieces(chess.QUEEN, chess.BLACK))

    material_score = 1 * (wp - bp) + 3 * (wn - bn) + 4 * (wb - bb) + 5 * (wr - br) + 10 * (wq - bq)
    return material_score + check_mate
    if board.turn:
        return -total_score
    else:
        return total_score

def best_move(board):
        best_score = -float('inf')
        best_move = chess.E4

        for move in board.legal_moves:
            board.push(move)
            score = evaluation(board)
            board.pop()

            if score >= best_score:
                best_score = score
                best_move = move
        return best_move
def get_human_move(board):
    #Get a move from  input
    human_move = input("Enter your move (in SAN format:eg,e4): ")
    return board.parse_san(human_move)

