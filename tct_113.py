# 시간 입력
n = int(input())

# 시, 분, 초 계산 -> 3이 하나라도 들어있는지 확인
# 분
count = 0
for hour in range(n+1):
    # 분
    for minute in range(60):
        # 초
        for second in range(60):
            sentence = f"{hour}시 {minute}분 {second}초"
            if '3' in sentence:
                count += 1

print(count)

