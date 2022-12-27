from collections import deque
n = int(input())
a = list(map(int,input().split()))
a.sort()
dq_a = deque(a)

num_books = n
book = 1
flag = True
while flag and dq_a:
    if dq_a[0] == book:
        book += 1
        dq_a.popleft()
    else:
        for _ in range(2):
            if dq_a:
                dq_a.popleft()
            else:
                flag = False
        if flag:
            dq_a.appendleft(book)

print(book-1)






