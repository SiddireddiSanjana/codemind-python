def prime(x):
    if x==1:
        return False
    for i in range(2,int((x**0.5)+1)):
        if x%i==0:
            return False
    else:
        return True
y=int(input())
z=int(input())
p=0
for i in range(y,z+1):
    if prime(i) == True:
        p+=1
print(p)