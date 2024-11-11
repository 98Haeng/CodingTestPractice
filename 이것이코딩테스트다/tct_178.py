n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

# 정렬 수행
array.sort()
for num in array:
    print(num, end=' ')