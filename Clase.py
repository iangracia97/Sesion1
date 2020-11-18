#!/usr/bin/env python
# coding: utf-8

# In[1]:


variable="Este curso python me gusta"


# In[2]:


len(variable)


# In[4]:


s.lower(variable)


# In[6]:


print(variable.upper())


# In[7]:


print(variable.lower())


# In[10]:


print("2+2=",(2+2))


# In[11]:


helado= input("Mi helado favorito es el de sirope de:")


# In[12]:


virutas= input("con virutas de:")


# In[14]:


print("Mi helado favorito es el de sirope de",helado,"con virutas de",virutas)


# In[1]:


frase="Mi helado favorito es este"


# In[2]:


print(frase.center(100,'-'))


# In[3]:


frase.count("e")


# In[6]:


len(frase.rsplit(sep=' '))


# Nombre2=input("Nombre:")

# #### Clase del martes 17 de noviembre
# 

# In[4]:


nombre2=input("Nombre: ")
Apellidos2=input("Apellidos:")
nombre_completo=nombre2+" "+Apellidos2
print(nombre_completo)
edad=22
nombre_completo=nombre_completo+str(edad)
print(nombre_completo)


# In[8]:


print(nombre_completo[8:])


# In[12]:


pos=eval(input("Dime una posicion:"))


# In[17]:


a="hola"
b="hola"
a=="hola"


# In[20]:


print("El caracter en la posicion %i es %c" % (pos,nombre_completo[pos-8]))


# In[21]:


colores="rojo,verde,amarillo,azul"
colores.split(",")


# In[23]:


color1,color2,color3,color4=colores.split(",")


# In[24]:


print(color1,color2,color3,color4)


# In[25]:


print("Los colores son %s,%s,%s y %s" % (color1,color2,color3,color4))


# In[26]:


cadena="aaabbbababababbbbaa"
cadena.replace("a","c")


# In[27]:


print(cadena)


# In[28]:


import math


# In[29]:


help(math.sqrt)


# In[30]:


print(math.sqrt(25))


# In[31]:


print(math.sqrt(90))


# In[32]:


print(math.sqrt(math.pi))


# In[34]:


print(math.factorial(10))


# In[40]:


from math import*
sqrt(25)
factorial(10)


# In[47]:


import datetime as dt
print(dt.datetime.now())
print(dt.date.today().weekday())


# In[48]:


ahora=dt.datetime.now()


# In[50]:


print(ahora.year,"/",ahora.month,"/",ahora.day)


# In[53]:


print("%i:%i:%i"%(ahora.hour,ahora.minute,ahora.second))


# In[54]:


import this 


# In[55]:


import mmap


# In[56]:


import statistics


# In[64]:


valores=3,4,5,6,7,8,4,23,44
from statistics import*
print(mean(valores))
print(median_low([3,6,5,4,4,4,3,3,3,]))
pstdev([5.6,5,.4,5.5])
pvariance([3,4,5,6,7,])
data=[4.8,9.3,7,6,8.9,9.1]
variance(data)


# In[65]:


getwd


# In[ ]:




