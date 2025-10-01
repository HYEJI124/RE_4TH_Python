# 차원 추가와 제거
# newaxis와 expand_dims
# 새로운 차원을 추가하여 브로드캐스팅이나 연산을 가능하게 함

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print('원본: \n', arr)
print('모양', arr.shape)
print()

# newaxis
row_vec = arr[np.newaxis, :]
print('행 벡터 \n', row_vec)
print('행 벡터 shape', row_vec.shape)
print()

col_vec = arr[:, np.newaxis]
print('열 벡터 \n', col_vec)
print('열 벡터 shape', col_vec.shape)
print()

arr = np.array([1, 2, 3, 4, 5])
# 첫 번째 축에 추가
arr_expanded0 = np.expand_dims(arr, axis=0)
print('axis=0 \n', arr_expanded0 )
print()

# 두 번째 축에 추가
arr_expanded1 = np.expand_dims(arr, axis=1)
print('axis=1 \n', arr_expanded1 )
print()

# squeeze
arr = np.array([[[1, 2, 3]]])
print('원본 \n', arr)
print('모양 \n', arr.shape)
print()

squeezed = np.squeeze(arr)
print('squeezed \n', squeezed)
print('squeezed 모양 \n', squeezed.shape)
print()

squeezed0 = np.squeeze(arr, axis=0)
print('squeezed0 \n', squeezed0)
print('squeezed0 모양 \n', squeezed0.shape)
print()

# 예외 발생
# squeezed3 = np.squeeze(arr, axis=3)
# print('squeezed3 \n', squeezed3)
# print('squeezed3 모양 \n', squeezed3.shape)
# print()

# 배열 평탄화 Flattening

# flatten: 항상 복사본 반환 (안전하지만 메모리 사용)
# ravel: 가능하면 뷰 반환 (빠르지만 주의 필요)

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print('2차원 배열')
print(arr)
print()

flattened = arr.flatten()
print('flattened 결과: ', flattened)
flattened[0] = 999
print()

print('2차원 배열')
print(arr)
print('flattened 결과: ', flattened)
print()

raveled = arr.ravel()
print('raveled 결과: ', raveled)
raveled[0] = 999
print()

print('2차원 배열')
print(arr)
print('raveled 결과: ', raveled)
print()

raveled_copy = arr.ravel().copy()
raveled_copy[1] = 999

print('2차원 배열')
print(arr)
print('raveled_copy 결과: ', raveled_copy)
print()


arr = np.array([1, 2, 3, 2, 1, 2, 3, 3, 1, 2, 1, 2, 5, 12])
uniq = np.unique(arr)
print(uniq)

uniq, idx, inv, cnt  = np.unique(arr,
                return_index=True,
                return_inverse=True,
                return_counts=True)

print('고유값', uniq)
print('첫 등장 인덱스', idx)
print('원본 -> 고유값 인덱스', inv)
print('등장 횟수', cnt)

print()

# 배열 결합 (Concatenation)

# 배열 이어 붙이기
# 같은 차원의 배열들을 특정 축을 따라 연결

# 1차원 배열 결합
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([7, 8, 9])

concat_1d = np.concatenate([a,b,c])
print('결합 결과:', concat_1d)

# 2차원 배열 결합
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print('A', A.shape)
print('B', B.shape)
print()

# ============== axis = 0 =================
# shape에서 열 개수 같으면 됨 A (2, 3), B (1, 3)

concat_v = np.concatenate([A, B], axis=0)
print('axis = 0 (수직결합):')
print(concat_v)
print(concat_v.shape)
print()

# ============== axis = 1 =================
# shape에서 행 개수 같으면 됨 A (2, 3), B (2, 1)
concat_h = np.concatenate([A, B], axis=1)
print('axis = 1 (수평결합):')
print(concat_h)
print(concat_h.shape)
print()

# vstack, hstack
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

vstacked = np.vstack([a, b])
print('v stack(수직)')
print(vstacked)
print()

hstacked = np.hstack([a, b])
print('h stack(수평)')
print(hstacked)
print()

# 배열 분할
# split

# 하나의 배열을 여러 개의 작은 배열로 나누는 작업
# 데이터를 배치로 나누거나 훈련/검증 세트로 분리할 때 사용

arr = np.arange(12)
print(arr)
print()

splits_equal = np.split(arr, 3) # 3개로 균등 분할
print('splits_equal', splits_equal)

for idx, sub in enumerate(splits_equal): # eumerate: 인덱스와 값이 같이 나옴
    print(idx+1, sub)
print()

splits_idx = np.split(arr, [3, 7]) # 인덱스 3, 7에서 분할
for idx, sub in enumerate(splits_idx): # eumerate: 인덱스와 값이 같이 나옴
    print(idx+1, sub)
print()

arr = np.arange(24).reshape(4, 6)
print(arr)
'''
[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]]
'''

row_splits = np.split(arr, 2, axis=0)
for i, sub in enumerate(row_splits):
    print(i+1, sub)
print()
'''
[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]]

[[12 13 14 15 16 17]
 [18 19 20 21 22 23]]
'''
# ==============================================

col_splits = np.split(arr, 2, axis=1)
for i, sub in enumerate(col_splits):
    print(i+1, sub)
print()
'''
[[ 0  1  2]          [[3  4  5]
 [ 6  7  8]          [9 10 11]
 [12 13 14]          [15 16 17]
 [18 19 20]]          [21 22 23]]
'''

arr = np.array([3, 1, 2, 3, 4, 5, 2])
sorted_copy = np.sort(arr)
print(sorted_copy)
print(arr)
print()

arr.sort()
print(arr)
print()

arr2 = np.array([
    [2, 1, 5],
    [3, 2, 1]
])

# axis = 0 (행 방향)
sorted_axis0 = np.sort(arr2, axis=0)
print(sorted_axis0)
print()

# axis = 1 (열 방향)
sorted_axis1 = np.sort(arr2, axis=1)
print(sorted_axis1)
print()

# axis = None (평탄화 후 정렬)
sorted_None = np.sort(arr2, axis=None)
print(sorted_None)
print()

# argsort
names = np.array(['김철수', '이영희', '박민수', '정수진', '최동욱'])
scores = np.array([85, 92, 78, 95, 88])

for name, score in zip(names, scores):
    print(f'{name} {score}')
print()

# 점수 순으로 정렬
sorted_idx = np.argsort(scores)[::-1] # 점수 높은 순서

for i, idx in enumerate(sorted_idx, 1):
    print(f'{i}위 {names[idx]} {scores [idx]}')
print()


