n=int(input("Terms"));
n1=0;
n2=1;
count=0;
if n<=0:
    print("Enter positive integer");
elif n==1:
    print("Fibonacci series:",n,":");
    print(n1);
else:
    print("Fibonacci sequence");
while count<n:
    print(n1);
    nth=n1+n2;
    n1=n2;
    n2=nth;
    count+=1;

