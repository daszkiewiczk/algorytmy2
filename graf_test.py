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
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    # edge_labels = nx.get_edge_attributes(G, 'capacity')
    nx.draw_networkx_edge_labels(G, pos,label_pos=0.75)
    plt.show()


def znajdz_otoczki_cwiartek():
    # pdo - punkty definiujace otoczki
    # pdo znajduja sie w pliku pdo.txt
    pdo_file = open("pdo.txt", "r")
    pdo = list()
    n = [int(el) for el in pdo_file.readline().split(" ")]
    # print(n)
    for i in range(4):
        pdo_tmp = list()
        for j in range(n[i]):
            pkt_lst = [float(el) for el in pdo_file.readline().split(" ")]
            # print(pkt_lst)
            pdo_tmp.append(Punkt(pkt_lst[0], pkt_lst[1]))
        pdo.append(pdo_tmp)
    otoczki = list()
    for i in range(4):
        otoczki.append(znajdz_otoczke(pdo[i]))
    return otoczki


if __name__ == '__main__':


    przepustowosc_cwiartki = list()
    otoczki = znajdz_otoczki_cwiartek()

    G = nx.DiGraph()
    nowe_przepustowosci_browarow = dict()
    G2 = nx.DiGraph()






    G.add_edge("b1", "b2", capacity=float(10), weight=int(10))
    #G.add_edge("b1", "b2", capacity=float(20), weight=int(12))
    #G.add_edge("b2", "b1", capacity=float(30), weight=int(2))
    G.add_edge("b2", "b3", capacity=float(3), weight=int(23))

    drukuj_graf(G)

    mincostFlowDict = nx.max_flow_min_cost(G, "S", "T")
    mincost = nx.cost_of_flow(G, mincostFlowDict)
    print(mincostFlowDict)
    for src, src_info in mincostFlowDict.items():
        for key in src_info:
            if (key == 'T'):
                # print(src, end=" ")
                # print(key, end=" ")
                # print(src_info[key])
                nowe_przepustowosci_browarow[src] = src_info[key]
    # print(flow_dict)
    mincostFlowValue = sum((mincostFlowDict[u]["T"] for u in G.predecessors("T"))) - sum(
        (mincostFlowDict["T"][v] for v in G.successors("T")))
    print("wartosc przeplywu z pol do browarow " + str(mincostFlowValue))
    print("koszt naprawy drog po dostarczeniu zboza do browarow: " + str(mincost))
    # ponizsze niepotrzebne ze wzgledu na utworzenie dwoch grafow
    # G.remove_node('S')
    # G.remove_node('T')
    for browar in nowe_przepustowosci_browarow:
        G2.add_edge("S2", browar, capacity=float(nowe_przepustowosci_browarow[
                                                     browar]) * j2b_przelicznik)  # z okreslonej ilosci zboza wytwarzamy okreslona ilosc browaru wiec trzeba przelczyc
    #for i in range(1, n_karczm + 1):
    #    nazwa_karczmy = "k" + str(i)
    #    G2.add_edge(nazwa_karczmy, "T2")  # zakładamy że przepustowość z karczmy do ujścia jest nieskończona
    #drukuj_graf(G2)

    mincostFlowDict = nx.max_flow_min_cost(G2, "S2", "T2")
    mincostFlowValue = sum((mincostFlowDict[u]["T2"] for u in G2.predecessors("T2"))) - sum(
        (mincostFlowDict["T2"][v] for v in G2.successors("T2")))
    mincost2 = nx.cost_of_flow(G2, mincostFlowDict)
    print("wartosc przeplywu z browarow do karczm " + str(mincostFlowValue))
    print("koszt naprawy drog zeby dostarczyc browar do karczm " + str(mincost2))
    print("laczny koszt naprawy drog: " + str(mincost + mincost2))
