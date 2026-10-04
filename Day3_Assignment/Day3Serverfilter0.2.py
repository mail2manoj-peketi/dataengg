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
def usageFilter(serverInventory) :
    highCpu, highDu = [], []
    for i in serverInventory :
        if (i.get("cpuusage")>=80) :
            highCpu.append(i.get("hostname"))  
        if(i.get("diskusage")>=80) :
            highDu.append(i.get("hostname"))     
    if(highCpu != []) :
        print(f"Servers found with high CPU Usage are : ")
        for i in highCpu :
            print(i)
    else :
        print("No servers with high CPU usage found")
    if(highDu != []) :
        print(f"Servers found with high Disk Usage are : ")
        for i in highDu :
            print(i)
    else : 
        print("No servers with high Disk usage found")
def prodFilter(serverInventory) :
    prodServers , critialProdServers = [] , []
    for i in serverInventory :
        if(i.get("environment") == "PROD") : 
            prodServers.append(i)
            if(i.get("cpuusage") >= 80 ) :
                critialProdServers.append(i)
    print(f"Prod Servers :")
    for i in prodServers :
        print(f"{i.get("hostname")}")
    print(f"Critical Prod Servers :")
    for i in critialProdServers :
        print(f"{i.get("hostname")}")
    return prodServers,critialProdServers
for i in range(10) :
    serverCreator(i)
for i in serverInventory :
    print(i)
usageFilter(serverInventory)
prodFilter(serverInventory)
# hc, hd = usageFilter(serverInventory)
# for i , k in hc, hd :
# print(f"Servers with High CPU Usage are as below :")
    

