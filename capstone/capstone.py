from ezgraphics import GraphicsWindow


class Board:

    def __init__(self):
        self.LINE_CONFIGS = [
            (200, 0, 15, 629),
            (415, 0, 15, 629),
            (0, 215, 629, 15),
            (0, 425, 629, 15)
        ]
        self.TEXT_CONFIGS = [
            (5, 5, "1"),
            (220, 5, "2"),
            (435, 5, "3"),
            (5, 230, "4"),
            (220, 230, "5"),
            (435, 230, "6"),
            (5, 445, "7"),
            (220, 445, "8"),
            (435, 445, "9")
        ]
        self.board_spaces = [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]
        ]
        self.board = None
        self.canvas = None

    def draw_board(self):
        self.board = GraphicsWindow(630, 630)
        self.canvas = self.board.canvas()
        self.canvas.setColor(red=115, green=179, blue=4)
        self.canvas.drawRect(x=0, y=0, width=630, height=630)
        self.canvas.setColor("black")
        for line in self.LINE_CONFIGS:
            self.canvas.drawRect(
                x=line[0],
                y=line[1],
                width=line[2],
                height=line[3]
            )
        self.canvas.setFontSize(size=20)
        for text in self.TEXT_CONFIGS:
            self.canvas.drawText(
                x=text[0],
                y=text[1],
                text=text[2]
            )
        self.board.show()

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

    def check_win(self) -> bool:
        win_state = False
        # Check rows for winning combinations
        for row in self.board_spaces:
            if row[0] == row[1] == row[2] and row[0] != "-":
                win_state = True
        # Check columns for winning combinations
        for column in range(3):
            if (self.board_spaces[0][column] == self.board_spaces[1][column] == self.board_spaces[2][column]
                    and self.board_spaces[0][column] != "-"):
                win_state = True
        # Check diagonals for winning combinations
        if (self.board_spaces[0][0] == self.board_spaces[1][1] == self.board_spaces[2][2]
                and self.board_spaces[0][0] != "-"):
            win_state = True
        if (self.board_spaces[0][2] == self.board_spaces[1][1] == self.board_spaces[2][0]
                and self.board_spaces[0][2] != "-"):
            win_state = True
        return win_state


class Game:

    def __init__(self):
        self.game_board = Board()
        self.player_one_name = None
        self.player_one_marker = None
        self.player_two_name = None
        self.player_two_marker = None

    def get_player_name(self, player: int, message: str) -> None:
        if player == 1:
            self.player_one_name = input(message)
        else:
            self.player_two_name = input(message)

    def get_player_marker(self, player: int, message: str) -> None:
        if player == 1:
            self.player_one_marker = input(message)
        else:
            self.player_two_marker = input(message)

    def reset_game(self):
        self.game_board = Board()

    def validate_play(self, digit: str) -> int:
        if not digit.isdigit():
            raise TypeError("You must provide a value that is a valid digit!")
        elif int(digit) > 9 or int(digit) < 1:
            raise ValueError("You must provide a value between 1-9!")
        return int(digit)

    def play(self):
        self.game_board.draw_board()
        end_state = False
        player = "one"
        player_name = self.player_one_name
        while not end_state:
            try:
                user_play = input(f"{player_name}, please enter a space on the board (1-9): ")
                validated_play = self.validate_play(user_play)
                row_column = self.game_board.convert_digit_to_row_column(validated_play)
                if player == "one":
                    self.game_board.place_move(row_column[0], row_column[1], self.player_one_marker)
                    if self.game_board.check_win():
                        end_state = True
                        print(f"Player {player_name} wins!")
                    player_name = self.player_two_name
                    player = "two"
                else:
                    self.game_board.place_move(row_column[0], row_column[1], self.player_two_marker)
                    if self.game_board.check_win():
                        end_state = True
                        print(f"Player {player_name} wins!")
                    player_name = self.player_one_name
                    player = "one"
            except (TypeError, ValueError) as ve:
                print(f"ERROR: {ve}")


def main():
    print("Welcome to Tic Tac Toe!")
    new_game = Game()
    new_game.get_player_name(1, "Player one, please enter your name: ")
    new_game.get_player_marker(1, "Player one, please enter your marker: ")
    new_game.get_player_name(2, "Player two, please enter your name: ")
    new_game.get_player_marker(2, "Player two, please select your marker: ")
    print("-"*30)
    print("Game start!")
    new_game.play()


if __name__ == "__main__":
    main()
