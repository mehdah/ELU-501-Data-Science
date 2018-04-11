# We are U19886

## Imports & pre-proceessing

import os
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import pylab
import numpy as np
import pickle

os.chdir('desktop/ELU 501 data science')

## Loading the graph

G = nx.read_gexf("mediumLinkedin.gexf")


## Loading the data

colleges = {}
locations = {}
employers = {}

with open('mediumCollege.pickle', 'rb') as handle:
    colleges = pickle.load(handle)
    
with open('mediumLocation.pickle', 'rb') as handle:
    locations = pickle.load(handle)
    
with open('mediumEmployer.pickle', 'rb') as handle:
    employers = pickle.load(handle)

    
## Seeking Google employees

google_employees = []

for person in employers:
    for employer in employers[person]:
        if employer == 'google':
            google_employees += [person]

nb_of_google_employees = len(google_employees)


## Registering Google employees informations

register = dict()

for employee in google_employees:
    
    college = None
    location = None
    
    if employee in colleges:
        college = colleges[employee][0]
        
    if employee in locations:
        location = locations[employee][0]
        
    register[employee] = [college, location]
    
## U19886 information

self = ['NoCollege', locations['U19886'][0]]

## U19886 to Google 

# Area

test = False
count = 0

for employee in register:
    test = 'rockford illinois area' in register[employee]
    if test == True:
        count += 1


# Shortest path

shortest_pathIG = {}

for employee in google_employees:
    shortest_pathIG[employee] = nx.shortest_path(G, 'U19886', employee)
    
# who is the nearest google employee ?

min = float('inf')
nearest = ['U19886', min] 

for employee in google_employees:
    L = len(shortest_pathIG[employee])
    if L < min:
        min = L
        nearest = [employee, L]


## Google to U19886

shortest_pathsGI = {}

for employee in google_employees:
    shortest_pathsGI[employee] = list(nx.all_shortest_paths(G, employee, 'U19886'))
    
nb_paths = {}

for employee in google_employees:
    nb_paths[employee] = len(shortest_pathsGI[employee])
    
##

list_nodes = []

for employee in shortest_pathsGI:        
    for path in shortest_pathsGI[employee]:
        for nodes in path:
            if not(nodes in list_nodes):
                list_nodes += [nodes]

H = G.subgraph(list_nodes)


##

nodes = list_nodes

k=0
while k < len(nodes):
    if nodes[k] == 'U19886':
        del nodes[k]
    k += 1

##

pos = nx.spring_layout(H, iterations = 1000)
nx.draw_networkx_nodes(H, pos, nodelist = ['U19886'], node_color = 'r', node_size = 20)
nx.draw_networkx_nodes(H, pos, nodelist = nodes, node_color = 'b', node_size = 20)
nx.draw_networkx_nodes(H, pos, nodelist = google_employees, node_color = 'g', node_size = 20)
nx.draw_networkx_edges(H, pos)
plt.axis('off')
plt.show()

# On voit que le no U7091 est un fdp

##

nx.draw_networkx(H, pos, node_size = 20, font_size = 9)
plt.show()

##

nodes1 = list(G.nodes)

k=0
while k < len(nodes1):
    if nodes1[k] == 'U7091':
        del nodes1[k]
    k += 1
    
P = G.subgraph(nodes1)

oefkp
