# CS-003 - Capstone - Tic-Tac-Toe Learning AI
# 8/1/2024
# Zoraida Rodriguez
# Timothy Sanders
#
# Problem Statement
# Implement a program that allows two players to play tic-tac-toe
# or allow the player to play against a learning AI.
# The simple AI will create a random number between 1-9 instead of being asked

from abc import ABC, abstractmethod
import copy
import random
import sys

from ezgraphics import GraphicsWindow
import pytest

from ai import AI, LearningAI, RandomAI

## The Board class is used to represent a tic tac toe board, with methods
## to draw the board, validate plays, and check whether the game has been won
class Board:

    ## Initializes the board class and configures the empty board
    def __init__(self):
        self.LINE_CONFIGS = [(200, 0, 15, 629), (415, 0, 15, 629),
                             (0, 215, 629, 15), (0, 425, 629, 15)]
        self.TEXT_CONFIGS = [(5, 5, "1"), (220, 5, "2"), (435, 5, "3"),
                             (5, 230, "4"), (220, 230, "5"), (435, 230, "6"),
                             (5, 445, "7"), (220, 445, "8"), (435, 445, "9")]
        self.board_spaces = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
        self.board = None
        self.canvas = None

    ## Method to create the game board itself using ezgraphics
    def draw_board(self):
        self.board = GraphicsWindow(630, 630)
        self.canvas = self.board.canvas()
        self.canvas.setColor(red=115, green=179, blue=4)
        self.canvas.drawRect(x=0, y=0, width=630, height=630)
        self.canvas.setColor("black")
        for line in self.LINE_CONFIGS:
            self.canvas.drawRect(x=line[0],
                                 y=line[1],
                                 width=line[2],
                                 height=line[3])
        self.canvas.setFontSize(size=20)
        for text in self.TEXT_CONFIGS:
            self.canvas.drawText(x=text[0], y=text[1], text=text[2])
        self.board.show()

    ## Closes the window in ezgraphics to allow for resetting the game
    def close_board(self):
        self.board.close()

    ## Converts a move (1-9) to row and column coordinates.
    #  @param moveDigit: int
    #    - the numbered space on the board to place a marker
    #  @return tuple(int, int)
    #    - a tuple of the corresponding row and column of the input digit
    def convert_digit_to_row_column(self, digit: int) -> tuple[int, int]:
        if digit <= 3:
            row = 0
            column = digit - 1
        elif digit <= 6:
            row = 1
            column = (digit - 1) % 3
        else:
            row = 2
            column = (digit - 1) % 3
        return row, column

    ## Place a move on the board if the cell is empty.
    #  @param row: int
    #    - the specific row (0-2) to place the marker on
    #  @param column: int
    #    - the specific column (0-2) to place the marker on
    #  @return bool
    #    - indicates whether the move was placed successfully
    def place_move(self, row: int, column: int, marker: str) -> bool:
        text_x = (column * 210) + 50
        text_y = (row * 210) + 25
        if self.board_spaces[row][column] != "-":
            raise ValueError("You must specify an unoccupied space!")
        elif self.board_spaces[row][column] == "-":
            self.board_spaces[row][column] = marker
            self.canvas.setFontSize(150)
            self.canvas.drawText(x=text_x, y=text_y, text=marker)
            self.board.show()
            return True
        else:
            return False

    ## Checks if the given marker (‘X’, ‘O’) has won.
    #  @param marker: str
    #      - The specific marker to check the win condition for
    #  @return bool
    #      - returns True if the specified marker has won, otherwise False
    def check_win(self) -> bool:
        win_state = False
        # Check rows for winning combinations
        for row in self.board_spaces:
            if row[0] == row[1] == row[2] and row[0] != "-":
                win_state = True
        # Check columns for winning combinations
        for column in range(3):
            if (self.board_spaces[0][column] == self.board_spaces[1][column] ==
                    self.board_spaces[2][column]
                    and self.board_spaces[0][column] != "-"):
                win_state = True
        # Check diagonals for winning combinations
        if (self.board_spaces[0][0] == self.board_spaces[1][1] ==
                self.board_spaces[2][2] and self.board_spaces[0][0] != "-"):
            win_state = True
        if (self.board_spaces[0][2] == self.board_spaces[1][1] ==
                self.board_spaces[2][0] and self.board_spaces[0][2] != "-"):
            win_state = True
        return win_state

    ## Checks if the game has ended in a draw by checking to see if any spaces are yet to be played
    #  @return bool
    #      - returns True if the game is a draw, otherwise False
    def check_draw(self) -> bool:
        return not any("-" in row for row in self.board_spaces)


## The Game board contains methods to handle the playing of the tic tac toe game,
## keeping track of player names and markers, along with defining methods for
## playing against another player or against the AI
class Game:

    ## Initializes the Game() class with a new board
    def __init__(self):
        self.game_board = Board()
        self.player_one_name = None
        self.player_one_marker = None
        self.player_two_name = None
        self.player_two_marker = None
        self._player_ai_name = None
        self._player_ai_marker = None
        self._player_ai = None

    ## Prompts the player for a name, then assigns it to an
    ## instance variable
    #  @param player: int
    #      - The number of the player to get the name from
    #  @param message: str
    #      - The message to display to the player in the input function
    def get_player_name(self, player: int, message: str) -> None:
        if player == 1:
            self.player_one_name = input(message)
        else:
            self.player_two_name = input(message)

    ## Ask for the ‘X’ or ‘O’ option, then assigns it to an
    ## instance variable.
    #  @param player: int
    #      - The player to ask for the marker from
    #  @param message: str
    #      - The message to be displayed to the player in the input function
    def get_player_marker(self, player: int, message: str) -> None:
        if player == 1:
            self.player_one_marker = input(message)
        else:
            self.player_two_marker = input(message)

    ## Resets the game board for a new game
    def reset_game(self):
        self.game_board = Board()

    ## Performs validation on the plays made by the user, enforces that the entry is a digit
    ## that is between 1-9 (zeros to reset the game are handled elsewhere
    #  @param - digit: str
    #      - The raw input from the user
    def validate_play(self, digit: str) -> int:
        if not digit.isdigit():
            raise TypeError("You must provide a value that is a valid digit!")
        elif int(digit) > 9 or int(digit) < 1:
            raise ValueError("You must provide a value between 1-9!")
        return int(digit)

    ## Initializes the RandomAI class and sets the AI player name and marker
    def set_ai_player(self):
        self._player_ai = RandomAI()
        self._player_ai_name = "AI"
        self._player_ai_marker = "AI"

    ## Initializing the LearningAI class and sets the AI player name and marker
    def set_learning_ai_player(self):
        self._player_ai = LearningAI()
        self._player_ai_name = "AI"
        self._player_ai_marker = "AI"

    ## Displays an intimidating message to any human foolish enough to challenge the AI
    @staticmethod
    def print_dalek():
        print("""
                    Exterminate!
                    Err... Let's play!
                   /
              ___
      D>=G==='   '.
            |======|
            |======|
        )--/]IIIIII]
           |_______|
           C O O O D
          C O  O  O D
         C  O  O  O  D
         C__O__O__O__D
        [_____________]
        """)

    ## Manages the game flow, takes turns between players, and checks
    ## for win/draw conditions after each move.
    def play(self):
        self.game_board.draw_board()
        end_state = False
        player = "one"
        player_name = self.player_one_name
        while not end_state:
            try:
                user_play = input(
                    f"{player_name}, please enter a space (1-9) on the board (0 to restart the game) : "
                )
                if user_play == "0":
                    self.game_board.close_board()
                    self.reset_game()
                    self.play()
                validated_play = self.validate_play(user_play)
                row_column = self.game_board.convert_digit_to_row_column(
                    validated_play)
                if player == "one":
                    self.game_board.place_move(row_column[0], row_column[1],
                                               self.player_one_marker)
                    if self.game_board.check_win():
                        end_state = True
                        print(f"Player {player_name} wins!")
                        play_again = input(
                            "Would you like to play again? (Y/N): ")
                        if play_again == "Y":
                            self.game_board.close_board()
                            self.reset_game()
                            self.play()
                        else:
                            sys.exit()
                    if self.game_board.check_draw():
                        print("Game has ended in a draw!")
                        play_again = input(
                            "Would you like to play again? (Y/N): ")
                        if play_again == "Y":
                            self.game_board.close_board()
                            self.reset_game()
                            self.play()
                        else:
                            sys.exit()
                    player_name = self.player_two_name
                    player = "two"
                else:
                    self.game_board.place_move(row_column[0], row_column[1],
                                               self.player_two_marker)
                    if self.game_board.check_win():
                        end_state = True
                        print(f"Player {player_name} wins!")
                        play_again = input(
                            "Would you like to play again? (Y/N): ")
                        if play_again.upper().strip() == "Y":
                            self.game_board.close_board()
                            self.reset_game()
                            self.play()
                        else:
                            sys.exit()
                    player_name = self.player_one_name
                    player = "one"
            except (TypeError, ValueError) as ve:
                print(f"ERROR: {ve}")

    ## The play_ai() method is used to control the game logic when a user decides
    ## to play against the simple AI that has been implemented in this application
    ## This method manages the game flow between the human player and the AI,
    ## checking for win conditions and valid moves after each entry.
    def play_ai(self):
        self.set_learning_ai_player()
        self.game_board.draw_board()
        end_state = False
        player = "one"
        player_name = self.player_one_name
        while not end_state:
            try:
                if player == "one":
                    user_play = input(
                        f"{player_name}, please enter a space (1-9) on the board (0 to restart the game) : "
                    )
                    if user_play == "0":
                        self.game_board.close_board()
                        self.reset_game()
                        self.play_ai()
                    validated_play = self.validate_play(user_play)
                    row_column = self.game_board.convert_digit_to_row_column(
                        validated_play)
                    temp_board = copy.deepcopy(self.game_board.board_spaces)
                    self.game_board.place_move(row_column[0], row_column[1],
                                               self.player_one_marker)
                    if self.game_board.check_win():
                        self._player_ai.learn_from_loss(temp_board)
                        end_state = True
                        print(
                            f"The AI has benevolently allowed {player_name} to win!"
                        )
                        play_again = input(
                            "Would you like to play again? (Y/N): ")
                        if play_again == "Y":
                            self.game_board.close_board()
                            self.reset_game()
                            self.play_ai()
                        else:
                            sys.exit()
                    if self.game_board.check_draw():
                        print("Game has ended in a draw!")
                        play_again = input(
                            "Would you like to play again? (Y/N): ")
                        if play_again == "Y":
                            self.game_board.close_board()
                            self.reset_game()
                            self.play_ai()
                        else:
                            sys.exit()
                    player = "AI"
                available_spaces = self._player_ai.get_empty_spaces(
                    self.game_board.board_spaces)
                chosen_move = self._player_ai.make_informed_move(available_spaces,self.game_board.board_spaces)
                print(
                    f"The AI senses a weak, carbon-based life form and plays {chosen_move}"
                )
                row_column = self.game_board.convert_digit_to_row_column(
                    chosen_move)
                self.game_board.place_move(row_column[0], row_column[1],
                                           self._player_ai_marker)
                if self.game_board.check_win():
                    end_state = True
                    print(
                        "The AI has defeated the mere human life form in Tic Tac Toe!"
                    )
                    play_ai_again = input(
                        "Would you like to lose to the AI again? (Y/N): ")
                    if play_ai_again.upper() == "Y":
                        self.game_board.close_board()
                        self.reset_game()
                        self.play_ai()
                    else:
                        sys.exit()
                player_name = self.player_one_name
                player = "one"
            except (TypeError, ValueError) as ve:
                print(f"ERROR: {ve}")


def main():
    print("Welcome to Tic Tac Toe!")
    new_game = Game()
    new_game.get_player_name(1, "Player one, please enter your name: ")
    new_game.get_player_marker(1, "Player one, please enter your marker: ")
    ai_response = input("Would you like to play the AI? (Y/N): ")
    if ai_response.upper() == "Y":
        new_game.print_dalek()
        new_game.set_learning_ai_player()
        print("-" * 30)
        print("Game start!")
        new_game.play_ai()
    else:
        new_game.get_player_name(2, "Player two, please enter your name: ")
        new_game.get_player_marker(2,
                                   "Player two, please select your marker: ")
        print("-" * 30)
        print("Game start!")
        new_game.play()


if __name__ == "__main__":
    main()
"""
> python capstone/capstone.py
Welcome to Tic Tac Toe!
Player one, please enter your name: Zoe
Player one, please enter your marker: X
Player two, please enter your name: Tim
Player two, please select your marker: O
------------------------------
Game start!
Zoe, please enter a space (1-9) on the board (0 to restart the game) : 6
Tim, please enter a space (1-9) on the board (0 to restart the game) : 6
ERROR: You must specify an unoccupied space!
Tim, please enter a space (1-9) on the board (0 to restart the game) : 2
Zoe, please enter a space (1-9) on the board (0 to restart the game) : 3
Tim, please enter a space (1-9) on the board (0 to restart the game) : 9
Zoe, please enter a space (1-9) on the board (0 to restart the game) : 5
Tim, please enter a space (1-9) on the board (0 to restart the game) : 7
Zoe, please enter a space (1-9) on the board (0 to restart the game) : 4
Player Zoe wins!
Would you like to play again? (Y/N): Y
Zoe, please enter a space (1-9) on the board (0 to restart the game) : 1
Tim, please enter a space (1-9) on the board (0 to restart the game) : 2
Zoe, please enter a space (1-9) on the board (0 to restart the game) : 3
Tim, please enter a space (1-9) on the board (0 to restart the game) : 4
Zoe, please enter a space (1-9) on the board (0 to restart the game) : 5
Tim, please enter a space (1-9) on the board (0 to restart the game) : 6
Zoe, please enter a space (1-9) on the board (0 to restart the game) : 8
Tim, please enter a space (1-9) on the board (0 to restart the game) : 7
Zoe, please enter a space (1-9) on the board (0 to restart the game) : 9
Game has ended in a draw!
Would you like to play again? (Y/N): N
"""
"""
> python capstone/capstone.py

Welcome to Tic Tac Toe!
Player one, please enter your name: Tim
Player one, please enter your marker: X
Would you like to play the AI? (Y/N): Y

                    Exterminate!
                    Err... Let's play!
                   /
              ___
      D>=G==='   '.
            |======|
            |======|
        )--/]IIIIII]
           |_______|
           C O O O D
          C O  O  O D
         C  O  O  O  D
         C__O__O__O__D
        [_____________]

------------------------------
Game start!
Tim, please enter a space (1-9) on the board (0 to restart the game) : 1
The AI senses a weak, carbon-based life form and plays 4
Tim, please enter a space (1-9) on the board (0 to restart the game) : 2
The AI senses a weak, carbon-based life form and plays 6
Tim, please enter a space (1-9) on the board (0 to restart the game) : 5
The AI senses a weak, carbon-based life form and plays 9
Tim, please enter a space (1-9) on the board (0 to restart the game) : 7
The AI senses a weak, carbon-based life form and plays 3
The AI has defeated the mere human life form in Tic Tac Toe!
Would you like to play again? (Y/N): N
"""
