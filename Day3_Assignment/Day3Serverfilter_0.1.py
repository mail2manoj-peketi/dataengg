#Day3Serverfilter.py
import random
from random import choice
serverInventory=[]

def serverCreator(i) :
    serverInventory.append({
                             "hostname" : f"app{i}",
                             "environment" : choice(['PROD','PREPROD']) , 
                             "status" : choice(['UP','DOWN']), 
                             "cpuusage" : random.randint(1,100) , 
                             "diskusage" : random.randint(1,100)
                             })

for i in range(10) :
    serverCreator(i)
for i in serverInventory :
    print(i)
