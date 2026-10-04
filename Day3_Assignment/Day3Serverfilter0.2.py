#Day3Serverfilter.py
import random
from random import choice
serverInventory=[]
list=int(input("Enter how many servers you wish to create : "))
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
        print(f"\nServers found with high CPU Usage are : \n---------------------------------------")
        for i in highCpu :
            print(i)
    else :
        print("No servers with high CPU usage found")
    if(highDu != []) :
        print(f"\nServers found with high Disk Usage are : \n---------------------------------------")
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
    print(f"\n-------------------------------\n\nHighest CPU is {highestCpu.get("hostname")} : {highestCpu.get("cpuusage")}")
    print(f"Highest Disk Usage is {highestDu.get("hostname")} : {highestDu.get("diskusage")}")
def prodFilter(serverInventory) :
    prodServers , critialProdServers = [] , []
    for i in serverInventory :
        if(i.get("environment") == "PROD") : 
            prodServers.append(i)
            if(i.get("cpuusage") >= 80 ) :
                critialProdServers.append(i)
    if prodServers :
        print(f"\nProd Servers :\n---------------------")
        for i in prodServers :
            print(f"{i.get("hostname")}")
    else :
        print(f"\nNo Prod Servers found !")
    if critialProdServers :
        print(f"\nCritical Prod Servers :\n------------------------")
        for i in critialProdServers :
            print(f"{i.get("hostname")}")
    else :
        print(f"\nNo Critical Prod Servers found !")
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
def avgCpuDu(serverInventory):
    totalCpu,totalDu = 0.0,0.0
    for i in serverInventory:
         totalCpu += i.get("cpuusage")
         totalDu += i.get("diskusage")
    avgCpu = totalCpu/list
    avgDu = totalDu/list
    return avgCpu, avgDu
def serverHeatlthCheck(serverInventory):
    for i in serverInventory:
        if(i.get("status") == "DOWN") :
             print(f"{i.get("hostname")} : DOWN     - Immediate attention")
        elif(i.get("cpuusage") >= 90 or i.get("diskusage") >= 90):
            print(f"{i.get("hostname")} : CRITICAL - Needs attention")
        elif(i.get("cpuusage") >= 70 or i.get("diskusage") >= 80) :
            print(f"{i.get("hostname")} : WARNING  - Check and take action")
        else:
            print(f"{i.get("hostname")} : HEALTHY")

#for i in serverInventory :
#     print(i)
for i in range(list) :
    serverCreator(i)
print(f"=============================\nSERVER HEALTH REPORT\n=============================\n")
print(f"Total Servers : {list}\n")
print(f"Server Status\n-------------\n")
aliveStatus(serverInventory)
averageCpuDu=avgCpuDu(serverInventory)
print(f"\nAverage CPU usage is {int(averageCpuDu[0])}%\nAverage Disk usage is {int(averageCpuDu[1])}%")
usageFilter(serverInventory)
prodFilter(serverInventory)
print("\nServer Health Check\n---------------------")
serverHeatlthCheck(serverInventory)