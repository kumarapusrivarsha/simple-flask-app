from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize the game board
board = [''] * 9
current_player = 'X'
game_over = False
winner = None

@app.route('/')
def index():
    return render_template('index.html', board=board, current_player=current_player, game_over=game_over, winner=winner)

@app.route('/play', methods=['POST'])
def play():
    global board, current_player, game_over, winner

    # Get the position where the player wants to place their mark
    position = int(request.form['position'])

    # Check if the position is valid and the game is not over
    if 0 <= position < 9 and board[position] == '' and not game_over:
        # Place the mark on the board
        board[position] = current_player

        # Check for a winner
        if check_winner(current_player):
            game_over = True
            winner = current_player
        elif '' not in board:
            # If there is no winner and the board is full, it's a tie
            game_over = True

        # Switch the current player
        current_player = 'O' if current_player == 'X' else 'X'

    return index()

def check_winner(player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True

    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] == player or board[2] == board[4] == board[6] == player:
        return True

    return False

if __name__ == '__main__':
    app.run(debug=True)
