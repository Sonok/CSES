import sys
lst = sys.stdin.readline()
count = longest = 1
for i in range(1, len(lst)):
    if lst[i] == lst[i-1]:
        count += 1
    else:
        count = 1
    longest = max(longest,count)
print(longest)