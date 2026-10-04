#diskUsage.py
diskUsage, totalDiskSpace = int(input("Enter disk usage : ")) , int(input("Enter total disk space : "))
print(f"Current disk usage : {(diskUsage*100) / totalDiskSpace} % ")