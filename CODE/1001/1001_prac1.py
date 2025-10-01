# 실습3. 논리 연산과 조건 연산(1)
import numpy as np
# 1. 1차원 배열 [5, 12, 18, 7, 30, 25]에서 10보다 크고 20보다 작은 값만 필터링하세요.
arr1 = np.array([5, 12, 18, 7, 30, 25])
print('문제 1: \n', arr1[(arr1 > 10) & (arr1 < 20)])
print()

'''
    리더님 방법
    arr1 = np.array([5, 12, 18, 7, 30, 25])
    result = arr1[(arr1 > 10) & (arr1 < 20)]
    print('1. : ', result)
'''

# 2. 배열 [10, 15, 20, 25, 30, 35]에서 15 이하이거나 30 이상인 값만 선택하세요.
arr2 = np.array([10, 15, 20, 25, 30, 35])
print('문제 2: \n', arr2[(arr2 <= 15) | (arr2 >= 30)])
print()

'''
    리더님 방법
    arr2 = np.array([10, 15, 20, 25, 30, 35])
    result = arr2[(arr2 <= 15) | (arr2 >= 30)]
    print('2. : ', result)
'''

# 3. 배열 [3, 8, 15, 6, 2, 20]에서 10 이상인 값을 모두 0으로 변경하세요.
arr3 = np.array([3, 8, 15, 6, 2, 20])
arr3[arr3 >= 10] = 0
print('문제 3: \n', arr3)
print()

'''
    리더님 방법
    arr3 = np.array([3, 8, 15, 6, 2, 20])
    arr3[arr3 >= 10] = 0
    print('3. : ', arr3)
'''

# 4. 배열 [7, 14, 21, 28, 35]에서 20 이상인 값은 "High", 나머지는 "Low"로 표시하는 새로운 배열을 생성하세요.
arr4 = np.array([7, 14, 21, 28, 35])
result = np.where(arr4 >= 20 , 'High', 'Low')
print('문제 4: \n', result)
print()

'''
    리더님 방법
    arr4 = np.array([7, 14, 21, 28, 35])
    result = np.where(arr4 >= 20, 'High', 'Low')
'''

'''
    삼항 연산자
        : 참일 때_값 if 조건 else 거짓일 때_값

    문제 1.
    num = 8
    result = '짝수' if num % 2 == 0 else '홀수'

    문제 2.
    a, b = 10, 20
    max_value = a if a > b else b
'''

# 5. 0~9 범위의 배열에서 짝수는 그대로 두고, 홀수는 홀수 값 × 10으로 변환한 배열을 만드세요
arr5 = np.arange(10)
arr5[arr5 % 2 != 0] *= 10
print('문제 5: \n', arr5)
print()

'''
    리더님 방법
    arr5 = np.arange(10)
    result = np.where(arr5 % 2 == 0, arr5, arr5 * 10)
    print(result)
'''

# 6. 아래 2차원 배열 에서 20 이상 40 이하인 값만 선택하세요.
arr6 = np.array([[10, 25, 30], [40, 5, 15], [20, 35, 50]])
print('문제 6: \n', arr6[(arr6 >= 20) & (arr6 <= 40)])
print()

'''
    리더님 방법
    arr6 = np.array([
    [10, 25, 30],
    [40, 5, 15],
    [20, 35, 50]
    ])
    result = arr6[(arr6 >= 20) & (arr6 <= 40)]
    print(result)
    print()
'''

# 7. 배열 [1, 2, 3, 4, 5, 6]에서 3의 배수가 아닌 값만 선택하세요.
arr7 = np.array([1, 2, 3, 4, 5, 6])
print('문제 7: \n', arr7[~(arr7 % 3 == 0)])
print()

'''
    리더님 방법
    arr7 = np.array([1, 2, 3, 4, 5, 6])
    result = arr7[arr7 % 3 != 0]
    print(result)
'''

# 8. 랜덤 정수(0~100) 10개 배열에서 아래와 같이 새로운 배열을 만드세요.
# • 50 이상인 값은 그대로
# • 50 미만인 값은 50으로 변경
arr8 = np.random.randint(1, 101, size = 10)
arr8[arr8 < 50] = 50
print('문제 8: \n', arr8)
print()

'''
    리더님 방법
    arr8 = np.random.randint(0, 101, 10)
    result = np.where(arr8 >= 50, arr8, 50)
    print(result)
'''

# 9. 2차원 배열에서 아래와 같이 분류된 문자열 배열을 생성하세요.
# • 70 이상 → "A"
# • 30 이상 70 미만 → "B"
# • 30 미만 → "C“

arr9 = np.array([[5, 50, 95], [20, 75, 10], [60, 30, 85]])
result = np.where(arr9 >= 70, 'A', np.where((arr9 >= 30) & (arr9 < 70), 'B', 'C'))
print('문제 9: \n', result)

'''
    리더님 방법
    arr9 = np.array([[5, 50, 95], [20, 75, 10], [60, 30, 85]])
    result = np.where(arr9 >= 70, 'A',
                                     np.where(arr9 >= 30, 'B', 'C))
    print(result)
'''

