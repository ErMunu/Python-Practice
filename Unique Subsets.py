from collections import Counter
n = int(input())
arr = list(map(int, input().split()))
k = int(input())
count = Counter(arr)
found = any(freq >= k for freq in count.values())
print(found)
