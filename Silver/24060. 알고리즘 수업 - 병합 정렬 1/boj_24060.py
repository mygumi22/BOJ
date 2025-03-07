# 문제링크 https://www.acmicpc.net/problem/24060

# A = [4, 5, 1, 3, 2]
# K = 7
# N = 5

# A = [4, 5, 1, 3, 2]
# K = 13
# N = 5

N, K = map(int, input().split())
A = list(map(int, input().split()))
T = []

def merge_sort(A, low, high):
  if high > low:
    mid = (low + high) // 2
    merge_sort(A, low, mid)
    merge_sort(A, mid+1, high)
    merge(A, low, mid, high)

def merge(A, low, mid, high):
  i = low
  j = mid + 1
  S = []

  while (i <= mid and j <= high):
    if A[i] <= A[j]:
      S.append(A[i])
      i += 1
    else:
      S.append(A[j])
      j += 1
  while (i <= mid):
    S.append(A[i])
    i += 1
  while (j <= high):
    S.append(A[j])
    j += 1

  i = low
  t = 0
  while (i <= high):
    A[i] = S[t]
    T.append(A[i])

    i += 1
    t += 1

merge_sort(A, 0, len(A) - 1)
if K > len(T):
  print(-1)
else:
  print(T[K-1])