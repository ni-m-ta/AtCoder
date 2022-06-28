A=int(input())
B=int(input())
C=int(input())
X=int(input())
count=0
x=X
for a in range(A+1):
    for b in range(B+1):
        for c in range(C+1):
            x-=500*a+100*b+50*c
            if x==0:
                count+=1
            x=X

print(count)