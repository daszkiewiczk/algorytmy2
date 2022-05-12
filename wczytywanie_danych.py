import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import scipy as sp
from scanline import czy_przynalezy
from punkt import Punkt
from otoczka import znajdz_otoczke

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
    #edge_labels = nx.get_edge_attributes(G, 'capacity')
    nx.draw_networkx_edge_labels(G, pos)
    plt.show()

def znajdz_otoczki_cwiartek():
    #pdo - punkty definiujace otoczki
    #pdo znajduja sie w pliku pdo.txt
    pdo_file = open("pdo.txt","r")
    pdo = list()
    n = [int(el) for el in pdo_file.readline().split(" ")]
    #print(n)
    for i in range(4):
        pdo_tmp = list()
        for j in range(n[i]):
            pkt_lst = [float(el) for el in pdo_file.readline().split(" ")]
            #print(pkt_lst)
            pdo_tmp.append(Punkt(pkt_lst[0], pkt_lst[1]))
        pdo.append(pdo_tmp)
    otoczki = list()
    for i in range(4):
        otoczki.append(znajdz_otoczke(pdo[i]))
    return otoczki

if __name__ == '__main__':
    plik = open("dane.txt","r")
    n_string = plik.readline().split(" ")
    n_pol = int(n_string[0]) 			    #ile jest pól jęczmienia
    #n_jeczmienia = float(n_string[1]) 	    #ile średnio jęczmienia wyrasta na jednym poletku
    n_browarow = int(n_string[1])		    #ile browarów, z których każdy może przetworzyć określoną liczbę jęczmienia
    n_karczm = int(n_string[2])             #ile jest karczm
    j2b_przelicznik = float(n_string[3]) 	#w każdym z browarów z tony jęczmienia uzyskuje się jednakową ilość piwa
    n_skrzyzowan = int(n_string[4])		    #ile skrzyzowan

    przepustowosc_cwiartki = list()
    otoczki = znajdz_otoczki_cwiartek()

    G = nx.DiGraph()
    nowe_przepustowosci_browarow = dict()
    G2 = nx.DiGraph()

    for i in range(0,5):
        przepustowosc_cwiartki.append(float(plik.readline()))
    #ponizej wersja dodawania przepustowosci bez rozroznienia na cwiartki
    #for i in range(1,n_pol+1):
    #    G.add_edge("S", "p"+str(i), capacity=n_jeczmienia)
    for i in range(1,n_pol+1):
        linia = plik.readline()
        x = float(linia.split(" ")[0])
        y = float(linia.split(" ")[1])
        p = Punkt(x,y)
        if czy_przynalezy(p, otoczki[0]):
            G.add_edge("S", "p"+str(i), capacity=przepustowosc_cwiartki[0])
        elif czy_przynalezy(p, otoczki[1]):
            G.add_edge("S", "p"+str(i), capacity=przepustowosc_cwiartki[1])
        elif czy_przynalezy(p, otoczki[2]):
            G.add_edge("S", "p"+str(i), capacity=przepustowosc_cwiartki[2])
        elif czy_przynalezy(p, otoczki[3]):
            G.add_edge("S", "p"+str(i), capacity=przepustowosc_cwiartki[3])
        else:
            G.add_edge("S", "p"+str(i), capacity=przepustowosc_cwiartki[4])
    print(G.edges("S","capacity"))
    for i in range(1,n_browarow+1):
        nazwa_browaru = "b"+str(i)
        G.add_edge(nazwa_browaru, "T", capacity=float(plik.readline()))
        nowe_przepustowosci_browarow[nazwa_browaru] = 0
    for i in range(n_skrzyzowan):
        linia = plik.readline().split(" ")
        G.add_edge(linia[0], linia[1], capacity=(float)(linia[2]), weight = int(linia[4]))
        G2.add_edge(linia[0], linia[1], capacity=(float)(linia[3]), weight = int(linia[4]))

    drukuj_graf(G)

    mincostFlowDict = nx.max_flow_min_cost(G, "S", "T")
    mincost = nx.cost_of_flow(G, mincostFlowDict)
    print(mincostFlowDict)
    for src,src_info in mincostFlowDict.items():
        for key in src_info:
             if(key == 'T'):
                 #print(src, end=" ")
                 #print(key, end=" ")
                 #print(src_info[key])
                 nowe_przepustowosci_browarow[src] = src_info[key]
    #print(flow_dict)
    mincostFlowValue = sum((mincostFlowDict[u]["T"] for u in G.predecessors("T"))) - sum((mincostFlowDict["T"][v] for v in G.successors("T")))
    print("wartosc przeplywu z pol do browarow " + str(mincostFlowValue))
    print("koszt naprawy drog po dostarczeniu zboza do browarow: "+ str(mincost))
    #ponizsze niepotrzebne ze wzgledu na utworzenie dwoch grafow
    #G.remove_node('S')
    #G.remove_node('T')
    for browar in nowe_przepustowosci_browarow:
        G2.add_edge("S2",browar,capacity=float(nowe_przepustowosci_browarow[browar]) * j2b_przelicznik)    #z okreslonej ilosci zboza wytwarzamy okreslona ilosc browaru wiec trzeba przelczyc
    for i in range(1,n_karczm+1):
        nazwa_karczmy = "k"+str(i)
        G2.add_edge(nazwa_karczmy, "T2")  #zakładamy że przepustowość z karczmy do ujścia jest nieskończona
    drukuj_graf(G2)

    mincostFlowDict = nx.max_flow_min_cost(G2, "S2", "T2")
    mincostFlowValue = sum((mincostFlowDict[u]["T2"] for u in G2.predecessors("T2"))) - sum((mincostFlowDict["T2"][v] for v in G2.successors("T2")))
    mincost2 = nx.cost_of_flow(G2, mincostFlowDict)
    print("wartosc przeplywu z browarow do karczm "+str(mincostFlowValue))
    print("koszt naprawy drog zeby dostarczyc browar do karczm "+ str(mincost2))
    print("laczny koszt naprawy drog: "+str(mincost+mincost2))