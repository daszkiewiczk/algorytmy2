import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import scipy as sp

def drukuj_graf(G):
    pos = nx.kamada_kawai_layout(G)
    nx.draw(G, pos, with_labels=True)
    edge_labels = nx.get_edge_attributes(G, 'capacity')
    nx.draw_networkx_edge_labels(G, pos)
    plt.show()

plik = open("dane.txt","r")
first_line = plik.readline()
n_pol = first_line.split(" ")[0] 			#ile jest pól jęczmienia
n_jeczmienia = first_line.split(" ")[1] 	#ile średnio jęczmienia wyrasta na jednym poletku
n_browarow = first_line.split(" ")[2] 		#ile browarów, z których każdy może przetworzyć określoną liczbę jęczmienia
n_karczm = first_line.split(" ")[3]         #ile jest karczm
j2b_przelicznik = first_line.split(" ")[4] 	#w każdym z browarów z tony jęczmienia uzyskuje się jednakową ilość piwa
n_skrzyzowan = first_line.split(" ")[5]		#ile skrzyzowan

n_pol = int(n_pol)
n_jeczmienia = int(n_jeczmienia)
n_browarow = int(n_browarow)
j2b_przelicznik = int(j2b_przelicznik)
n_skrzyzowan = int(n_skrzyzowan)
n_karczm = int(n_karczm)
#p = [0]*n
#z = [0]*m

G = nx.DiGraph()
#G = np.zeros((n+m+k,n+m+k))

nowe_przepustowosci_browarow = dict()
for i in range(1,n_pol+1):
    G.add_edge("S", "p"+str(i), capacity=n_jeczmienia)
for i in range(1,n_browarow+1):
    nazwa_browaru = "b"+str(i)
    G.add_edge(nazwa_browaru, "T", capacity=int(plik.readline()))
    nowe_przepustowosci_browarow[nazwa_browaru] = 0
#print(G.out_edges)
for i in range(n_skrzyzowan):
    linia = plik.readline()
    #print(linia.split(" ")[0])
    G.add_edge(linia.split(" ")[0], linia.split(" ")[1], capacity=(int)(linia.split(" ")[2]))
    # if(linia[0] == "b"):
    # 	i = linia.split(" ")[1::]
    # elif(linia[0] == "s"):
    # 	i = int(linia.split(" ")[1::])+n
    # elif(linia[0] == "d"):
    # 	i = int(linia.split(" ")[1::])+n+k
    #
    # if(linia.split(" ")[1][0] == "b"):
    # 	j = int(linia.split(" ")[1][1::])
    # elif(linia.split(" ")[1][0] == "s"):
    # 	j = int(linia.split(" ")[1][1::])+n
    # elif(linia.split(" ")[1][0] == "d"):
    # 	j = int(linia.split(" ")[1][1::])+n+k
    # G[(i,j)] == (int)(linia.split(" ")[2])

#rysowanie reprezentacji graficznej grafu
options = {
    "font_size": 10,
    "node_size": 500,
    "node_color": "pink",
    "edgecolors": "black",
    "linewidths": 2,
    "width": 2,
}
#pos = nx.spring_layout(G, seed=3068)  # Seed layout for reproducibility
#pos = nx.nx_agraph.graphviz_layout(G)
drukuj_graf(G)
flow_value, flow_dict = nx.maximum_flow(G, "S", "T")
#print(flow_value)

for src,src_info in flow_dict.items():
    for key in src_info:
         if(key == 'T'):
             print(src, end=" ")
             print(key, end=" ")
             print(src_info[key])
             nowe_przepustowosci_browarow[src] = src_info[key]
print(flow_dict)
print(flow_value)
G.remove_node('S')
G.remove_node('T')
for browar in nowe_przepustowosci_browarow:
    print(browar,nowe_przepustowosci_browarow[browar])
    G.add_edge("S2",browar,capacity=int(nowe_przepustowosci_browarow[browar]))
for i in range(1,n_karczm+1):
    nazwa_karczmy = "k"+str(i)
    G.add_edge(nazwa_karczmy, "T2")  #zakładamy że przepustowość z karczmy do ujścia jest nieskończona
#for browar in nowe_przepustowosci_browarow:
#    G.add_edge("S",)
drukuj_graf(G)

flow_value, flow_dict = nx.maximum_flow(G, "S2", "T2")
print(flow_value)