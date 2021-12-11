#!/usr/bin/env python
import os
import re
import sys
import copy
import math
import itertools
import numpy as np

def parse_input( filename ):
	with open(filename, 'r') as fp:
		line = fp.readline()
		
		positions = list( map( lambda x: int(x), line.strip().split(',') ) )
		return positions
	
def main( filename ):
	positions = parse_input(filename)
	print(positions)
	
	min_pos = min(positions)
	max_pos = max(positions)
	
	min_fuel = sys.maxsize
	min_fuel_value=0
	
	for i in range(min_pos,max_pos):
		fuel = 0
		for j in range( 0, len(positions) ):
			delta = abs(i-positions[j])
			cost = 0 if delta == 0 else ( (delta/2) * (1 + delta) ) 
			print( "{0} -> {1} ({2} steps) takes {3} fuel".format(positions[j], i, delta, cost))
			fuel += cost
			
		print("Error for {0} is {1}".format(i, fuel))
		
		if( fuel < min_fuel ):
			min_fuel = fuel
			min_fuel_value = i
			
	print( "Fuel used {0} to move to position {1}".format(min_fuel, min_fuel_value) )

		
if __name__ == '__main__':
	main( 'day7_input.txt' )
	