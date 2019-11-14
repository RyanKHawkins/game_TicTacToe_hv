# TicTacToe - Hybrid Version
# by Ryan Hawkins

import random
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


EMPTY = "   "


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
    

def player_move(player):
    pass


def computer_move():
    pass


def space_free(space):
    return space not in ["X", "O"]


def random_move():
    pass


def smart_move():
    pass


def game_won():
    pass


def vertical_win():
    pass


def horizontal_win():
    pass


def diagonal_win():
    pass


def board_full():
    pass


def game_tie():
    pass


def switch_players():
    pass


# temporary testers
board = create_board()
display_board(board)
