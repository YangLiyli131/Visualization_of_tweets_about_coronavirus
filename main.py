# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 20:36:50 2020
Last Updated: Apr 20
@author: Yang
"""

import networkx as nx
import pandas as pd
from networkx.algorithms import approximation as apxa
import operator
import matplotlib.pyplot as plt
import numpy as np
import csv 

# load data
nodes = pd.read_csv("nodes_corona.csv") 
edges = pd.read_csv("edges_corona.csv") 

# remove multiple undirected edges between pairs of nodes
Graphtype = nx.Graph()
G = nx.from_pandas_edgelist(edges, source = 'Source', target = 'Target', create_using=Graphtype)
G.add_nodes_from(nodes)
G.remove_edges_from(nx.selfloop_edges(G))

Graphtype = nx.DiGraph()
GG = nx.from_pandas_edgelist(edges, source = 'Source', target = 'Target', create_using=Graphtype)
GG.add_nodes_from(nodes)
GG.remove_edges_from(nx.selfloop_edges(GG))

#################
# degree
degree_cen = nx.algorithms.centrality.degree_centrality(G)
sorted_degree_cen = sorted(degree_cen.items(), key=operator.itemgetter(1), reverse = True)
List_degree_users = []
List_degree_values = []
for i in range(50):
    List_degree_users.append(sorted_degree_cen[i][0])
    List_degree_values.append(sorted_degree_cen[i][1])
    
y_pos = np.arange(len(List_degree_users[:10]))   
plt.figure(figsize=(16,9))
plt.bar(y_pos, List_degree_values[:10])
# Create names on the x-axis
plt.xticks(y_pos, List_degree_users[:10], rotation=-20)
plt.yticks([])
plt.title('Top 10')
# Show graphic
plt.savefig('degree_top10.png',dpi = 300)
plt.show()

y_pos = np.arange(len(List_degree_users[10:30]))   
plt.figure(figsize=(16,9))
plt.bar(y_pos, List_degree_values[10:30])
# Create names on the x-axis
plt.xticks(y_pos, List_degree_users[10:30], rotation=-20)
plt.yticks([])
plt.title('Top 10-30')
# Show graphic
plt.savefig('degree_top30.png', dpi = 300)
plt.show()
   
y_pos = np.arange(len(List_degree_users[30:50])) 
plt.figure(figsize=(16,9))  
plt.bar(y_pos, List_degree_values[30:50])
# Create names on the x-axis
plt.xticks(y_pos, List_degree_users[30:50], rotation=-20)
plt.yticks([])
plt.title('Top 30-50')
# Show graphic
plt.savefig('degree_top50.png', dpi = 300)
plt.show()

#################
# closeness centrality
closeness_cen = nx.algorithms.centrality.closeness_centrality(GG) 
sorted_closeness_cen = sorted(closeness_cen.items(), key=operator.itemgetter(1), reverse = True)
List_closeness_users = []
List_closeness_values = []
for i in range(50):
    List_closeness_users.append(sorted_closeness_cen[i][0])
    List_closeness_values.append(sorted_closeness_cen[i][1])

#################
# bridge edges
# A bridge in a graph is an edge whose removal causes the number of connected components of the graph to increase. 
# Equivalently, a bridge is an edge that does not belong to any cycle.
bridges = list(nx.bridges(G))

with open('edge_bridge.csv','w') as out:
    csv_out = csv.writer(out)
    csv_out.writerow(['Source','Target'])
    for row in bridges:
        csv_out.writerow(row)
        
bridges_freq = {}
for i in range(len(bridges)):
    node_name = bridges[i][0]
    if node_name not in bridges_freq:
        bridges_freq[node_name] = 1
    else:
        bridges_freq[node_name] = bridges_freq[node_name] + 1

sorted_bridges_freq = sorted(bridges_freq.items(), key=operator.itemgetter(1), reverse = True)

    
#################
#strong_components = nx.algorithms.components.strongly_connected_components(GG)
#weak_components = nx.algorithms.components.weakly_connected_components(GG)
#attract_components = nx.algorithms.components.attracting_components(GG)

