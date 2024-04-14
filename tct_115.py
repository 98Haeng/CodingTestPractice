cols = ['a','b','c','d','e','f','g','h']
rows = [1,2,3,4,5,6,7,8]
# 입력 좌표
point = input()
# 열 : 유니코드 정수 -> 정수로 반환
point_col = int(ord(point[0]) - int(ord('a'))) + 1
point_row = int(point[1])
# 몇번 움직일 수 있는지 확인
count = 0
# 움직일 수 있는 방안 : 총 8가지
movelist = [(2, -1), (2,1), (-2,1), (-2,-1), (1,2), (1,-2), (-1, 2), (-1,-2)]
for move in movelist:
    row = move[0]
    col = move[1]
    move_row = point_row + row
    move_col = point_col + col

    if move_row >= 1 and move_row <= 8 and move_col >= 1 and move_col <= 8:
        count += 1

print(count)