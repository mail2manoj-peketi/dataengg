#serverInventorySummary.py
import random
inventory, highDUHostNameValues = [], {}
upCount, downCount, prodCount, uatCount = 0, 0, 0, 0

serverSerial=int(input("Enter no of servers you wish to create :"))
for i in range(1,serverSerial + 1) :
    env , diskUsage , serverStatus = ("PROD","UAT"), random.randint(1,100) , ("UP","DOWN")
    if(i<10):
        inventory.append({"hostname" : f"app0{i}" , "environment" : random.choice(env), "serverstatus" : random.choice(serverStatus), "diskusage" : diskUsage })
    else:
        inventory.append({"hostname" : f"app{i}" , "environment" : random.choice(env), "serverstatus" : random.choice(serverStatus), "diskusage" : diskUsage })
    if(inventory[i-1].get("serverstatus") == "UP"):
        upCount += 1
    else:
        downCount += 1
    if(inventory[i-1].get("environment") == "PROD"):
        prodCount += 1
    else:
        uatCount += 1
    if(inventory[i-1].get("diskusage") >= 85 ):
      highDUHostNameValues.update({inventory[i-1].get("hostname") : inventory[i-1].get("diskusage")})
      #print(inventory[i-1].items())

print(f"\nServer Inventory Summary Report\n\n============================\n")
print(f"Total Servers : {serverSerial}\n")
print(f"Server Live Status \nUP : {upCount} \nDOWN : {downCount}\n")
print(f"Environmental Count \nPROD : {prodCount} \nUAT : {uatCount}\n")
print(f"High Disk Usage servers : ")
for x, y in highDUHostNameValues.items():
    print(f"{x} : {y}%")