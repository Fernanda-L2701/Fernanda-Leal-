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
    print("\nWrite 0 to stop process")
    x = float(input(f"Introduce x{n}:"))             
    listx.append(x)
    if x != 0:
        y = float(input(f"Introduce y{n}:"))
        listy.append(y)
        sumY+=y
        datos+=1
        n+=1
    else: i+=1
media=sumY/datos #Promedio                                                                   

for j in listy:                                                                          
    aparece = listy.count(j)                                                             
    if aparece > repetir:                                                       
        repetir = aparece                                                       
moda=[]                                                                              
for j in listy:                                                                              
    aparece = listy.count(j)                                                             
    if aparece == repetir and j not in moda:                                   
        moda.append(j)
        
lista = [(listy[p]-media)**2   #desviacion
                   for p in range(len(listy))]
suma=sum(lista)
s2=suma/(datos-1)
s=s2**.5

q= int(input("si desa la moda, media y desviacion estandar preciona 1, si no presiona 2 "))
if q==1:
    print(f"Sample mean:{media}")
    print(f"Mode:{moda}")
    print(f"Standard deviation:{s}")
elif q==2:
    a=int (input(" que desea calcular ? 1: moda, 2: media, 3: desviacion estandar"))
    if a==1:
        print(f"Mode:{moda}")
    elif a==2:
        print(f"Sample mean:{media}")
    else:
        print(f"Standard deviation:{s}")
        
            
        
            
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




