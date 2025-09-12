# for문 - 정해진 횟수만큼 반복

for i in range(5):
    print("안녕하세요")


# range(끝) - 0부터 끝 - 1 까지
range(5) # 0, 1, 2, 3, 4
# range(시작, 끝) - 시작부터 끝 - 1 까지
range(2, 6) # 2, 3, 4, 5
# range(시작, 끝, 간격) - 시작부터 끝 - 1 까지 간격만큼
range(2, 6, 2) # 2, 4

for i in range(5):
    print(f'i의 값 {i}')
print("========")
print()

for i in range(2, 6):
    print(f'i의 값 {i}')
print("========")
print()

for i in range(2, 6, 2):
    print(f'i의 값 {i}')
print("========")
print()

# 구구단 만들기
# 4단

for i in range(1, 10):
    print(f"4 X {i} = {4 * i }")

num = 4
print('4단')
for i in range(1, 10):
    print(f'{num} * {i} = {num * i}')
print("========")
print()

# 구구단 전체

for num in range(1, 10):
    print(f"{num} 단")
    for i in range(1, 10):
        print(f'{num} * {i} = {num * i}')
    print() # 단수마다 한 줄씩 띄고
    print("========")

# 리스트와 for문
# 리스트

# 과일 리스트 순회
fruits = ["사과", "바나나", "오렌지", "포도"]

for fruit in fruits:
    print(f"과일: {fruit}")
print()

scores = [65, 27, 87, 86]

for score in scores:
    print(f"점수: {score}")
print()

# 총점
total = 0
count = 0

for score in scores:
    total += score
    count += 1
    print(f"점수: {score}")

print("총점:",total)
print("평균:",total / count)
print("=========")

word = "python"
for char in word:
    print(char)

# 중첩 for문 - 반복 속의 반복
# 별 패턴 1: 직각삼각형

print("=========")
for i in range(1, 6):
    for j in range(i):
        print("*", end='')
    print()
print("=========")

# 정사각형 만들기

for i in range(1, 6):
    for j in range(1, 6):
        print("*", end='')
    print()
print("=========")

