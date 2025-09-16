# 실습 2. for문과 range
# 문제 1. 입력 받은 수의 합 구하기
n = int(input('숫자를 입력하세요:'))
number = []
for i in range(1, n+1):
    number.append(i)
print(sum(number))
print()

# 다른 방법
n = int(input('숫자를 입력하세요:'))

print(sum([x for x in range(1, n+1)]))

# 리더님 방법
num = int(input('숫자를 입력해주세요: '))

sum_num = 0
for i in range(1, num+1):
    sum_num += i

print(sum_num)

# 문제 2. 구구단 만들기
n = int(input('출력하고 싶은 단을 입력하세요:'))
for i in range(1, 10):
    print(f'{n} X {i} = {n * i}')
print()


# 리더님 방법
n = int(input('출력하고 싶은 단을 입력하세요:'))
for i in range(1, 10):
    print(f'{n} * {i} = {n * i}')

# 문제 3. 3의 배수의 합 구하기
three = []
for i in range(1, 101):
    if i % 3 == 0:
        three.append(i)
    else:
        pass
print(sum(three))
print()

# 다른 방법
sum = 0
for i in range(1, 101):
    if (i % 3 == 0):
        sum += i

print('총 합:', sum)

# 리더님 방법
total = 0
for i in range(3, 101, 3):
    total += i

print('total', total)

# 문제 4. 짝수이면서 5의 배수인 수 출력하기
n = int(input('숫자를 입력하세요:'))
number = []
for i in range(1, n+1):
    if (i % 2 == 0) & (i % 5 == 0):
        number.append(i)
    else:
        pass
print(number)

# 다른 방법
n = int(input('숫자를 입력하세요:'))
number = []
for i in range(1, n+1):
    if (i % 2 == 0) & (i % 5 == 0):
        print(i)

# 리더님 방법
n = int(input('숫자를 입력하세요:'))
for i in range(n+1):
    if (not i % 2) and (not i % 5): # 나누어 떨어지면 나머지 0, 0은 False, not False = True, 둘 다 True여야 출력
        print(i)