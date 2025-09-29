# Numpy(numerical Python)는 파이썬에서 과학계산을 위한 핵심 라이브러리
# 데이터과학, 머신러닝, 과학 연구 분야에서 가장 중요한 도구 중 하나

# 속도 문제 해결
# 파이썬은 인터프리터 언어로 실행속도가 느림
# Numpy는 C언어로 구현되어 있어 대용량 데이터 연산을 매우 빠르게 처리함

# 메모리 효율성
# 파이썬 리스트: 각 요소가 객체로 저장되어 메모리 오버헤드가 큼
# Numpy 배열: 연속된 메모리 공간에 같은 타입의 데이터를 저장

# 벡터화 연산
# 반복문 없이 전체 배열에 대한 연산을 한 번에 수행


import numpy as np

print('Numpy 버전:', np.__version__)
print('Numpy 설치 경로:', np.__file__)

# ndarray(N-dimensional array) Numpy의 핵심 자료구조
# 같은 타입의 요소들을 담는 다차원 컨테이너

arr = np.array([1, 2, 3, 4, 5])
print('1. 객체 타입:', type(arr)) # 1. 객체 타입: <class 'numpy.ndarray'>
print('2. 데이터 타입:', arr.dtype) # 2. 데이터 타입: int64
print('3. 배열 모양:', arr.shape) # 3. 배열 모양: (5,)
print('4. 차원 수:', arr.ndim) # 4. 차원 수: 1
print('5. 전체 요소 수:', arr.size) # 5. 전체 요소 수: 5


# 중요한 차이점 1: 타입 고정
python_list = [1, 2.5, '3.' , True]
numpy_array = np.array([1, 2.5, '3.' , True])
print('파이썬 리스트:', python_list) # 파이썬 리스트: [1, 2.5, '3.', True]
print('Numpy 배열:', numpy_array) # Numpy 배열: ['1' '2.5' '3.' 'True'] <- 자동 변환됨(하나의 타입으로)


# 중요한 차이점 2: 연산 방식
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print('리스트 더하기:', list1 + list2) # 리스트 더하기: [1, 2, 3, 4, 5, 6]

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print('Numpy 배열 더하기:', arr1 + arr2) # Numpy 배열 더하기: [5 7 9]

# 정수 배열
int_array = np.array([1, 2, 3, 4, 5])
print('정수 배열:', int_array)
print('데이터 타입:', int_array.dtype)

# 실수 배열
float_array = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
print('실수 배열:', float_array)
print('데이터 타입:', float_array.dtype)

# 타입을 명시적으로 지정 배열
specified_array = np.array(['1', '2', 3, 4, 5], dtype = np.float32)
print('명시적 배열:', specified_array)
print('데이터 타입:', specified_array.dtype)

# 문자열 배열
string_array = np.array(['apple', 'banana', 'cherry'])
print('문자열 배열:', string_array)
print('데이터 타입:', string_array.dtype) # <U6 (유니코드 문자열, 최대 6자)

# 2차원 배열 (3X3 행렬)
matrix = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [4, 5, 6]
])

print()
print('2차원 배열:', matrix) 
print('모양:', matrix.shape) # 모양: (3, 3)
print('차원:', matrix.ndim) # 차원: 2
print('크기:', matrix.size) # 크기: 9


# for i in range(3):
#     for j in range(3):
#         print()

rows = []
for i in range(3):
    row = [i * 3 + j for j in range(4)]
    rows.append(row)                                  

matrix2 = np.array(rows)
print()
print('동적 생성 행렬:', matrix2)

# 3차원 배열 (2 X 3 X 4)
# 2개의 3 X 4 행렬로 구성
tensor = np.array([
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ],
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ],
])

print('3차원 배열 모양:', tensor.shape) # (2, 3, 4) -> 3행(줄), 4열(요소 개수)
print('차원:', tensor.ndim)

# numpy 내장 함수로 배열 생성
# 연속된 숫자 배열 arange
# 0부터 9까지
arr1 = np.arange(10)
print('0부터 9까지', arr1)

arr2 = np.arange(1, 11)
print('1부터 10까지', arr2)

arr3 = np.arange(1, 21, 2)
print('1부터 20까지 홀수만', arr3)

arr4 = np.arange(1, 11, 0.5) # range는 int만 가능 / arange는 float도 가능
print('1부터 11까지', arr4)

# 균등 간격 배열 linspace
# 시작, 끝 사이를 균등하게 나눈 숫자들
arr1 = np.linspace(0, 10, 5)
print('0부터 10까지 5개 요소\n', arr1) # step = (10 - 0)/(5 - 1) = 2.5

'''
     step = (stop - start) / num - 1
'''

arr2 = np.linspace(0, 10, 5, endpoint=False)
print('끝값 제외\n', arr2) # step = (10 - 0)/5 = 2

'''
     step = (stop - start) / num
'''

# 로그 간격 배열 logspace
# logspace(start, end, num)

# zeros: 0으로 채운 배열
print()
zeros_1d = np.zeros(5)
print('1차원 zeros:', zeros_1d)

print()
zeros_2d = np.zeros((3, 4))
print('2차원 zeros:', zeros_2d)

print()
zeros_2d_int = np.zeros((3, 4), dtype=int)
print('2차원 zeros:', zeros_2d_int)

matrix = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [4, 5, 6]
])
# 기존 배열과 같은 모양의 영 배열
print()
zeros_copy = np.zeros_like(matrix)
print('zeros_like:', zeros_copy)


# 1차원 일 배열
print()
ones_1d = np.ones(5)
print('1차원 ones:', ones_1d)

# 2차원 일 배열(3, 4)
print()
ones_2d = np.ones((3, 4))
print('2차원 ones:', ones_2d)

# 2차원 일 배열(3, 4) bool 타입
print()
ones_2d_bool = np.ones((3, 4), dtype=bool)
print('2차원 ones:', ones_2d_bool)


# full: 특정 값으로 채운 배열
print()
full_array = np.full((3, 4), 7)
print('2차원 배열:', full_array)

matrix = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [4, 5, 6]
])
print()
full_like = np.full_like(matrix, 999)
print('2차원 배열:', full_like)

print()
# 메모리만 할당, 값은 쓰레기값
empty_array = np.empty((2, 3))
print('2차원 배열(주의: 쓰레기값)', empty_array)

# 3X3 항등행렬
print()
identity = np.eye(3)
print('3X3 항등 행렬: \n', identity) # 대각선으로 1이 채워짐

# 4X5 행렬에서 대각선이 1
print()
matrix = np.eye(4, 5)
print('4X5 대각 1: \n', matrix) # 대각선으로 1이 채워짐

# 대각선 위치 조정(k 매개변수)
print()
matrix = np.eye(4, k = 1)
print('위쪽 대각선: \n', matrix) # 1의 위치가 대각선으로 1만큼 올라감


# 대각선 위치 조정(k 매개변수)
print()
matrix = np.eye(4, k = -1)
print('아래쪽 대각선: \n', matrix) # 1의 위치가 대각선으로 1만큼 내려감

# 정방 항등 행렬 - eye와 비슷
print()
identity = np.identity(4)
print('4X4 항등 행렬:\n', identity)

# 0과 1 사이의 균일 분포
'''
    균일분포
    어떤 구간 안에서 모든 값이 똑같은 확률로 나올 수 있는 분포
    치우침 없이 고르게 퍼져있는 확률 분포
'''
print()
random_uniform = np.random.rand(3, 4)
print('0부터 1 균일 분포: \n', random_uniform)
print()
rounded = np.round(random_uniform, 2)
print('0부터 1 균일 분포 (소수점 2자리): \n', rounded)

# 특정 범위의 균일 분포(예: 10 ~ 20)
print()
low, high = 10, 20
random_range = low + (high - low) * np.random.rand(3, 3)
print(f'{low}부터 {high} 균일 분포\n', random_range)

print()
uniform = np.random.uniform(low = 0, high = 100, size = (2, 3))
print('0부터 100 균일 분포\n', uniform)

# 정규분포 난수 생성
# 표준 정규 분포 (평균 0, 표준편차 1)
print()
random_normal1 = np.random.randn(3, 3)
print('표준 정규 분포\n', random_normal1)

# 평균 100, 표준편차 15인 정규분포
print()
mean, std = 100, 15
scores = mean + std * np.random.randn(1000)
print('표준 정규 분포\n', scores[:10])
print('실제 평균: ', scores.mean())
print('실제 표준편차: ', scores.std())

# 정수 난수
# 0 ~ 9 사이의 정수 난수
print()
random_int = np.random.randint(0, 10, size=(3, 4))
print('0 ~ 9 정수 난수\n', random_int)

# 주사위 시뮬레이션(1 ~ 6)
dice = np.random.randint(1, 7, size=10)
print('주사위 10번 굴리기\n', dice)

# 시드 설정(재현 가능한 난수)
print()
np.random.seed(42)
random1 = np.random.rand(5)
print('첫 번째 난수:', random1)

print()
np.random.seed(42)
random2 = np.random.rand(5)
print('두 번째 난수:', random2)
print('같은가?', np.array_equal(random1, random2))

# 새로운 방식(권장)
print()
rng = np.random.default_rng(seed=42)
random3 = rng.random((2, 3))
print('새로운 방식 난수:\n', random3)

