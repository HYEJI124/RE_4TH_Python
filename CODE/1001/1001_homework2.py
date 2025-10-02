# 실습2. 배열의 결합과 분리(1)
import numpy as np

# 1. 다음 두 배열을 행 방향으로 이어붙이세요.
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
result = np.concatenate((a, b), axis=0)
print('문제 1: \n', result)
print()

'''
    리더님 방법
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6]])

    result = np.vstack((a, b))
    print('result', result)
'''

# 2. 아래 배열을 3개로 같은 크기로 분할하세요.
a = np.arange(12)
split_a = np.split(a, 3)
print('문제 2: \n', split_a)
print()

'''
    리더님 방법
    a = np.arange(12)
    result = np.split(a, 3)
    print('result', result)
'''

# 3. 다음 배열들을 새로운 축에 쌓아 shape이 (3, 2)인 배열을 만드세요.
a = np.array([1, 2])
b = np.array([3, 4])
c = np.array([5, 6])

result = np.stack((a, b, c), axis=0)
print('문제 3: \n', result)
print('문제 3(모양): \n', result.shape)
print()

'''
    리더님 방법
    a = np.array([1, 2])
    b = np.array([3, 4])
    c = np.array([5, 6])

    result = np.stack((a, b, c), axis=0)
    print('result \n', result)
'''

# 4. shape가 (2, 3)인 아래 두 배열을 shape (2, 2, 3)인 3차원 배열을 만드세요.
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])

result = np.stack((a, b), axis = 1)
print('문제 4: \n', result)
print()

'''
    리더님 방법
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.array([[7, 8, 9], [10, 11, 12]])

    result = np.stack((a, b), axis=0)
    print('result \n', result)
'''
# 5. 아래의 1차원 배열을 2:3:3 비율(총 3개)로 분할하세요.
arr = np.arange(8)
result = np.split(arr, [2, 5])
print('문제 5: \n', result)
print()

'''
    리더님 방법
    arr = np.arange(8)
    result = np.split(arr, [2, 5])
    print('result \n', result)
'''

# 6. 아래 두 배열을 axis=0, axis=1로 각각 stack하여 두 경우의 결과 shape을 모두 구하세요
a = np.ones((2, 3))
b = np.zeros((2, 3))

axis0 = np.stack((a, b), axis=0)
print('문제 6 (axis=0): \n', axis0)
print('문제 6 (axis=0) 모양: \n', axis0.shape)
axis1 = np.stack((a, b), axis=1)
print('문제 6 (axis=1): \n', axis1)
print('문제 6 (axis=1) 모양: \n', axis1.shape)
print()

'''
    리더님 방법
    a = np.ones((2, 3))
    b = np.zeros((2, 3))

    # 위아래로 쌓음
    result0 = np.stack((a, b), axis=0)
    print('result0 \n', result0) # (2, 2, 3)

    # 옆으로 쌓음
    result1 = np.stack((a, b), axis=1)
    print('result1 \n', result1) # (2, 2, 3)


'''