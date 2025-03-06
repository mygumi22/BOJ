# 문제링크 https://www.acmicpc.net/problem/1924

m, d = map(int, input().split())

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days = {0: 'SUN', 1: 'MON', 2: 'TUE', 3: 'WED', 4: 'THU', 5: 'FRI', 6: 'SAT'}

daynum = d

for i in range(1, m):
  daynum += month_days[i - 1]

result_num = daynum % 7
print(days[result_num])
