#!/usr/bin/env python
import os
import sys


def main( filename ):
	
	decreasing_count = 0
	increasing_count = 0
	
	with open(filename, 'r') as fp:
		line = fp.readline()
		last_value = int( line )
		while line:
			current_value = int(line)
			if current_value < last_value:
				decreasing_count += 1
				print( current_value, " increased" )
			elif current_value > last_value:
				increasing_count += 1
				print( current_value, " decreased" )
				
			last_value = current_value
			line = fp.readline()
			
		print( "Increasing Count: ", increasing_count )
		print( "Decreasing Count: ", decreasing_count )
		
	
	
if __name__ == '__main__':
	main( 'day1a_input.txt' )