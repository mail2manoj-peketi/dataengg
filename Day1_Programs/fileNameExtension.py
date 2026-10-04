#fileNameExtension.py
filePath, n = input("Enter file path : "), -1
while(filePath[n] != '/' ):
    #print(f"{filePath[n]}", end="")
    n = n-1
n=n+1
print(filePath[n:])