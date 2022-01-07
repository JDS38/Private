import numpy as np
import random
import pygame
import sys
import math
from tkinter import *

dote_Count = 24
Ai=1
Ai_piece = 9


# def create_board()
# return board()

def drop_piece(board, dote,piece):
    board[dote]= piece

def valide_location(board, dote):
    return board[dote_Count-1] == 0

def get_next_open_dote(board, dote):
    for dc in range (dote_Count):
        if board[dc][dote] == 0:
            return dc
def print_board(board):
    print(np.flip(board, 0))


game_over = False
FREEZONE = 1
def Ai():
    if turn == Ai and not game_over:
        Pos = int(math.floor(FREEZONE))
        if valide_location(FREEZONE):
            dote = get_next_open_dote(FREEZONE)
            drop_piece


