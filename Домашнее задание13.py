def rot(arr): return arr[-1:] + arr[:-1]
print(*rot(input().split()))