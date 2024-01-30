#1
def chetam(N):
    val = 1
    while val!=N:
        yield val**2
        val+=1
#2
def chetam1():
    val = 0
    n = int(input())
    while val!=n:
        if val%2==0:
            yield val
        val+=1
#3
def chetam2(n):
    val = 0
    while val!=n:
        if val%3==0 or val%4==0:
            yield val
        val+=1
#4
def squares(a,b):
    while a!=b:
        yield a**2
        a+=1
prikols = squares(5,10)
for prikol in prikols:
    print(prikol)
#5
def chetam3(N):
    while N!=0:
        yield N
        N-=1