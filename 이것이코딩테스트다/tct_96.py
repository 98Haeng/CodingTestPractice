n, m = map(int, input().split())
mins = []
for _ in range(n):
    nums = map(int, input().split())
    mins.append(min(nums))
print(max(mins))