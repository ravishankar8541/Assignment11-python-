# Write a python script to calculate sum of first N odd natural numbers
n=int(input("Enter a number :"))
sum=0
i=1
while i<=n:
    if i%2:
        sum=sum+i
    i+=1    
print(sum)        
