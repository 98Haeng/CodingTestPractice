#### 현재 미해결 ####
# Try1 : 메모리초과 
import sys
from itertools import combinations
input = sys.stdin.readline
n, k = map(int, input().split())
tastes = list(map(int, input().split()))

results = []
combis = list(combinations(tastes, k))
# print(combis)

# 맛의 합을 구하는 함수
def get_taste(lst):
    taste_sum = 0
    global results
    # 첫번째 맛 : 그대로 반영
    for i in range(len(lst)):
        if i == 0:
            taste_sum += lst[i]
        else:
            if lst[i]  >= lst[i-1]:
                taste_sum += lst[i]-lst[i-1]
            else:
                taste_sum += 0
    results.append(taste_sum)
    return

for i in range(len(combis)):
    get_taste(combis[i])
print(max(results))

# Try2 : 시간 초과
from itertools import combinations
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
tastes = list(map(int, input().split()))
result = 0
for combi in combinations(tastes, k):
    # 첫번째는 그대로 반영
    taste_sum = combi[0]
    for i in range(1, len(combi)):
        if combi[i] >= combi[i-1]:
            taste_sum += combi[i]-combi[i-1]

    result = max(result, taste_sum)
print(result)
