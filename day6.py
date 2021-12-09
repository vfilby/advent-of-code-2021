#!/usr/bin/env python
import os
import re
import sys
import copy

new_spawn_time = 9
existing_spawn_time = 7
			
			
def ring_math( zero_day, increment ):
	return (zero_day+increment) % (existing_spawn_time)

def print_ring( ring, zero_day ):
	print(*["{:4d}".format(i%(existing_spawn_time)) for i in range( -zero_day, -zero_day+existing_spawn_time)],
          *["{:4d}".format(i) for i in range(existing_spawn_time,new_spawn_time)])
	print(*["{:04d}".format(i) for i in ring], "Total Fish: {0}".format(sum(ring)))
	
def main( filename ):
	
	ring = [0] * new_spawn_time
	
	with open(filename, 'r') as fp:
		line = fp.readline()
		
		initial_state = list( map( lambda x: int(x), line.strip().split(',') ) )
		
		print(initial_state)
		for fish in initial_state:
			ring[fish] += 1
			
		print(ring)
		
		for i in range(257):
			print("--------\nAfter {0} Day".format(i))
			zero_day = ring_math(0, i)
			
			to_spawn = ring[zero_day]
			print_ring(ring, zero_day)
			
			# Cray cray ring math time.  Only the first 6 elements are part of the ring, 7 and 8 
			# just feed in and need to be handled separately.  
			
			# move fixed 7 to relative 6
			relative_6 = ring_math(zero_day, existing_spawn_time)
			ring[relative_6] += ring[-2]
			
			# move fixed 8 to fixed 7
			ring[-2] = ring[-1]
			
			# create spawn at 8
			ring[-1] = to_spawn

		
if __name__ == '__main__':
	main( 'day5_input.txt' )
	