
#KBC
def quest_check(a1,ans1,amnt1):
    print(a1)
    ans=input("Ans:")
    if(ans == ans1):
        print("You won ₹",amnt1,"👌\n")
        return amnt1
    else:
        print("❌ Wrong answer \n")
        return 0

print("WELCOME TO KBC!!!!!")
print("So, Here is your first question on your computer screen ----->\n\n")

a="""Q1. Which person established the today well known institute in INDIA  named as IISC BANGLORE?
A.Sir Dorabji Tata\nB.Sir Jamsetji Tata\nC.Sir Ratan Tata\nD.Dada Bhai Naoroji"""
b="Q2. Swami Vivekanand dies in ?\nA.1885\nB.1904\nC.1898\nD.1902"
c="""Q3. Who is the person with longest-serving  chairman of Tata group ?\nA. Jamset Ji Tata\nB.Ratan Tata\nC.Dorab ji Tata\nD.J.R.D Tata"""
d="""Q4.For how many years J.R.D Tata hold position of chairman in Tata groups ?\nA.24years\nB.53years\nC.37years\nD.45years"""
e="""Q5. Tata group was established in ?\nA.1859\nB.1868\nC.1876\nD.1884"""

arr = [a,b,c,d,e]
ans=['A','D','D','B','B']
amount = [100000,300000,600000,2000000,7000000]
amnt=0

for i in range(5):
    r= quest_check(arr[i],ans[i],amount[i])
    amnt+=r
    if (r != amount[i]):
        print("You won ₹",amnt)
        break
if(amnt==10000000):
    print("🎉🎉🎉 You are a CR0REPATI")

    