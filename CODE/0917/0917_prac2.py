# 실습 4. 리스트 컴프리헨션 연습 문제
# 문제 1. 제곱값 리스트 만들기

square = [x ** 2 for x in range(1, 11)]
print(square)
print()

# 문제 2. 3의 배수만 리스트 만들기

three = [x for x in range(1, 50) if x % 3 == 0]
print(three)
print()

# 문제 3. 문자열 리스트에서 길이가 5 이상인 단어만 뽑기
fruits = ["apple", "fig", "banana", "plum", "cherry", "pear", "orange"]
fruit = [x for x in fruits if len(x) >= 5]
print(fruit)
print()

