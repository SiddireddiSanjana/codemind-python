n=int(input())
lst=list(map(int,input().split()))
avg=sum(lst)/n
print("{:.2f}".format(avg))