import numpy as np
# 1. 0부터 24까지 정수를 가진 배열을 만들고, (5, 5) 배열로 변환한 뒤 가운데 행(3번째 행)과 가운데 열(3번째 열)을 각각 1차원 배열로 출력하세요.
arr = np.arange(25).reshape(5, 5)
print('가운데 행: ',arr[2, :])
print('가운데 열: ',arr[:, 2])
print()


# 2. 0~99 난수로 이루어진 (10, 10) 배열을 생성하고, 짝수 인덱스의 행만 선택하여 출력하세요.
arr = np.random.randint(0, 100, (10, 10))
print('짝수 인덱스 행만 선택: \n', arr[::2])
print()

# 3. 0부터 49까지 정수를 가진 배열을 (5, 10) 배열로 변환한 후, 2행 3열부터 4행 7열까지의 부분 배열을 추출하세요.
arr = np.arange(50).reshape(5, 10)
print('부분 배열: \n', arr[1:4, 2:7])
print()

# 4. 0~9 난수로 이루어진 (4, 4) 배열을 생성하고, 각각 인덱싱으로 추출해 출력하세요.(for 이용)
# • 주대각선 요소 (왼쪽 위 → 오른쪽 아래)
# • 부대각선 요소 (오른쪽 위 → 왼쪽 아래)
arr = np.random.randint(0, 10, (4, 4))
print('주대각선 요소: \n', [arr[i, i] for i in range(4)])
print('부대각선 요소: \n', [arr[i, 3 - i] for i in range(4)])
print()

# 5. 0~9 난수로 이루어진 (3, 4, 5) 3차원 배열을 생성하고, 두 번째 층에서 첫 번째 행과 마지막 열의 값을 출력하세요.
arr = np.random.randint(0, 10, (3, 4, 5))
print('두 번째 층에서 첫 행 마지막 열: ', arr[1, 0, -1])
print()

# 6. 35부터 74까지의 순차적인 수로 이루어진 1차원 배열을 만들고 10x4 행렬로 변환 후 출력해주세요.
arr = np.arange(35, 75).reshape(10, 4)
print('10X4 배열: \n', arr)
print()

# 7. 6번에서 만든 배열을 맨 끝의 행부터 역순으로 출력해주세요.
print('6번 배열 역순 출력: \n', arr[::-1])
print()

# 8. 6번에서 만든 배열 중 두 번째 행부터 마지막 직전 행까지, 세번째 열부터 마지막 열까지 슬라이싱해서 출력해주세요.
print('부분 슬라이싱: \n', arr[1:-1 , 2:])
print()

# 9. 1부터 50까지의 난수로 된 5x6 배열을 만들고, 배열에서 짝수만 선택하여 출력하는 코드를 작성하세요.
arr = np.random.randint(1, 51, (5, 6))
print('짝수만: \n', arr[arr % 2 == 0])
print()

# 10. 0부터 99까지의 정수로 이루어진 (10, 10) 배열을 생성한 후, [1, 3, 5]번째 행과 [2, 4, 6]번째 열의 교차하는 원소들만 선택하여 출력하세요.
arr = np.arange(100).reshape(10, 10)
rows = [1, 3, 5]
cols = [2, 4, 6]
result = []
for r in rows:
    row_vals = [] # 현재 r에 대한 한 행을 담을 리스트
    for c in cols:
        row_vals.append(arr[r, c]) # arr의 (r, c) 위치 원소를 가져와 추가
    result.append(row_vals) # 완성된 한 행을 result 리스트에 추가

result = np.array(result)
print('교차 원소: \n', result)

# 방법 2. 'np.ix_' 사용
arr = np.arange(100).reshape(10, 10)
rows = [1, 3, 5]
cols = [2, 4, 6]
print("교차 원소:\n", arr[np.ix_(rows, cols)])

# 11. 0~9 난수로 이루어진 1차원 배열(길이 15)을 생성하고, 짝수 인덱스 위치에 있는 값들 중에서 5 이상인 값만 선택해 출력하세요.
arr = np.random.randint(0, 10, 15)
print('짝수 인덱스 & 값이 5 이상: ', arr[::2][arr[::2] >= 5])
print()
