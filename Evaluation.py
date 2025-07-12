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

    material_score = 1 * (wp - bp) + 3.3 * (wn - bn) + 3.5 * (wb - bb) + 5 * (wr - br) + 9 * (wq - bq)
    return material_score + check_mate
    if board.turn:
        return total_score
    else:
        return -total_score
def negamax(board, depth, alpha, beta, color):
    if depth == 0 or board.is_game_over():
        return color * evaluation(board)
    
    max_eval = float('-inf')
    for move in board.legal_moves:
        board.push(move)
        if move == None:
            break
        eval = -negamax(board, depth - 1, -beta, -alpha, -color)
        board.pop()
        max_eval = max(max_eval, eval)
        alpha = max(alpha, eval)
        if alpha >= beta:
            break
    return max_eval
def best_move(board):
    legal_moves = list(board.legal_moves)
    alpha = float('-inf')
    beta = float('inf')
    color = 1 if board.turn else -1
    best_score = float('-inf')
    best_move_found = random.choice(legal_moves)
        for move in board.legal_moves:
            board.push(move)
            score = -negamax(board, depth - 1, -beta, -alpha, -color)
            if board.is_capture(move):
             captured = board.piece_at(move.to_square)
             taker = board.piece_at(move.from_square)
             if captured and taker and piece_values[captured.piece_type] >= piece_values[taker.piece_type]:
                score += 10
        board.pop()
            if score == best_score:
              best_score = score
              best_move_found = move
    return best_move_found
def random_move(board):
    legal_moves = list(board.legal_moves)
    if legal_moves:
        return random.choice(legal_moves)
    else:
        return None
def get_human_move(board):
    human_move = input("Enter your move (in SAN format:eg,e4): ")
    try:
      return board.parse_san(human_move)
    except ValueError:
        print("Invalid move.Try again.")

