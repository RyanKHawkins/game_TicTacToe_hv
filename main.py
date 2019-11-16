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
    board = create_board()
    num_players = input("How many players? (0 - 2):  ")

    current_player = "X"
    waiting_player = "O"

    if game_won(board):
        pass

    current_player, waiting_player = waiting_player, current_player


def player_move(board, player):
    valid_position = False
    position = ""
    while not valid_position and not position in ["1", "2", "3"]:
        position = input("Choose a spot (1-9):  ")
        position = int(position) - 1
        if space_free(board, position):
            board[position] = player
            valid_position = True
        else:
            position = input("That spot is taken. Choose another (1-9):  ")
            valid_position = False


def computer_move(board):
    possible_moves = []
    for space in board:
        if space_free(space):
            possible_moves.append(space)
    return possible_moves


def space_free(board, space):
    #return space not in ["X", "O"]
    if board[space] != "X" != "O":
        return True
    return False

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
    if board[0] == board[1] == board[2] == player:
        return True
    if board[3] == board[4] == board[5] == player:
        return True
    if board[6] == board[7] == board[8] == player:
        return True
    return False


def vertical_win(board, player):
    for column in range(3):
        if board[column] == board[column + 3] == board[column + 6] == player:
            return True
    return False


def diagonal_win(board, player):
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False


def board_full(board):
    for position in board:
        if position not in ["X", "O"]:
            return False
    return True


def game_tie(board):
    return board_full(board)

