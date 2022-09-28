# Write a python script to calculate factorial of a given number
n=int(input("Enter a number :"))
sum=1
while n>=1:
    sum=sum*n
    n-=1
print(sum)    