#!/usr/bin/env python
import os
import sys


def main( filename ):
	
	decreasing_count = 0
	increasing_count = 0
	values = []
	
	with open(filename, 'r') as fp:
		lines = fp.readlines()
		
		for line in lines:
			values.append( int(line) )
			
			
	if len(values) < 4:
		print( "Not enough values")
	
	
	last_value = sum( values[0:3] )
	print( last_value, " initial" )
	
	for i in range(1, len(values) - 2):
		current_value = sum( values[i:i+3] )
		#print( values[i:i+3], current_value )
		
		if current_value < last_value:
			decreasing_count += 1
			print( current_value, " decreased" )
		elif current_value > last_value:
			increasing_count += 1
			print( current_value, " increased" )
		else:
			print( current_value, " no change")
			
		last_value = current_value
		
	print( "Increasing Count: ", increasing_count )
	print( "Decreasing Count: ", decreasing_count )
		
	
	
if __name__ == '__main__':
	main( 'day1a_input.txt' )