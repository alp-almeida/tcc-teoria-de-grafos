# -*- coding: utf-8 -*-

import copy

from node_map import *
from cities import *

 
current_route_step_by_step = []
current_route_distance = 0
smaller_route_distance = 1000000
smaller_route_step_by_step = []


# jogar os globais nos parametros da funcao dijkstra com inicializacao padrao, e chamar a funcao com o cabecalho completo apenas dentro da funcao.

#-------------------| Defining methods |-------------------------
 
def list_duplicator(_list):
	clone = []
	for line in _list: clone.append(line[:])
	return clone
 
def dijkstra( start_node
            , stop_node
			,_node_map
			, current_route_step_by_step = []
			, current_route_distance = 0
			, smaller_route_distance = 1000000
			, smaller_route_step_by_step = []
):

	#print(start_node,stop_node,current_route_distance,smaller_route_distance)

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
		smaller_route_distance , smaller_route_step_by_step = dijkstra(   next_node,  stop_node,
					list_duplicator(_node_map), 
					list_duplicator(current_route_step_by_step) , 
					current_route_distance , 
					smaller_route_distance , 
					list_duplicator(smaller_route_step_by_step) )
		current_route_distance -= next_node_distance
		current_route_step_by_step.pop()
	return [smaller_route_distance , smaller_route_step_by_step]

