'''num=int(input("Enter number"));
for i in range(2,num):
    if num%i==0:
        print(num," is not a prime number");
        break
    else:
        print(num,"is a prime number");
        break'''
n=int(input("Enter number"))
count=0
for i in range(1, n+1):
    if n%i==0:
        count=count+1
if count==2:
    print("prime number")
else:
    print("Not a prime number")


