#IF ,ELIF, ELSE
''' a=int(input("Enter a number"))
if(a==0):
    print("Sunday")
elif a==1:
    print("Monday")
elif a==2:
    print("Tuesday")
elif a==3:
    print("Wednesday")'''
    
#one line if
'''if(10>5):print("it is bigger")
#one line is and else
a=6
print("10 is smaller") if(a<100) else print("a is greater")
#multipkle else statements on the same line
b=36
print("A") if a>b else print("=") if a==b else print("B")
p1=int(input("Enter a number"))
p2=int(input("Enter a number"))
p3=int(input("Enter a number"))
p4=int(input("Enter a number"))

if((p1>p2) and (p1>p3) and (p1>p4)):
        print("Person 1 is greater")
elif((p2>p1) and (p2>p3) and (p2>p4)):
    print("person 2 is greater")
elif((p3>p1) and (p3>p2) and (p3>p4)):
    print("Person 3 is greater than all other")
else:
    print("Person 4 is greater")
'''
# to check number is three digit
#a=int(input("enrter a"))
'''b=str(a)
print(len(b))
if(len(b)==3):
    print("three digit")

#or
if((a>=100)and(a<=1000)):
    print("3 digit")
if((a%5==0)):
    print("dividible by 5)")
else:
    print("No divisible by 5")'''
#last digit / by 3 or not
'''n=a%10
print(n)
if(n%3==0):
    print("divisible by 3")
else:
    print("no")


wdays=int(input("Enter working days"))
absdays=int(input("Enter absent days"))
presentday=wdays-absdays
n=(presentday/wdays)*100
print(n,"%")
if(n>=75):
    print("He is eligible")
else:
    print("not eligible")'''
elec=int(input("enter"))
if(elec<=100):
    print("no vharges")
elif elec>100 and elec<200:
    print(5*elec)
elif elec>200:
    print(10*elec)
    
