#BIRTHDAY CALCULATION
import datetime

bdate=input("Enter your birth day and month (DD-MM):").split("-")
bdt=datetime.date.today()
a=bdt.year

if(int(bdate[1])==bdt.month and bdt.day > int(bdate[0])):
    a+=1
elif(int(bdate[1])<bdt.month):
    a+=1

bd=datetime.date(a,int(bdate[1]),int(bdate[0]))
if(bd==bdt):
    print("🎉Happy Birthday🎉")
else:
    print("Your birthday is in",bd-bdt)
