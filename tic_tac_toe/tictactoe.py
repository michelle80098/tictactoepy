'''
Name: Michelle Huang
Class: Programming with Classes
Assignment: Tic Tac Toe Game 

Purpose:Tic-Tac-Toe is a game in which two players seek in alternate turns to complete a row, a column, or a diagonal with either three x's or three o's drawn in the spaces of a grid of nine squares

Rules: 
Tic-Tac-Toe is played according to the following rules.

The game is played on a grid that is three squares by three squares.
Player one uses x's. Player two uses o's.
Players take turns putting their marks in empty squares.
The first player to get three of their marks in a row (vertically, horizontally, or diagonally) is the winner.
If all nine squares are full and neither player has three in a row, the game ends in a draw.
'''


print('Welcome to Tic Tac Toe')
board = [" ", " ", " ",
        " ", " ", " ",
        " ", " ", " "]
current_player = "X"
winner = None
game_running = True

# print board
def display_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])

# take input from player 
def player_input(board):
    user_input = int(input("Enter a number between 1-9: "))
    #  checks that user input is between 1-9 & check user selection is available
    if user_input >= 1 and user_input <= 9 and board[user_input-1] == " ":
        board[user_input-1] = current_player
    else: 
        print("Not a valid number/spot unavailable!")
    


def check_win(board):
    global winner
    global game_running 
    if board[0] == board[1] == board[2] and board[0] != " ": 
        winner = board[0]
        game_running = False
        display_board(board)
        print(f"Congratulations! {winner} is the winner.")
        return True 
    elif board[3] == board[4] == board[5] and board[3] != " ":
        winner = board[3]
        game_running = False
        display_board(board)
        print(f"Congratulations! {winner} is the winner.")
        return True
    elif board[6] == board[7] == board[8] and board[6] != " ":
        winner = board[6]
        game_running = False
        display_board(board)
        print(f"Congratulations! {winner} is the winner.")
        return True
    elif board[0] == board[3] == board[6] and board[0] != " ": 
        winner = board[0]
        game_running = False
        display_board(board)
        print(f"Congratulations! {winner} is the winner.")
        return True
    elif board[1] == board[4] == board[7] and board[1] != " ": 
        winner = board[1]
        game_running = False
        display_board(board)
        print(f"Congratulations! {winner} is the winner.")
        return True
    elif board[2] == board[5] == board[8] and board[2] != " ": 
        winner = board[2]
        game_running = False
        display_board(board)
        print(f"Congratulations! {winner} is the winner.")
        return True
    elif board[0] == board[4] == board[8] and board[0] != " ": 
        winner = board[0]
        game_running = False
        display_board(board)
        print(f"Congratulations! {winner} is the winner.")
        return True
    elif board[2] == board[4] == board[6] and board[2] != " ":
        winner = board[2]
        game_running = False
        display_board(board)
        print(f"Congratulations! {winner} is the winner.")
        return True 


def check_draw(board):
    global game_running
    if " " not in board:
        display_board(board)
        print("It's a tie! ")
        game_running = False

def switch_player():
    global current_player
    if current_player  == "X":
        current_player = "O"
    else:
        current_player = "X"
        
def main():
    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6 ")
    print("--+---+--")
    print("7 | 8 | 9 ")
    print()
    while game_running:
        display_board(board)
        player_input(board)
        check_win(board)
        check_draw(board)
        switch_player()
        
main()


    
