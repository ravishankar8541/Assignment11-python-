# Write a python script to calculate sum of first N even natural numbers
n=int(input("Enter a number :"))
sum=0
i=1
while i<=n:
    if i%2==0:
        sum=sum+i
    i+=1    
print(sum)