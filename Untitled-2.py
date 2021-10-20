
import random

araye=[]
print("tedad adad morednazar ra vared konid :")
n=int(input())
for i in range(n):
    x=random.randint(0,1000)
    if x not in araye:
        araye.append(x)
print("araye az adad tasadofi :   ",araye)