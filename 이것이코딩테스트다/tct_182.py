n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a는 작은거부터, b는 큰거부터 정렬
a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]

print(sum(a))