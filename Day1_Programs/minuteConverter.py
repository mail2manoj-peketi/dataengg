#minuteConverter.py  - Minutes to hours and minutes
minutes = int(input("Enter minutes here : "))
converted = print(f"{int( minutes / 60)} hours and {-1 * ( (int(minutes / 60) * 60) - minutes) } minutes")