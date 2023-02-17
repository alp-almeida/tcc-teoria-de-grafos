from node_map import node_map
from cities import cities
from original import *
 

#-------------------| Global Variables |-------------------------
#para processo
current_route_step_by_step = []
current_route_distance = 0
smaller_route_distance = 1000000
smaller_route_step_by_step = []

def run(initial_node , final_node):
	global current_route_step_by_step
	global current_route_distance 
	global smaller_route_distance 
	global smaller_route_step_by_step 

	current_route_step_by_step = []
	current_route_distance = 0
	smaller_route_distance = 1000000
	smaller_route_step_by_step = []

	if (initial_node in cities and final_node in cities):
		
		dijkstra(initial_node,final_node,list_duplicator(node_map))

		if (smaller_route_distance != 1000000):
			print(" Better route ..." , cities[initial_node],'->',cities[final_node] ,' | Distance:',round(smaller_route_distance,2),'kms')
			# Showing the results
			# print(' Smaller route :');
			# for node in smaller_route_step_by_step: print('\t',node)


#-------------------| Starting Process |----------------------

print("Starting process:")

for initial_node in cities:
	for final_node in cities:
		if initial_node != final_node:
			run(initial_node, final_node)

print('Ending process ...')