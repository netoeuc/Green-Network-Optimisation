import networkx as nx
from networkx.algorithms.flow import edmonds_karp
from networkx.algorithms import *
import matplotlib.pyplot as plt



import copy


def adaptNetwork(metric, G, source, target, flow, variance=0):
	nodesToBeTurnedOff = standbyActivation(metric, G, source, target, flow, variance)
	G = turnNodesOff(G, nodesToBeTurnedOff)
	return (get_network_statistics(G))


def turnNodesOff(G, nodesToBeTurnedOff):
	for i in G.nodes():
		G.node[i]["on"] = True
	for i in nodesToBeTurnedOff:
		G.node[i]["on"] = False
	return G




def get_network_statistics(G):
	energyConsumption, renewableEnergyUsage, wattPerMb, workingDevices= 0, 0, 0, 0.0;
	for i in G.nodes():
		if (G.node[i]["on"]):
			workingDevices+= 1;
			energyConsumption+=G.node[i]["energyConsumption"]
			renewableEnergyUsage+=G.node[i]["renewableEnergyUsage"]
			wattPerMb+=G.node[i]["wattPerMb"]
	meanWattPerMb = wattPerMb/workingDevices;
	return {'energyConsumption': energyConsumption, 'renewableEnergyUsage': renewableEnergyUsage, 'meanWattPerMb': meanWattPerMb}
	# return [energyConsumption, renewableEnergyUsage, meanWattPerBit]














def standbyActivation(metric, G, source, target, flow, variance=0):
	result = []
	if (flow+variance)>=nx.maximum_flow_value(G, source, target):
		return result
	else:
		if (metric=="energyConsumption"):
			list = sort_path_by_energyConsumption(G, source, target)
			remainingFlow = flow+variance;
			currentPath = 0;
			turnedOnDevices = []
			for i in range(len(list)):
				currentPath+=1;
				turnedOnDevices+=list[i]
				subgraph = G.subgraph(list[i])
				remainingFlow-=nx.maximum_flow_value(subgraph, source, target)
				if not(remainingFlow<=0):
					continue
				else:
					break
			while(currentPath<len(list)):
				result+=list[currentPath]
				currentPath+=1;
			result = [x for x in result if x not in turnedOnDevices]
			return result


		elif (metric=="renewableEnergyUsage"):
			list = sort_path_by_renewableEnergyUsage(G, source, target)
			remainingFlow = flow+variance;
			currentPath = 0;
			turnedOnDevices = []

			for i in range(len(list)):
				currentPath+=1;
				turnedOnDevices+=list[i]
				subgraph = G.subgraph(list[i])
				remainingFlow-=nx.maximum_flow_value(subgraph, source, target)
				if not(remainingFlow<=0):
					continue
				else:
					break
			while(currentPath<len(list)):
				result+=list[currentPath]
				currentPath+=1;
			result = [x for x in result if x not in turnedOnDevices]
			return result


		elif (metric=="wattPerMb"):
			list = sort_path_by_wattPerMb(G, source, target)
			remainingFlow = flow+variance;
			currentPath = 0;
			turnedOnDevices = []

			for i in range(len(list)):
				currentPath+=1;
				turnedOnDevices+=list[i]
				subgraph = G.subgraph(list[i])
				remainingFlow-=nx.maximum_flow_value(subgraph, source, target)
				if not(remainingFlow<=0):
					continue
				else:
					break
			while(currentPath<len(list)):
				result+=list[currentPath]
				currentPath+=1;
			result = [x for x in result if x not in turnedOnDevices]
			return result
		


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

	return sortedList







