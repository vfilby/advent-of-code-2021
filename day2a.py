#!/usr/bin/env python
import os
import re
import sys


def main( filename ):
	
	decreasing_count = 0
	increasing_count = 0
	values = []
	
	distance = 0
	depth = 0
	aim = 0
	
	with open(filename, 'r') as fp:
		input = fp.readline()
		while input:
			m= re.match( '(?P<command>[a-zA-Z]+)\s+(?P<param>\d+)', input)
			if m:
				print(distance, depth, aim)
				param = int(m['param'])
				print(m['command'],param)
				
				
				if m['command'] == 'forward':
					distance += param
					depth += (aim * param)
				if m['command'] == 'up':
					aim = max( 0, aim - param)
				if m['command'] == 'down':
					aim += param
				
					
			input = fp.readline()
	print( distance, depth)
	print( distance * depth )
	
	
if __name__ == '__main__':
	main( 'day2a_input.txt' )