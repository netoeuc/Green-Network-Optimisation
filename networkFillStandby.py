from greenerNetwork import *


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
		elif (metric=="renewableEnergyUsage"):
		elif (metric=="wattPerMb"):
		result = 
