def sum_of_divisor(n):
    sum=0
    if(n<2):
        return sum
    for i in range(1,n+1):
        if n%i==0:
            sum=sum+i
    return sum
print(sum_of_divisor(10))