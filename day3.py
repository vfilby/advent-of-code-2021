#!/usr/bin/env python
import os
import re
import sys
import copy


def main( filename ):
	
	lines = []
	with open(filename, 'r') as fp:
		lines = fp.readlines()
	
	total = float(len(lines))
	digits = len(lines[0])
	one_count = []
	
	for i in range( 0, digits  - 1):
		one_count.append( 0 )
	
	print(one_count)
	
	for line in lines:
		for i in range( 0, digits - 1):
			if line[i] == '1':
				one_count[i] += 1
	
	print(one_count)
	
	gamma = [round((x/total)) for x in one_count]
	print(gamma)
	
	epsilon = [1 - round((x/total)) for x in one_count]
	print(epsilon)	
	
	gamma_value = int("".join(str(x) for x in gamma), 2)
	epsilon_value = int("".join(str(x) for x in epsilon), 2)
	
	print( "Gamma:",  gamma_value)
	print( "Epsilon:", epsilon_value )
	print( "Power Consumption:", gamma_value * epsilon_value)
		
	o2_values = lines.copy()
	co2_values = lines.copy()
	possible_values = [ '0', '1']
	o2_value = None
	co2_value = None
	
	for i in range( 0, digits - 1):
		#print('i:', i)
		#print('o2_values:', o2_values)
		o2_slice = [o2_values[n][i] for n in range(len(o2_values))]
		o2_counts = {v:o2_slice.count(v) for v in possible_values}
		
		# Duplicate values, the most frequent bit is equal to the total
		if o2_counts['0'] == len(o2_values) or o2_counts['1'] == len(o2_values):
			o2_value = o2_values[0]
			break;		
		
		o2_most_frequent = '0' if o2_counts['0'] > o2_counts['1'] else '1'
		o2_new_values = filter( lambda l: l[i] == o2_most_frequent, o2_values)
		o2_values = list(o2_new_values)
		#print('o2_slice:', o2_slice, o2_counts, o2_most_frequent)
		#print('o2_values filtered:', o2_values)
		
		if len(o2_values) == 1:
			o2_value = o2_values[0]
			break;
	
	for i in range( 0, digits - 1):
		#print( 'i:', i, len(co2_values))
		#print('co2_values:', co2_values)
		co2_slice = [co2_values[n][i] for n in range(len(co2_values))]
		co2_counts = {v:co2_slice.count(v) for v in possible_values}
		
		# Duplicate values, the most frequent bit is equal to the total
		if co2_counts['0'] == len(co2_values) or co2_counts['1'] == len(co2_values):
			co2_value = co2_values[0]
			break;		
			
		co2_most_frequent = '1' if co2_counts['1'] < co2_counts['0'] else '0'
		co2_new_values = filter( lambda l: l[i] == co2_most_frequent, co2_values)
		co2_values = list(co2_new_values)
		#print('co2_slice:', co2_slice, co2_counts, co2_most_frequent)
		#print('co2_values filtered:', co2_values)
		
	
	print(int(o2_value,2), int(co2_value,2))
	print('Life Support:', int(o2_value,2) * int(co2_value,2))
	
if __name__ == '__main__':
	main( 'day3_input.txt' )