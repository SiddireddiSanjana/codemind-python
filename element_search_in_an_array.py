n=int(input())
lst=list(map(int,input().split()))
k=int(input())
for i in lst:
    if i == k:
        print("True")
        break
else:
    print("False")