import networkx as nx
import numpy as np

zonas_avo = [146,683,666,682,677,287,307,288,291,289,290,304,266,684,599,153,590]

def zone(p1, p2):
    if p1 in zonas_avo:
        if p1 not in zonas:
            zonas.append(p1)
        if p2 not in zonas:
            zonas.append(p2)

OD, zonas = {}, []
for line in open('mod.csv'):
    sl = line.split(',')
    o, d, demanda = int(sl[0]), int(sl[1]), np.double(sl[2])
    if demanda > 100:
        zone(o, d), zone(d, o)
    OD[(o,d)] = demanda

for zone in zonas_avo:
    if zone not in zonas:
        zonas.append(zone)

print(f'Hay un total de {len(zonas)} que cumplen con una demanda mayor a 100, estas zonas son:\n{zonas}')
nx.write_gpickle(zonas, 'zonas.gpickle')