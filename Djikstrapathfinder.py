import osmnx as ox
import networkx as nx
import matplotlib as plt

#Definition des lieux d'intéret/ Define your places of intrest
adresse_depart = "Eiffel Tower, Paris, France"
adresse_arrivee = "Louvre Museum, Paris, France"

#Téléchargement du graphe routier/Downloading of the route's graph
G = ox.graph_from_address(adresse_depart, dist=2000, network_type="drive")

#Conversion des adresses en coordonnées/ conversion of the addresses into coordonnates 
coord_depart = ox.geocode(adresse_depart)
coord_arrivee = ox.geocode(adresse_arrivee)

#Récupération des meuds les plus proches/ closest nodes 
noeud_depart = ox.nearest_nodes(G, coord_depart[1], coord_depart[0])
noeud_arrivee = ox.nearest_nodes(G, coord_arrivee[1], coord_arrivee[0])

#Calcul du chemin le plus court/ calculating the shortest path
chemin = nx.dijkstra_path(G, noeud_depart, noeud_arrivee, weight='length')

#Préparation des coordonnées pour affichage/ prepping the coords for display
coordonnées_chemin = [(G.nodes[n]['x'], G.nodes[n]['y']) for n in chemin]

#Affichage du graphe et du trajet/ displaying the graph alongside the path
fig, ax = ox.plot_graph_route(
  G,
  chemin,
  route_linewidth=4,
  node_size=0,
  bgcolor='black',
  show= True,
  close=True
)
