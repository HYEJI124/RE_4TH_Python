# 배열 모양 변경, 조작
import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5, 6])

print('======= 1차원 =======')
print('shape', arr_1d.shape) # 모양 (6,)
print('ndim', arr_1d.ndim) # 차원
print('size', arr_1d.size) # 사이즈
print(arr_1d.reshape(3, -1)) # - : 자동으로 채워줌
# print(arr_1d.reshape(4, -1)) # 불가능 6개를 4로 나눌 수 없음

print()

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

print('======= 2차원 =======')
print('shape', arr_2d.shape) # 모양 (2, 3)
print('ndim', arr_2d.ndim) # 차원
print('size', arr_2d.size) # 사이즈
print()

# 기본 산술 연산
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 4, 3, 2, 1])

print('배열 a:', a)
print('배열 b:', b)

print()
print('덧셈 (a + b): \n', a + b)
print('뺄셈 (a - b): \n', a - b)
print('곱셈 (a * b): \n', a * b)
print('거듭제곱 (a ** b): \n', a ** b)
print('나눗셈 (a / b): \n', a / b)
print('몫 (a // b): \n', a // b)
print('나머지 (a % b): \n', a % b)


# 스칼라와의 연산
a = np.array([1, 2, 3, 4, 5])
scalar = 10

print()
print('+ 스칼라', a + scalar)
print('- 스칼라', a - scalar)
print('* 스칼라', a * scalar)
print('/ 스칼라', a / scalar)
print('스칼라 / 배열', scalar / a)

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
B = np.array([
    [7, 8, 9],
    [10, 11, 12]
])

print()
print('행렬 A \n', A)
print('행렬 B \n', B)

print()
print('행렬 A + B \n', A + B)
print()
print('행렬 A * B\n', A * B)
print()
print('행렬 A / B\n', A / B)
print()


A = np.array([
    [1, 2],
    [3, 4]
])
B = np.array([
    [7, 8],
    [9, 10]
])

print('행렬 곱셈 (A @ B) \n', A @ B) # 1 X 7 + 2 X 9 = 25 / 1 X 8 + 2 X 10 = 28 / 3 X 7 + 4 X 9 = 57 / 3 X 8 + 4 X 10 = 64
print()
# 브로드 캐스팅(Broadcasting)
# 서로 다른 모양의 배열 간 연산을 가능하게 하는 Numpy 기능
arr = np.array([1, 2, 3, 4, 5])
scalar = 10

# 스칼라가 자동으로 배열 크기로 '브로드캐스트'됨
# [1, 2, 3, 4, 5] + [10, 10, 10, 10, 10]

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
vector = np.array([10, 20, 30])

print(matrix + vector)
print()
'''
[                                           [
    [1, 2, 3],                                   [10, 20, 30],
    [4, 5, 6],              +                    [10, 20, 30],
    [7, 8, 9],                                   [10, 20, 30]
]                                           ]
'''

# 브로드캐스팅 규칙
# 규칙 1: 차원 수가 다르면 작은 쪽의 앞에 1을 추가!
# (3, 3) 2차원 + (3, ) 1차원 {-> (1, 3) 2차원} # (2, 3, 4) 3차원
a = np.array([1, 2, 3]) # (3, ) 1차원
b = np.array([[4], [5], [6]]) # (3, 1) 2차원

print(a.shape)
print(b.shape)
print()

a + b # (3, ) + (3, 1) -> (1, 3) + (3, 1) -> (3, 3)
print(a + b)

# 규칙 2: 각 차원에서 크기가 1이거나 같아야 함
# 호환 가능: (3, 1) & (1, 4) = (3, 4)
# 호환 불가능: (3, 2) & (4, 2) => 에러 ... (3이나 4 둘 중 하나가 1이 들어가거나 3이나 4 둘 중 하나로 값이 같아야 함)

print()
a = np.ones((1, 3))
b = np.ones((2, 1))
print(a + b)

# 1차원
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# np.sum(arr) # 합
# np.mean(arr) # 평균
# np.median() # 중앙값
# np.std() # 표준편차
# np.max() # 최댓값
# np.min() # 최솟값
# np.var() # 분산
# np.ptp() # max - min
print()
print('누적 합', np.cumsum(arr))
print('누적 곱', np.cumprod(arr))
print()

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print('행별 합 (axis=1)', np.sum(matrix, axis=1))
print('열별 합 (axis=0)', np.sum(matrix, axis=0))
print()

print('행별 평균 (axis=1)', np.mean(matrix, axis=1))
print('열별 평균 (axis=0)', np.mean(matrix, axis=0))
print()

print('행별 누적 합 (axis=1)\n', np.cumsum(matrix, axis=1))
print('열별 누적 합 (axis=0)\n', np.cumsum(matrix, axis=0))
print()




