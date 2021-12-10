#!/usr/bin/env python
import os
import re
import sys
import copy
import itertools
import numpy as np

def parse_input( filename ):
	vent_lines = np.empty((0,4), int)
	with open(filename, 'r') as fp:
		lines = fp.readlines()
		
		for line in lines:
			match = re.match( "^\s*(?P<x1>\d+),(?P<y1>\d+) -> (?P<x2>\d+),(?P<y2>\d+)\s*$", line)
			
			if match:
				coordinates = [int(x) for x in [match['x1'], match['y1'], match['x2'], match['y2']]]
				vent_lines = np.vstack([vent_lines, coordinates])
			else:
				print("Error parsing input: ", line )
	print(vent_lines)
	return vent_lines
	
def create_full_coordinate_list( vent_line ):
	
	print("Generating full coordinates for:", vent_line)
	x1,y1,x2,y2 = vent_line
	
	x_dir = 1 if x2>=x1 else -1
	y_dir = 1 if y2>=y1 else -1
	
	print( "x1: {0}, x2: {1}, x_dir: {2}, y1: {3}, y2: {4}, y_dir: {5}".format(x1, x2, x_dir, y1, y2, y_dir))
	return [*range(y1,y2+y_dir,y_dir)],[*range(x1,x2+x_dir,x_dir)]
	
def construct_map( vent_lines ):
	# Total map as a 1-dim array
	map = {}
	
	map['min_x'] = min( [*vent_lines[:,0], *vent_lines[:,2]])
	map['min_y'] = min( [*vent_lines[:,1], *vent_lines[:,3]])
	map['max_x'] = max( [*vent_lines[:,0], *vent_lines[:,2]])
	map['max_y'] = max( [*vent_lines[:,1], *vent_lines[:,3]])
	
	map['points'] = np.zeros( (map['max_y']+1, map['max_x']+1), int)

	for vent_line in vent_lines:
		c = create_full_coordinate_list(vent_line)
		if c:
			print(c)
			map['points'][c] += 1

		print( map['points'] )
		print( (map['points'] >= 2).sum() )
	
	return map
	
	
def main( filename ):
	vent_lines = parse_input(filename)
	construct_map(vent_lines)
		


		
if __name__ == '__main__':
	main( 'day5_input.txt' )
	