timers = [300, 60, 10]

time = int(input())
counts = []
def count_time(time):
    if time % 10 != 0:
        return -1
    global counts
    for t in timers:
        count = time // t
        counts.append(count)
        time -= t * count
    return counts

result = count_time(time)
if result != -1:
    for count in counts:
        print(count, end=' ')
else:
    print(result)
# print(result)