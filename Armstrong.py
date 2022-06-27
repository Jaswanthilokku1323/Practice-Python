a=int(input("Enter number"))
sum=0
temp=a
while a>0:
    rem=a%10
    sum=sum+rem*rem*rem
    a=a//10
if temp==sum:
    print("Armstrong number")
else:
    print("Not Armstrong number")