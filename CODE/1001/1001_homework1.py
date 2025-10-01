# 실습1. 배열 형태 변형, 차원 확장·축소(1)
import numpy as np

# 1. 아래의 배열을 사용해서
# 1) ravel과 flatten을 각각 사용해 1차원 배열로 변환하고,
# 2) arr의 첫 번째 원소(arr[0,0])를 999로 바꾼 뒤 ravel 결과와 flatten 결과에 어떤 변화가 있는지 확인하세요.
arr = np.array([[10, 20], [30, 40], [50, 60]])

raveled = arr.ravel()
print('raveled 결과: ', raveled)
flattened = arr.flatten()
print('flattened 결과: ', flattened)
print()

arr[0,0] = 999
print('raveled 결과: ', raveled)
print('flattened 결과: ', flattened)
print()

# 2. 크기가 32x32인 이미지 데이터를 가정하고, 이 배열에 대해 expand_dims를 사용하여
# shape (1, 32, 32)로 바꾸는 코드를 작성하세요.
img = np.random.rand(32, 32)
img_expanded = np.expand_dims(img, axis=0)
print('shape (1, 32, 32)로 바꾼 결과: \n', img_expanded)
print('모양: \n', img_expanded.shape)
print()

# 3. 아래 배열에서 불필요한 1차원을 모두 제거하여 shape이 (28, 28)이 되도록 만드세요.
img = np.random.randint(0, 255, (1, 28, 28, 1))
img_squeeze = np.squeeze(img)
print('shape (28, 28)로 바꾼 결과: \n', img_squeeze)
print('모양: \n', img_squeeze.shape)
print()

# 4. 아래 2차원 배열을 1) 1차원 배열로 만든 후 2) 중복값을 제거한 뒤 shape (1, n)으로 재구성하세요.
arr = np.array([[3, 1, 2, 2], [1, 2, 3, 1], [2, 2, 1, 4]])
flat = arr.ravel()
uniq = np.unique(flat)
reshape = uniq.reshape(1, -1)
print('중복값 제거 후 shape(1, n): \n', reshape)
print('모양: \n', reshape.shape)
print()

# 5. 다음 배열을 shape (10,)로 만든 뒤 고유값 배열을 구하세요.
arr = np.array([[[1], [3], [2], [1], [3], [2], [3], [1], [2], [3]]]) # shape (1, 10, 1)
flat = arr.reshape(-1)
uniq = np.unique(flat)
print('shape (10,): \n', flat)
print('모양: \n', flat.shape)
print('고유값 배열: \n', uniq)
print()

# 6. 다음 배열을 1차원 배열로 만든 후 고유값만 추출해서 shape (고유값 개수, 1)인 2차원 배열로 변환하세요.
arr = np.array([ [[0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5]], [[3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]] ]) # shape (2, 3, 4)
flat = arr.ravel()
uniq = np.unique(flat)
reshaped = uniq.reshape(-1, 1) 
print('1차원 배열: \n', flat)
print('고유값 배열: \n', uniq)
print('shape (10,): \n', reshaped)
print()
