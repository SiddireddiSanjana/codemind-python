k=int(input())
a=k
d=0
def position(n):
  c=str(n)
  return len(c)
while k!=0:
  d=d+(k%10)**position(k)
  k=k//10
if d==a:
  print(True)
else:
  print(False)