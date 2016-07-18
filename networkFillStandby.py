






def standbyActivation(metric, G, source, target, flow, variance=0):
	result = []
	if (flow+variance)>=nx.maximum_flow_value(G, source, target):
		return result
	else:
		if (metric=="energyConsumption"):
			list = sort_path_by_energyConsumption(G, source, target)
			remainingFlow = flow+variance;
			currentPath = 0;
			for i in range(len(list)):
				currentPath+=1;
				subgraph = G.subgraph(list[i])
				remainingFlow-=nx.maximum_flow_value(subgraph, source, target)
				if not(remainingFlow<=0):
					continue
				else:
					break
			while(currentPath<len(list)):
				result+=list[currentPath]
				currentPath+=1;
			return result


		elif (metric=="renewableEnergyUsage"):
			list = sort_path_by_renewableEnergyUsage(G, source, target)
			remainingFlow = flow+variance;
			currentPath = 0;
			for i in range(len(list)):
				currentPath+=1;
				subgraph = G.subgraph(list[i])
				remainingFlow-=nx.maximum_flow_value(subgraph, source, target)
				if not(remainingFlow<=0):
					continue
				else:
					break
			while(currentPath<len(list)):
				result+=list[currentPath]
				currentPath+=1;
			return result


		elif (metric=="wattPerMb"):
			list = sort_path_by_wattPerMb(G, source, target)
			remainingFlow = flow+variance;
			currentPath = 0;
			for i in range(len(list)):
				currentPath+=1;
				subgraph = G.subgraph(list[i])
				remainingFlow-=nx.maximum_flow_value(subgraph, source, target)
				if not(remainingFlow<=0):
					continue
				else:
					break
			while(currentPath<len(list)):
				result+=list[currentPath]
				currentPath+=1;
			return result
		
