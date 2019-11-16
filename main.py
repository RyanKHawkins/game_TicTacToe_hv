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

    clear()
    display_board(board)

    while not game_won(board) and not game_tied(board):

        player_move(board, current_player)
        display_board(board)
        if game_won(board):
            winner = current_player
            print(f"{winner} won!")

        if game_tied(board):
            print("Game tied.")

        current_player, waiting_player = waiting_player, current_player


def player_move(board, player):
    valid_position = False
    position = ""
    while not valid_position:
        position = input(f"Where do you want to place your '{player}'?:  ").strip()
        while not position in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a number between 1 and 9:  ").strip()
        position = int(position) - 1
        if space_free(board, position):
            board[position] = player
            valid_position = True
        else:
            print("That spot is taken.")
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


def game_won(board):
    if horizontal_win(board):
        return True
    if vertical_win(board):
        return True
    if diagonal_win(board):
        return True
    return False


def horizontal_win(board):
    if board[0] == board[1] == board[2]:
        return True
    if board[3] == board[4] == board[5]:
        return True
    if board[6] == board[7] == board[8]:
        return True
    return False


def vertical_win(board):
    for column in range(3):
        if board[column] == board[column + 3] == board[column + 6]:
            return True
    return False


def diagonal_win(board):
    if board[0] == board[4] == board[8]:
        return True
    if board[2] == board[4] == board[6]:
        return True
    return False


def board_full(board):
    for position in board:
        if position not in ["X", "O"]:
            return False
    return True


def game_tied(board):
    if not game_won(board) and board_full(board):
        return True
    return False

play_game()