# Write a python script to calculate sum of first N natural numbers

print("Enter a number :")
n=int(input())
sum=0
for a in range(1,n+1,1):
    sum=sum+a
print(sum)    