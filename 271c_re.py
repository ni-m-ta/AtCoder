num_books = int(input())
a = list(map(int,input().split()))
a.sort()
not_overlapping_a = list(set(a))
num_overlaps = num_books - len(not_overlapping_a)

book = 1
i = 0
flag = True
if num_books == 1 and not_overlapping_a != 1:
    flag = False 

while flag:
    if i < len(not_overlapping_a) and not_overlapping_a[i] == book:
        book += 1
        i += 1
    else:
        count = 0
        for _ in range(2):
            if num_overlaps > 0:
                count += 1
                num_overlaps -= 1
            elif not_overlapping_a.pop() > book:
                count += 1
            else:
                flag = False
        if count == 2:
            not_overlapping_a.insert(i,book)
                
print(book-1)






