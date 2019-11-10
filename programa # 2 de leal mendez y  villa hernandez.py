#!/usr/bin/env python
# coding: utf-8

# In[ ]:


i = 0
n = 1
datos=0
listx = []
listy = []
sumY=0
repetir=0
for k in range(0,2):
    x = float(input(f"Introduce x{n}:"))             
    listx.append(x)
    y = float(input(f"Introduce y{n}:"))                
    listy.append(y)
    sumY+=y
    n+=1
    datos+=1
while i < 1:
    print("\n escribe 0 para parar el proceso")
    x = float(input(f"Introduce x{n}:"))             
    listx.append(x)
    if x != 0:
        y = float(input(f"Introduce y{n}:"))
        listy.append(y)
        sumY+=y
        datos+=1
        n+=1
    else: i+=1
ordenaday=sorted(listy)
print(f"List Y:\n {listy}")
print(f"Ordered list Y:\n {ordenaday}")
a=int(input ("escribe el porcentaje que deseas aplicar:%"))
oldPromedio=sumY/datos
print(f"el total de la media es:\n {oldPromedio}")
pc=a*.01
pcOfData=pc*datos
pcToAplicate=pcOfData//1
reciduo=pcOfData%1
if reciduo  > .5:
    total=int(pcToAplicate+1)
elif reciduo <.5:
    total=int(pcToAplicate)
else:
    total=int(pcToAplicate)
print (f"numero de datos que eliminaste:\n{total}")
datos-=1
for d in range (total):
    ordenaday.pop(0)
    datos-=1
for t in range (total):
    ordenaday.pop(datos)
    datos-=1
datos+=1
print (f"la nueva lista de y es:\n{ordenaday}")
print (f"el nuevo numero de datos es:\n{datos}")
NuevaSumay=sum (ordenaday)
NewPromedio=NuevaSumay/datos
print (f"la meda es:\n{NewPromedio}")


# In[ ]:




