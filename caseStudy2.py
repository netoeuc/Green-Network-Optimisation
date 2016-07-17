from shortestPath import *
from networkFillStandby import *
from greenerNetwork import *



G = nx.DiGraph();


# deviceProfile = [energyConsumption, (renewableEnergyUsage * energyConsumption), wattPerMb]
redDevicesMetrics = [50, (0.5*50), 1]
blueDevicesMetrics = [60, (0.8*60), 0.5]
blackDevicesMetrics = [10, (0.05*10), 2]



for i in range(37):
	if (i in [1,2,3,4,7,8,14,24,29,30,31,33,35]):
		G.add_node(i, energyConsumption=redDevicesMetrics[0], renewableEnergyUsage=redDevicesMetrics[1], wattPerMb=redDevicesMetrics[2], on=True)		
	elif (i in [0,5,6,9,11,12,13,16,17,18,19,25,26,28,36]):
		G.add_node(i, energyConsumption=blueDevicesMetrics[0], renewableEnergyUsage=blueDevicesMetrics[1], wattPerMb=blueDevicesMetrics[2], on=True)
	else:
		G.add_node(i, energyConsumption=blackDevicesMetrics[0], renewableEnergyUsage=blackDevicesMetrics[1], wattPerMb=blackDevicesMetrics[2], on=True)



##### Edges

G.add_edge(0, 1, capacity=1024, flow = 0)
G.add_edge(0, 8,  capacity=100, flow = 0)
G.add_edge(0, 15, capacity=100, flow = 0)
G.add_edge(0, 22,  capacity=100, flow = 0)
G.add_edge(0, 29, capacity=100, flow = 0)

G.add_edge(1,  2,   capacity=100, flow = 0)
G.add_edge(8,  9,   capacity=100, flow = 0)
G.add_edge(15, 16,  capacity=100, flow = 0)
G.add_edge(22, 23, capacity=1024, flow = 0)
G.add_edge(29, 30,  capacity=100, flow = 0)


G.add_edge(2,   3,  capacity=100, flow = 0)
G.add_edge(9,  10,  capacity=100, flow = 0)
G.add_edge(16, 17,  capacity=100, flow = 0)
G.add_edge(23, 24, capacity=1024, flow = 0)
G.add_edge(30, 31,  capacity=100, flow = 0)

G.add_edge(3,   4,  capacity=100, flow = 0)
G.add_edge(10, 11,  capacity=100, flow = 0)
G.add_edge(17, 18,  capacity=100, flow = 0)
G.add_edge(24, 25, capacity=1024, flow = 0)
G.add_edge(31, 32,  capacity=100, flow = 0)

G.add_edge(4,   5,  capacity=100, flow = 0)
G.add_edge(11, 12,  capacity=100, flow = 0)
G.add_edge(18, 19,  capacity=100, flow = 0)
G.add_edge(25, 26, capacity=1024, flow = 0)
G.add_edge(32, 33,  capacity=100, flow = 0)



G.add_edge(5,   6,  capacity=100, flow = 0)
G.add_edge(12, 13,  capacity=100, flow = 0)
G.add_edge(19, 20,  capacity=100, flow = 0)
G.add_edge(26, 27, capacity=1024, flow = 0)
G.add_edge(33, 34,  capacity=100, flow = 0)



G.add_edge(6,   7,  capacity=100, flow = 0)
G.add_edge(13, 14,  capacity=100, flow = 0)
G.add_edge(20, 21,  capacity=100, flow = 0)
G.add_edge(27, 28, capacity=1024, flow = 0)
G.add_edge(34, 35,  capacity=100, flow = 0)


G.add_edge(7,  36,  capacity=100, flow = 0)
G.add_edge(14, 36,  capacity=100, flow = 0)
G.add_edge(21, 36,  capacity=100, flow = 0)
G.add_edge(28, 36, capacity=1024, flow = 0)
G.add_edge(35, 36,  capacity=100, flow = 0)


# print (G.node[0]['energyConsumption'])
flow_value = nx.maximum_flow_value(G, 0, 36)
# print(flow_value)
smallest = all_shortest_paths(G, 0, 36, "energyConsumption");
# print([p for p in smallest])

print("------")
print(get_network_statistics(G))
print("------")
print(adaptNetwork("energyConsumption", G, 0, 36, 100))
print(G.node[30])





# nx.draw_random(G)
# nx.draw_circular(G)
# nx.draw_spectral(G)
# plt.show()