import time

a = int((time.strftime('%H')))

if (a < 12):
    print("Good Morning")
elif (a < 18):
    print("Good Afternoon")
else:
    print("Good Evening")