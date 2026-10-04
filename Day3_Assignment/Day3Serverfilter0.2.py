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
    highestCpu, highestDu = [],[]
    highestCpuInt, highestDuInt = 0,0
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
#===========TO find highest usage=======================
    for i in serverInventory :
        if i.get("cpuusage")> highestCpuInt :
                        highestCpu = i
                        highestCpuInt = i.get("cpuusage")
        if i.get("diskusage")> highestDuInt :
                        highestDu = i
                        highestDuInt = i.get("diskusage")
    print(f"Highest CPU is {highestCpu.get("hostname")} : {highestCpu.get("cpuusage")}")
    print(f"Highest Disk Usage is {highestDu.get("hostname")} : {highestDu.get("diskusage")}")
def prodFilter(serverInventory) :
    prodServers , critialProdServers = [] , []
    for i in serverInventory :
        if(i.get("environment") == "PROD") : 
            prodServers.append(i)
            if(i.get("cpuusage") >= 80 ) :
                critialProdServers.append(i)
    if prodServers :
        print(f"Prod Servers :")
        for i in prodServers :
            print(f"{i.get("hostname")}")
    else :
        print(f"No Prod Servers found !")
    if critialProdServers :
        print(f"Critical Prod Servers :")
        for i in critialProdServers :
            print(f"{i.get("hostname")}")
    else :
        print(f"No Critical Prod Servers found !")
    return prodServers,critialProdServers
def aliveStatus(serverInventory) :
    up, down = 0,0
    for i in serverInventory:
        if i.get("status") == 'UP' :
            up += 1
        else :
            down += 1
    print(f"UP : {up}\nDOWN : {down}")
    return up, down       

for i in range(10) :
    serverCreator(i)
for i in serverInventory :
     print(i)
usageFilter(serverInventory)
prodFilter(serverInventory)
print(f"Server Status\n-------------")
aliveStatus(serverInventory)


    

