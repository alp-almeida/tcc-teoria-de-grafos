# -*- coding: utf-8 -*-
# https://www.tutorialspoint.com/execute_python3_online.php
import time
import copy

 
#-------------------| Definindo funções |-------------------------
 
def list_duplicator(_list):
	clone = []
	for line in _list: clone.append(line[:])
	return clone
 
def dijkstra(start_node,stop_node,_node_map):
	global smaller_route_distance
	global current_route_distance
	global smaller_route_step_by_step
    
	current_route_step_by_step.append(cities[start_node])
    
	while(sum(_node_map[start_node]) > 0 ):
		next_node_distance = min(distance for distance in _node_map[start_node] if distance != 0)
		next_node = _node_map[start_node].index(next_node_distance)
		_node_map[next_node][start_node]=0
		_node_map[start_node][next_node]=0
		if(current_route_distance + next_node_distance > smaller_route_distance):
				continue
		current_route_distance += next_node_distance
		if( next_node == stop_node ):
				if(current_route_distance < smaller_route_distance):
						current_route_step_by_step.append(cities[next_node])
						smaller_route_step_by_step = current_route_step_by_step[:]
						smaller_route_distance = current_route_distance
						current_route_step_by_step.pop()
		dijkstra(next_node,stop_node,list_duplicator(_node_map))
		current_route_distance -= next_node_distance
		current_route_step_by_step.pop()

#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------


