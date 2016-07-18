from shortestPath import *
from networkFillStandby import *
from greenerNetwork import *



G = nx.DiGraph();


# deviceProfile = [energyConsumption, (renewableEnergyUsage * energyConsumption), wattPerMb]
redDevicesMetrics = [50, (0.5*50), 1]
blueDevicesMetrics = [60, (0.8*60), 0.5]
blackDevicesMetrics = [10, (0.05*10), 2]


G.add_node(0, energyConsumption=redDevicesMetrics[0], renewableEnergyUsage=redDevicesMetrics[1], wattPerMb=redDevicesMetrics[2], on=True)
G.add_node(1, energyConsumption=redDevicesMetrics[0], renewableEnergyUsage=redDevicesMetrics[1], wattPerMb=redDevicesMetrics[2], on=True)
G.add_node(2, energyConsumption=redDevicesMetrics[0], renewableEnergyUsage=redDevicesMetrics[1], wattPerMb=redDevicesMetrics[2], on=True)
G.add_node(3, energyConsumption=redDevicesMetrics[0], renewableEnergyUsage=redDevicesMetrics[1], wattPerMb=redDevicesMetrics[2], on=True)



##### Edges


G.add_edge(0, 3, capacity=100, flow = 0)

G.add_edge(0, 2, capacity=100, flow = 0)
G.add_edge(0, 1, capacity=100, flow = 0)
G.add_edge(1, 3, capacity=100, flow = 0)
G.add_edge(2, 3, capacity=100, flow = 0)




print(simulate(G, "renewableEnergyUsage", 0, 3, 1))
print(simulate(G, "renewableEnergyUsage", 0, 3, 1))


# nx.draw_random(G)
# nx.draw_circular(G)
# nx.draw_spectral(G)
# plt.show()