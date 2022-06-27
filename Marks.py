s1=int(input("Enter mathematics marks"));
s2=int(input("Enter statistics marks"));
s3=int(input("Enter computer marks"));
avg=(s1+s2+s3)/3;
if avg>=90:
    print("Grade: A");
elif 80<=avg<90:
    print("Grade: B");
elif 70<=avg<80:
    print("Grade: C");
elif 60<=avg<70:
    print("Grade: D");
else:
    print("Grade: F");