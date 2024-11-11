# 데이터 입력
formula = str(input())

# 1. -를 기준으로 분할
m = formula.split('-')

answer = 0
x = sum(map(int, m[0].split('+')))
# 처음 숫자가 -인지 + 인지에 따라 시작점이 달라짐
if formula[0] == '-':
    answer -= x
else:
    answer += x

# 2. 분할한 것들을 합쳐서 - 적용
for x in m[1:]: # 첫번째 작업은 이미 했기때문에 인덱스 1부터 시작
    x = sum(map(int, (x.split('+'))))
    answer -= x
print(answer)