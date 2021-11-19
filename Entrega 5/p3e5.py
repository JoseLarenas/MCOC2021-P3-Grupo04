import matplotlib.pyplot as plt
import osmnx as ox
import geopandas as gps
import networkx as nx

def graficar(zonas, gdf_edges):
    fig, ax = plt.subplots(1,1) 
    zonas.plot(ax=ax,color='#CDCDCD')
    
    gdf_clipped = gps.clip(gdf_edges, zonas)
    motorway = gdf_clipped[gdf_clipped['highway'].isin(['motorway'])]
    primary = gdf_clipped[gdf_clipped['highway'].isin(['primary'])]
    secondary = gdf_clipped[gdf_clipped['highway'].isin(['secondary'])]
    tertiary = gdf_clipped[gdf_clipped['highway'].isin(['tertiary'])]
    
    motorway.plot(ax=ax,color='orange')
    primary.plot(ax=ax,color='yellow')
    secondary.plot(ax=ax,color='green')
    tertiary.plot(ax=ax,color='blue')
    gdf_clipped[gdf_clipped['name'].isin(['Autopista Vespucio Oriente'])].plot(ax=ax,color='red')
    
    fig.set_size_inches(18, 10)
    plt.title('Américo Vespucio Oriente')
    plt.savefig('fig_entrega_5',bbox_inches='tight')
    plt.show()

def main():
    zonas_gdf = gps.read_file('eod.json')
    ox.config(use_cache=True, log_console=True)
    zonas = nx.read_gpickle('zonas.gpickle')
    G = nx.read_gpickle('santiago_grueso.gpickle')    
    graficar(zonas_gdf[zonas_gdf['ID'].isin(zonas)], ox.graph_to_gdfs(G,nodes=False))

if __name__ == '__main__':
    main()