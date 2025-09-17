# 실습 3. 중첩 for문 연습 문제
# 문제 1. 구구단 만들기

for i in range(2, 10):
    print(f'[ {i} 단 ]')
    for j in range(1, 10):
        print(f'{i} X {j} = {i * j}')
    print()

# 문제 2. 중첩 for문 별찍기
# 왼쪽 정렬
n = int(input('정수를 입력하세요:'))
print()

for i in range(1, n+1):
    print('*' * i, '' * (n - i))

print()

# 가운데 정렬
n = int(input('정수를 입력하세요:'))
print()

for i in range(1, n+1):
    print(' ' * (n - i), '*' * (2 * i -1), ' ' * (n - i))

print()

# 오른쪽 정렬
n = int(input('정수를 입력하세요:'))
print()

for i in range(1, n+1):
    print(' ' * (n - i), '*' * (i))

print()



# 리더님 방식
n = int(input('몇 줄 ? >'))

print('[왼쪽 정렬]')
for i in range(1, n + 1):
    for j in range(i):
        print('*', end='')
    print()


print('[가운데 정렬]')
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end= '')
    # 2 * i - 1
    for k in range(2 * i - 1):
        print('*', end='')
    print()


print('[오른쪽 정렬]')
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end= '')
    for k in range(i):
        print('*', end='')
    print()