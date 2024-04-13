from itertools import combinations
import math
import sys

# 입력 변수 설정
input = sys.stdin.readline
n, m = map(int, input().split())
kilos = list(map(int, input().split()))

# m개 조합
combis = list(combinations(kilos,m))
## 소수 판별
def check_prime(num):
    nam = 0
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

prime_sums = set()  # 중복 제거를 위해 set 사용

for combination in combis:
    weight_sum = sum(combination)
    if check_prime(weight_sum):
        prime_sums.add(weight_sum)

# 소수 몸무게 합을 오름차순으로 출력하거나, -1 출력
if prime_sums:
    print(" ".join(map(str, sorted(prime_sums))))
else:
    print(-1)
