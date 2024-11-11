# 돌 개수
n =int(input())

# 몫과 나머지로 승자 결정
if (n//3 + n%3)%2 == 1:
    print('SK')
else:
    print('CY')