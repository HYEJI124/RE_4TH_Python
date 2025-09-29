# 실습1. 배열 초기화 및 생성(1)
# 1. 0으로 채워진 크기 (3, 4) 배열을 생성한 후, 모든 값을 5로 채우는 새로운 배열을 만드세요.

import numpy as np
# 0으로 채워진 크기 (3, 4) 배열
print()
arr1 = np.zeros((3, 4))
print('2차원 zeros:', arr1)

# 모든 값을 5로 채우는 새로운 배열
print()
full_array = np.full_like(arr1, 5)
print('2차원 배열:', full_array)

'''
    리더님 방법
    arr1 = np.zeros((3, 4)) + 5
    print(arr1)
'''

# 2. 0부터 20까지 2씩 증가하는 1차원 배열을 생성하세요.
print()
arr1 = np.arange(0, 21, 2)
print('0부터 20까지 2씩 증가', arr1)

'''
    리더님 방법
    arr2 = np.arange(0, 21, 2)
    print(arr2)
'''

# 3. 0~1 사이의 실수 난수를 가지는 (2, 3) 크기의 배열을 생성하세요.
print()
random1 = np.random.rand(2, 3)
print('0부터 1 균일 분포(2, 3): \n', random1)

'''
    리더님 방법
    arr3 = np.random.rand(2, 3)
    print(arr3)
'''

# 4. 평균이 100, 표준편차가 20인 정규분포 난수 6개를 생성하세요.
print()
mean , std = 100, 20
normal = mean + std * np.random.randn(6)
print('평균 100, 표준편차 20인 정규분포\n', normal)

'''
    리더님 방법
    # normal(평균, 표준편차, 사이즈)
    arr4 = np.random.normal(100, 20, 6)
    print(arr4)
'''

# 5. 1부터 20까지의 정수를 포함하는 1차원 배열을 만들고, 이 배열을 (4, 5) 크기의 2차원 배열로 변환하세요.
print()
dim1 = np.arange(1, 21)
print(dim1)
print()
dim2 = dim1.reshape((4, 5))
print(dim2)

'''
    리더님 방법
    # reshape 재배치
        : 앞에 요소의 개수만큼 존재해야 함
    arr5 = np.arange(1, 21).reshape(4, 5) 
    print(arr5)
'''

# 6. 0부터 1까지 균등 간격으로 나눈 12개의 값을 가지는 배열을 생성하고, 이를 (3, 4) 크기로 변환하세요.
print()
random_uniform1 = np.linspace(0, 1, 12)
print(random_uniform1)

print()
random_uniform2 = random_uniform1.reshape((3, 4))
print(random_uniform2)

'''
    리더님 방법
    arr6 = np.linspace(0, 1, 12).reshape(3, 4)
    print(arr6)
'''
# 7. 0~99 사이의 난수로 이루어진 (10, 10) 배열을 생성한 뒤, np.eye()로 만든 단위 행렬을 더하여 대각선 요소가 1씩 증가된 배열을 만드세요.
arr7 = np.random.randint(0, 100, (10,10))
print(arr7)
arr7 = arr7 + np.eye(10) # 대각선에 1씩 더해짐
print(arr7)

'''
    리더님 방법
    arr7 = np.random.randint(0, 100, (10,10))
    arr7 = arr7 + np.eye(10) # 대각선에 1씩 더해짐
    print(arr7)
'''

# 8. 0~9 사이의 난수로 이루어진 (2, 3, 4) 3차원 배열을 생성하세요.
arr2 = np.random.randint(0, 10, (2, 3, 4))
print(arr2)

'''
    리더님 방법
    arr8 = np.random.randint(0, 10, (2, 3, 4))
    print(arr8)
'''