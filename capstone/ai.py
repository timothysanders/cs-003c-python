from abc import ABC, abstractmethod
import ast
import copy
import os
import random

import pytest


class AI(ABC):
    def __init__(self):
        pass

    ## The make_move() method is defined as an abstract method as we do not provide an implementation
    ## here, but rather, leave it to the RandomAI class to implement. The method is also marked as a
    ## static method because it does not use any instance specific data
    @abstractmethod
    def make_move(self, available_spaces: list[int]) -> int:
        pass


## The RandomAI class implements mehods to act as a simple AI, randomly choosing
## spaces on the board to play in a game of tic tac toe
class RandomAI(AI):

    def __init__(self):
        super().__init__()

    ## The make_move method is a method that randomly chooses an integer from the list
    ## that is passed in the `available_spaces` parameter
    #  @param available_spaces: list[int]
    #      - A list of integers that represents the spaces on a tic tac toe board that are
    #        available to play
    #  @return move
    #      - A randomly chosen integer, representing a tic tac toe play
    def make_move(self, available_spaces: list[int]) -> int:
        move = random.choice(available_spaces)
        return move

    ## This method takes a list of lists representing a tic tac toe board
    ## and returns a list of integers that correspond to the spaces on the
    ## board that have yet to be played.
    #  @param board_spaces: list[list[str]]
    #      - A list of lists of strings, representing a tic tac toe board
    #  @return empty_spaces: list[int]
    #      - A list of integers that represent the unplayed spaces
    @staticmethod
    def get_empty_spaces(board_spaces: list[list[str]]) -> list[int]:
        empty_spaces = []
        for i, row in enumerate(board_spaces):
            for j, space in enumerate(row):
                if space == "-":
                    empty_spaces.append(i * 3 + j + 1)
        return empty_spaces


## The LearningAI class implements methods to act as a learning AI, randomly
## choosing available spaces on the board, but never returning a losing move
class LearningAI(AI):

    def __init__(self):
        super().__init__()
        self._loss_combinations = self.load_loss_states("loss_states.txt")

    def load_loss_states(self, file_name):
        loss_states = []
        try:
            with open(file_name, "r", encoding="utf-8") as fl:
                for line in fl.read().splitlines():
                    loss_states.append(ast.literal_eval(line))
        except FileNotFoundError:
            pass
        return loss_states

    def make_move(self, available_spaces) -> int:
        pass

    def make_informed_move(self, available_spaces: list[int], board_state) -> int:
        valid_move = False
        while not valid_move:
            move = random.choice(available_spaces)
            valid_move = self.check_move(move, board_state)
        return move

    @staticmethod
    def get_empty_spaces(board_spaces: list[list[str]]) -> list[int]:
        empty_spaces = []
        for i, row in enumerate(board_spaces):
            for j, space in enumerate(row):
                if space == "-":
                    empty_spaces.append(i * 3 + j + 1)
        return empty_spaces

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

    ## Checks the given move to see if it matches a known losing combination
    #  @param move: int
    #  @return bool
    def check_move(self, move: int, board_state) -> bool:
        row, column = self.convert_digit_to_row_column(move)
        copied_board = copy.deepcopy(board_state)
        copied_board[row][column] = "AI"
        if copied_board in self._loss_combinations:
            return False
        else:
            return True

    def learn_from_loss(self, board_state):
        self._loss_combinations.append(board_state)
        self.persist_loss_states()

    def get_loss_states(self):
        return self._loss_combinations

    def persist_loss_states(self) -> None:
        with open("loss_states.txt", "w+", encoding="utf-8") as fl:
            for x in self.get_loss_states():
                fl.write(str(x)+"\n")


@pytest.mark.parametrize("board_spaces, empty_spaces", [
    ([["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([["X", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]], [2, 3, 4, 5, 6, 7, 8, 9]),
])
def test_get_empty_spaces(board_spaces, empty_spaces):
    learning_ai = LearningAI()
    assert learning_ai.get_empty_spaces(board_spaces) == empty_spaces


@pytest.mark.parametrize("loss_state, loss_combinations", [
    ([["X", "AI", "X"], ["AI", "X", "AI"], ["X", "-", "-"]], [[["X", "AI", "X"], ["AI", "X", "AI"], ["X", "-", "-"]]]),
    ([["X", "AI", "X"], ["AI", "X", "AI"], ["-", "-", "X"]], [[["X", "AI", "X"], ["AI", "X", "AI"], ["-", "-", "X"]]])
])
def test_learn_from_loss(loss_state, loss_combinations):
    learning_ai = LearningAI()
    learning_ai.learn_from_loss(loss_state)
    assert learning_ai._loss_combinations == loss_combinations


@pytest.mark.parametrize("digit, result_row_column", [
    (1, (0, 0)),
    (4, (1, 0)),
    (7, (2, 0))
])
def test_convert_digit_to_row_column(digit, result_row_column):
    learning_ai = LearningAI()
    assert learning_ai.convert_digit_to_row_column(digit) == result_row_column


def test_make_informed_move():
    available_spaces = [2, 3, 4, 5, 6, 7, 8, 9]
    board_state = [["X", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    learning_ai = LearningAI()
    assert learning_ai.make_informed_move(available_spaces, board_state) != 1


def test_check_move():
    available_spaces = [6, 7, 8, 9]
    board_state = [["X", "AI", "X"], ["X", "AI", "-"], ["-", "-", "-"]]
    learning_ai = LearningAI()
    learning_ai.learn_from_loss([["X", "AI", "X"], ["X", "AI", "AI"], ["-", "-", "-"]])
    assert learning_ai.check_move(6, board_state) is False
