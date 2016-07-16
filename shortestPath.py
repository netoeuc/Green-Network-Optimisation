from greenerNetwork import *



def sort_path_by_energyConsumption(G, source, target):
	list,list_values, temp_result = [p for p in all_shortest_paths(G, source, target, "energyConsumption")],[], 0; 
	for i in range(len(list)):
		for j in range(len(list[i])):
			temp_result+=G.node[list[i][j]]['energyConsumption']
		list_values+=[temp_result]
		temp_result = 0;
	list_values2,sortedList = copy.deepcopy(list_values),[]
	list_values.sort();
	for i in list_values:
		sortedList+=[list[list_values2.index(i)]]
	print
	print(list_values)
	return sortedList


def sort_path_by_renewableEnergyUsage(G, source, target):
	list,list_values, temp_result = [p for p in all_shortest_paths(G, source, target, "energyConsumption")],[], 0; 
	for i in range(len(list)):
		for j in range(len(list[i])):
			temp_result+=G.node[list[i][j]]['renewableEnergyUsage']
		list_values+=[temp_result]
		temp_result = 0;
	list_values2,sortedList = copy.deepcopy(list_values),[]
	list_values.sort();
	for i in list_values:
		sortedList+=[list[list_values2.index(i)]]
	print
	print(list_values)
	return sortedList


def sort_path_by_wattPerMb(G, source, target):
	list,list_values, temp_result = [p for p in all_shortest_paths(G, source, target, "energyConsumption")],[], 0; 
	for i in range(len(list)):
		for j in range(len(list[i])):
			temp_result+=G.node[list[i][j]]['wattPerMb']
		list_values+=[temp_result]
		temp_result = 0;
	list_values2,sortedList = copy.deepcopy(list_values),[]
	list_values.sort();
	for i in list_values:
		sortedList+=[list[list_values2.index(i)]]
	print
	print(list_values)
	return sortedList







