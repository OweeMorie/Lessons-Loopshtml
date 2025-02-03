'''
#loop : repitition
#1)for loop
#display hello 10 times
for i in range(1,11):
    print (i, "Hello")

#2)while loop
x=1
while x<=10:
    print(x,"Hello")
    x=x+1

#3)table of n
n=int(input("Enter n : "))
for i in range(1,11):
    print(n,'x',i,'=',n*i)

 #4) display factors of n
 #n=18 : 1,2,3,6,9,18 : 1 to 18: 1 to n
n=int(input("Enter n : "))
for i in range(1,n+1):
    if n%i==0:
        print(i,"is factor of ", n)

 #5)Check whether the number is prime or not
n=int(input("Enter n : "))
#3 : 1and 3
c=0
for i in range(1,n+1):
    if n%i==0:
        c=c+1
if c==2:
    print(n,"is prime number")
else:
    print(n,"is composite number")

#6)summation of n natural number
n=int(input("Enter n : "))
sum=0
for i in range(1,n+1):
    sum = sum+i
print(sum)
'''
#fa
n=int(input("Enter n : "))
f=1
for i in range(1,n+1):
    f = sum*i
print(sum)