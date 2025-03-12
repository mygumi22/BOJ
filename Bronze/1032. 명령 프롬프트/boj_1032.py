# 문제링크 https://www.acmicpc.net/problem/1032

import sys

n = int(sys.stdin.readline())
A = []

for _ in range(n):
  str = sys.stdin.readline().rstrip()
  A.append(str)

if n == 1:
  print(A[0])
else:
  result = ''
  for i in range(len(A)):
    if i == 0:
      result = A[i]
    else:
      list_result = list(result) # 기존텍스트
      list_a = list(A[i]) # i번째 입력한 텍스트

      for j in range(len(list_result)): # 텍스트 길이는 같기 때문에 j를 동시에 올리면서 비교
        if list_result[j] != list_a[j]:
          result = ''.join(list_result[:j]) + '?' + ''.join(list_result[j+1:])
          list_result = list(result)

  print(result)


        

