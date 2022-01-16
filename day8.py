#!/usr/bin/env python
import os
import re
import sys
import copy
import math
import string
import itertools
import numpy as np

# segment_config = {
# 	0: ['a','b','c','e','f','g'],
# 	1: ['c','f'],
# 	2: ['a','c','d','e','g'],
# 	3: ['a','c','d','f','g'],
# 	4: ['b','c','d','f'],
# 	5: ['a','b','d','f','g'],
# 	6: ['a','b','d','e','f','g'],
# 	7: ['a','c','f'],
# 	8: ['a','b','c','d','e','f','g'],
# 	9: ['a','b','c','d','f','g']
# }

# Indexing
#
#  0
# 1 2
#  3
# 4 5
#  6

segment_config = {
	0: [0,1,2,4,5,6],
	1: [2,5],
	2: [0,2,3,4,6],
	3: [0,2,3,5,6],
	4: [1,2,3,5],
	5: [0,1,3,5,6],
	6: [0,1,3,4,5,6],
	7: [0,2,5],
	8: [0,1,2,3,4,5,6],
	9: [0,1,2,3,5,6]
}

def position_to_char( position ):
	return char(ord('a')+position)
	
def get_segments_from_number( *numbers ):
	return list(itertools.chain(*[segment_config[x] for x in  numbers]))

def parse_input( filename ):
	with open(filename, 'r') as fp:
		lines = fp.readlines()
		
		displays = []
		for pattern, value in [l.split('|') for l in lines]:
			
			displays.append( 
				{ 
					'patterns': pattern.strip().split(' '),
					'values': value.strip().split(' ') 
				},
			)
			
		return displays
		
def count_uniques( displays ):
	c = 0
	for display in displays:
		for value in display['values']:
			if len(value) in [2,3,4,7]:
				c += 1
				
	print( "Count", c)
	
def filter_string( source, characters_to_filter ):
	translation_table = dict.fromkeys(map(ord, characters_to_filter), None)
	return source.translate(translation_table)
	
def get_patterns_by_length(patterns, length, contains=None):
	
	# pre-filter patterns if we have a contains
	filtered_patterns = []
	if contains:
		#print (patterns)
		for pattern in patterns:
			#print( "Checking '{0}' against '{1}'.".format(pattern,contains))
			#print( [c in pattern for c in list(contains)] )
			if False not in [c in pattern for c in list(contains)]:
				#print( "Match" )
				#print(pattern)
				filtered_patterns.append(pattern)
	else:
		filtered_patterns = patterns
		
	return [p for p in filtered_patterns if len(p) == length]
	
def decode_pattern(patterns):
	
	
	# Indexing
	#
	#  0
	# 1 2
	#  3
	# 4 5
	#  6
	
	possibles = [''] * 7
	
	# Step one, get 1 
	one = get_patterns_by_length(patterns, 2)[0]
	possibles[2] += one
	possibles[5] += one
	# print(possibles)
	
	# Step 2, get 7
	seven = get_patterns_by_length(patterns, 3)[0]
	seven_filtered = filter_string(seven, one)
	possibles[0] = seven_filtered
	# print(possibles)
	
	# Step three, get 4
	four = get_patterns_by_length(patterns, 4)[0]
	four_filtered = filter_string(four, ''.join([possibles[i] for i in [0,2,5]]))
	possibles[1] += four_filtered
	possibles[3] += four_filtered
	# print(possibles)
	
	# Step four, we should be able to positively identify the bottom segment
	# first identify the 9 by length and containing the 'four' and 'seven' segments 
	# to separate it from the 0 and the 6.
	one_four_segments = get_segments_from_number( 7,4 )
	one_four_possibles = ''.join( list(itertools.chain(*[possibles[x] for x in one_four_segments])) )
	#print( "1/4 segments", one_four_segments )
	#print( "1/4 possibles", one_four_possibles )
	nine = get_patterns_by_length(patterns, 6, contains=one_four_possibles )
	# print(nine)
	#print( "nine", nine)
	possibles[6] =  filter_string(nine[0], one_four_possibles)
	# print(possibles)
	
	# Step five we can identify segment four, by using parts of the 7 and 9
	eight = get_patterns_by_length( patterns, 7 )[0]
	step5_segments = get_segments_from_number(9)
	step5_possibles = ''.join( list(itertools.chain(*[possibles[x] for x in step5_segments])) )
	possibles[4] = filter_string(eight, step5_possibles)
	# print(possibles)
	
	# Step 6
	# find two using the length and the known segments
	# From this we should be able to set possibles 1, 2, 3, 5
	filter = possibles[0] + possibles[4] + possibles[6]	
	two = get_patterns_by_length(patterns, 5, filter)[0]
	# print(filter, two)
	for c in possibles[2]:
		if c in two:
			seg2 = c
		else: 
			seg5 = c
	possibles[2] = seg2
	possibles[5] = seg5
	# print(possibles)
	
	for c in possibles[1]:
		if c in two:
			seg3 = c
		else:
			seg1 = c
	possibles[1] = seg1
	possibles[3] = seg3
	# print(possibles)
			
	return possibles
	
def read_values( segments, values ):

	# Two step process, first map the alpha array to the corresponding segment
	# number. Second, map that to a digits.  To make digit look-ups easier 
	# convert the array to something easier to compare
	digit_lookup = {str(sorted(v)): str(k) for k,v in segment_config.items()}
	segment_lookup = {segments[i]: i for i in range(len(segments))}
	# print(digit_lookup)
	# print(segment_lookup)
	digits = ""
	
	for value in values:
		# print(value)
		segments = [segment_lookup[c] for c in value]
		# print(segments)
		lookup_key = str(sorted(segments))
		digits += digit_lookup[lookup_key]
		
	return int(digits)
	


def main( filename ):
	displays = parse_input(filename)
	
	sum = 0
	for display in displays:
		segments = decode_pattern(display['patterns'])
		value = read_values(segments, display['values'])
		# print(value)
		sum += value
		
	print( "sum:", sum)

		
if __name__ == '__main__':
	main( 'day8_input.txt' )
	