# TicTacToe - Hybrid Version
# by Ryan Hawkins

import random
import os
import time


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def create_board():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    return board


def display_board(board):
    print()
    print(" " + " | ".join(board[0:3]))
    print("--- " * 3)
    print(" " + " | ".join(board[3:6]))
    print("--- " * 3)
    print(" " + " | ".join(board[6:9]))
    print()


def play_game():
    num_players = input("How many players? (0 - 2):  ")

    current_player = "X"
    waiting_player = "O"

    if game_won(board):
        pass

    current_player, waiting_player = waiting_player, current_player


def player_move(player):
    pass


def computer_move(board):
    possible_moves = []
    for space in board:
        if space_free(space):
            possible_moves.append(space)
    return possible_moves


def space_free(space):
    return space not in ["X", "O"]


def random_computer_move(possible_moves):
    return random.choice(possible_moves)


def smart_computer_move():
    pass


def game_won(board, player):
    if horizontal_win(board, player):
        return True
    if vertical_win(board, player):
        return True
    if diagonal_win(board, player):
        return True
    return False


def horizontal_win(board, player):
    pass


def vertical_win(board, player):
    for column in range(3):
        if board[column] == board[column + 3] == board[column + 6] == player:
            return True
    return False


def diagonal_win():
    pass


def board_full(board):
    for position in board:
        if position not in ["X", "O"]:
            return False
    return True


def game_tie(board):
    return board_full(board)


# temporary testers
board = create_board()
display_board(board)
if board_full(board):
    print("Board is full.")
if not board_full(board):
    print("Board is not full.")
