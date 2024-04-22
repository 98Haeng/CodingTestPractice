# 부품 개수
n = int(input())
# 부품 목록
ar1 = list(map(int, input().split()))
# 찾고자 하는 개수
m = int(input())
# 부품 목록
ar2 = list(map(int, input().split()))

ar1.sort()

def binary_search(array, find, start, end):
    while start <= end:
        mid = (start + end)//2
        # 찾는수가 가운데보다 더 큰 경우
        if array[mid] == find:
            return mid
        elif array[mid] > find:
            end = mid - 1
        else:
            start = mid + 1
    return None
for i in ar2:
    result = binary_search(ar1, i, 0, n-1)
    if result != None:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')