import sys
imput = sys.stdin.readline
h,w = map(int,input().split())
s = [input() for _ in range(h)]
t = [input() for _ in range(h)]
arrngd_s = []
arrngd_t = []

for j in range(w):
    col1 = ''
    col2 = ''
    for i in range(h):
        col1 += s[i][j]
        col2 += t[i][j]
    arrngd_s.append(col1)
    arrngd_t.append(col2)

arrngd_s.sort()
arrngd_t.sort()

if arrngd_s == arrngd_t:
    print('Yes')
else:
    print('No')


