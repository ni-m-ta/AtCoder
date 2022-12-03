import sys
input = sys.stdin.readline
flag = 'Yes'
suits = ['H','D','C','S']
nums = [str(i) for i in range(2,10)]+['A','T','J','Q','K']
cards = []

n = int(input())
for _ in range(n):
    string = input()
    if string[0] not in suits:
        flag = 'No'
        break
    if string[1] not in nums:
        flag = 'No'
        break
    if string in cards:
        flag = 'No'
        break
    cards.append(string)

print(flag)
