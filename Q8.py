# Write a python script to calculate sum of digits of a given number
n=1563
i=1
sum=0
while n!=0:
    a=n%10
    sum=sum+a
    n=n//10
print(sum)   