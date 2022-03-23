import numpy as np                                              
plik = open("dane.txt","r")
first_line = plik.readline()
n = first_line.split(" ")[0]
m = first_line.split(" ")[1]
k = first_line.split(" ")[2]
t = first_line.split(" ")[3]
#print(n,m,k,t)

n = int(n)
m = int(m)
k = int(k)
t = int(t)
p = [0]*n
z = [0]*m

graf = np.zeros((n+m+k,n+m+k))

for i in range(n):
	p[i] = plik.readline()
for i in range(m):
	z[i] = plik.readline()

for iterator in range(t):
	linia_przelywu = plik.readline()
	if(linia_przelywu[0] == "b"):
		i = linia_przelywu.split(" ")[1::]
	elif(linia_przelywu[0] == "s"):
		i = int(linia_przelywu.split(" ")[1::])+n
	elif(linia_przelywu[0] == "d"):
		i = int(linia_przelywu.split(" ")[1::])+n+k
		
	if(linia_przelywu.split(" ")[1][0] == "b"):
		j = int(linia_przelywu.split(" ")[1][1::])
	elif(linia_przelywu.split(" ")[1][0] == "s"):
		j = int(linia_przelywu.split(" ")[1][1::])+n
	elif(linia_przelywu.split(" ")[1][0] == "d"):
		j = int(linia_przelywu.split(" ")[1][1::])+n+k
	graf[(i,j)] == (int)(linia_przelywu.split(" ")[2])
