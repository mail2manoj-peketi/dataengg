#day1_Challenge.py - Server Health Check calculator
server, cu, mu, du = input("Enter Server Name : "), int(input("Enter CPU Usage : ")), int(input("Enter Memory usage : ")), int(input("Enter Disk usage : "))
print(f"Server Name : {server}\nCPU Usage : {cu}%\nMemory usage : {mu}%\nDisk usage : {du}%\nAverage resource usage : {     int((cu + mu + du)/3)    }%")