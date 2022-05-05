import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import scipy as sp

def drukuj_graf(G):
    options = {
        "font_size": 10,
        "node_size": 500,
        "node_color": "pink",
        "edgecolors": "black",
        "linewidths": 2,
        "width": 2,
    }
    pos = nx.kamada_kawai_layout(G)
    nx.draw(G, pos, with_labels=True)
    edge_labels = nx.get_edge_attributes(G, 'capacity')
    nx.draw_networkx_edge_labels(G, pos)
    plt.show()


plik = open("dane.txt","r")
pierwsza_linia = plik.readline()
n_pol = pierwsza_linia.split(" ")[0] 			#ile jest pól jęczmienia
n_jeczmienia = pierwsza_linia.split(" ")[1] 	#ile średnio jęczmienia wyrasta na jednym poletku
n_browarow = pierwsza_linia.split(" ")[2] 		#ile browarów, z których każdy może przetworzyć określoną liczbę jęczmienia
n_karczm = pierwsza_linia.split(" ")[3]         #ile jest karczm
j2b_przelicznik = pierwsza_linia.split(" ")[4] 	#w każdym z browarów z tony jęczmienia uzyskuje się jednakową ilość piwa
n_skrzyzowan = pierwsza_linia.split(" ")[5]		#ile skrzyzowan

n_pol = int(n_pol)
n_jeczmienia = int(n_jeczmienia)
n_browarow = int(n_browarow)
j2b_przelicznik = float(j2b_przelicznik)
n_skrzyzowan = int(n_skrzyzowan)
n_karczm = int(n_karczm)

G = nx.DiGraph()

nowe_przepustowosci_browarow = dict()
for i in range(1,n_pol+1):
    G.add_edge("S", "p"+str(i), capacity=n_jeczmienia)
for i in range(1,n_browarow+1):
    nazwa_browaru = "b"+str(i)
    G.add_edge(nazwa_browaru, "T", capacity=int(plik.readline()))
    nowe_przepustowosci_browarow[nazwa_browaru] = 0
for i in range(n_skrzyzowan):
    linia = plik.readline()
    G.add_edge(linia.split(" ")[0], linia.split(" ")[1], capacity=(int)(linia.split(" ")[2]))
drukuj_graf(G)
flow_value, flow_dict = nx.maximum_flow(G, "S", "T")

for src,src_info in flow_dict.items():
    for key in src_info:
         if(key == 'T'):
             #print(src, end=" ")
             #print(key, end=" ")
             #print(src_info[key])
             nowe_przepustowosci_browarow[src] = src_info[key]
print(flow_dict)
print("wartosc przeplywu z pol do browarow " + str(flow_value))
G.remove_node('S')
G.remove_node('T')
for browar in nowe_przepustowosci_browarow:
    G.add_edge("S2",browar,capacity=int(nowe_przepustowosci_browarow[browar]) * j2b_przelicznik)    #z okreslonej ilosci zboza wytwarzamy okreslona ilosc browaru wiec trzeba przelczyc
for i in range(1,n_karczm+1):
    nazwa_karczmy = "k"+str(i)
    G.add_edge(nazwa_karczmy, "T2")  #zakładamy że przepustowość z karczmy do ujścia jest nieskończona
#for browar in nowe_przepustowosci_browarow:
drukuj_graf(G)

flow_value, flow_dict = nx.maximum_flow(G, "S2", "T2")
print("wartosc przeplywu z browarow do karczm "+str(flow_value))