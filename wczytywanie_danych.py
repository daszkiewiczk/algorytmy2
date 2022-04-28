import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

plik = open("dane.txt","r")
first_line = plik.readline()
n_pol = first_line.split(" ")[0] 			#ile jest pól jęczmienia
n_jeczmienia = first_line.split(" ")[1] 	#ile średnio jęczmienia wyrasta na jednym poletku
n_browarow = first_line.split(" ")[2] 		#ile browarów, z których każdy może przetworzyć określoną liczbę jęczmienia
j2b_przelicznik = first_line.split(" ")[3] 	#w każdym z browarów z tony jęczmienia uzyskuje się jednakową ilość piwa
n_skrzyzowan = first_line.split(" ")[4]		#ile skrzyzowan

n_pol = int(n_pol)
n_jeczmienia = int(n_jeczmienia)
n_browarow = int(n_browarow)
j2b_przelicznik = int(j2b_przelicznik)
n_skrzyzowan = int(n_skrzyzowan)
#p = [0]*n
#z = [0]*m

G = nx.DiGraph()
#G = np.zeros((n+m+k,n+m+k))


for i in range(1,n_pol+1):
	G.add_edge("S", "p"+str(i), capacity=n_jeczmienia)
for i in range(1,n_browarow+1):
	G.add_edge("b"+str(i), "T", capacity=int(plik.readline()))
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

options = {
    "font_size": 10,
    "node_size": 500,
    "node_color": "pink",
    "edgecolors": "black",
    "linewidths": 2,
    "width": 2,
}
pos = nx.spring_layout(G, seed=3068)  # Seed layout for reproducibility
nx.draw(G, pos=pos, with_labels=True)
plt.show()
flow_value, flow_dict = nx.maximum_flow(G, "S", "T")
print(flow_value)
print(flow_dict)