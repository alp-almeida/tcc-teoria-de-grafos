from node_map import *
from cities import *
from original import *
 

#-------------------| Global Variables |-------------------------

def run(initial_node , final_node):

	if (initial_node in cities and final_node in cities):
		
		distance , route = dijkstra(initial_node,final_node,list_duplicator(node_map))

		if (distance != 1000000):
			print(" Better route ..." , cities[initial_node],'->',cities[final_node] ,' | Distance:',round(distance,2),'kms')
			# Showing the results
			# print(' Smaller route :');
			# for node in smaller_route_step_by_step: print('\t',node)



print("Starting process:")

for initial_node in cities:
	for final_node in cities:
		if initial_node != final_node:
			run(initial_node, final_node)

print('Ending process ...')