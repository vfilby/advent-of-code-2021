#!/usr/bin/env python
import os
import re
import sys
import copy

board_size = 5


# parse array of strings to a two dimensional int array
def parse_board( lines ):
	board = { 'values': [], 'played': [] }
	for line in lines:
		for cell in range(board_size):
			board['values'].append( int(line[cell*3:cell*3+3]) )
	
	board['played'] = [False] * len(board['values'])
	
	return board

def parse_input( filename ):
	with open(filename, 'r') as fp:
		lines = fp.readlines()
	
	# strip blank lines
	lines = list( filter( lambda l: re.match( '^\s*$', l ) == None, lines) )
	
	board_count = int((len(lines)-1 ) / board_size)
	
	# ensure that input is n * 5 + 1
	if ( len(lines)-1 ) % float(board_size) != 0:
		print( 'invalid input')
		SystemExit(-1)
	
	# parse draws and store as ints
	draws = list( map( lambda x: int(x), lines[0].strip().split(',') ) )
	
	# parse boards
	boards = []
	board_input = [lines[i:i+board_size] for i in range(1, len(lines[1:]), board_size)]
	for lines in board_input:
		boards.append( parse_board(lines) )
		
	return draws, boards
	
def is_winning_board( board ):
	
	# Slice out rows and columns from played and check for any that sum to five
	for row in list( board['played'][i:i+board_size] for i in range( 0, board_size**2, board_size ) ):
		if sum(row) == board_size:
			return True
	for column in list( board['played'][i:i+(board_size**2):board_size] for i in range(board_size) ):
		if sum(column) == board_size:
			return True
			
def mark_draw( draw, board ):
	indices = [i for i,v in enumerate(board['values']) if v == draw]
	for i in indices:
		board['played'][i] = True
		

def print_board( board ):
	print(*["---" for i in range(board_size)], "|",*["---" for i in range(board_size)])
	for i in range( 0, board_size**2, board_size):
		row = board['values'][i:i+board_size]
		print(*["{:3d}".format(c) for c in row], "|", *["{:3d}".format(c) for c in board['played'][i:i+board_size]])

def calculate_score( draw, board ):
	unplayed = [a*(1-b) for a,b in zip( board['values'], board['played'])]
	print(sum(unplayed))
	return sum(unplayed) * draw

def win_first( draws, boards ):
	local_boards = copy.deepcopy( boards )
	for draw in draws:
		
		for board in local_boards:
			mark_draw( draw, board )

			won = is_winning_board(board)
			
			
			if won:
				print("Draw:", draw)
				print_board(board)
				print(calculate_score(draw, board))
				return board
	
def win_last( draws, boards ):
	local_boards = copy.deepcopy( boards )
	boards_won = [False] * len(local_boards)
	
	for draw in draws:
		print("Draw:",draw)	
		print( "Boards won:", boards_won)
		
		for i,board in enumerate(local_boards):
			print("Checking board:",i)
			if boards_won[i]:
				continue
				
			mark_draw( draw, board )
			print_board(board)
	
			won = is_winning_board(board)
			
			if won and sum(boards_won) == len(boards_won) - 1:
				print("Draw:", draw)
				print_board(board)
				print(calculate_score(draw, board))
				return board
			
			if won:
				boards_won[i] = True
				#print(boards_won)
				print("Board {0} eliminated".format(i))
			
			
			
	
def main( filename ):
	draws, boards = parse_input(filename)
	
	#print(draws)
	#print(boards)
	
	#is_winning_board(boards[0])
	win_first( draws, boards )
	
	win_last( draws, boards )
	

		
if __name__ == '__main__':
	main( 'day4_input.txt' )
	