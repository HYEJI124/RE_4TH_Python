# 실습 1. for문 기본 문법 문제
# 문제 1. 리스트의 값을 두 배로 변환하기
numbers = [3, 6, 1, 8, 4]
new_num = []
for i in numbers:
    new_num.append(i * 2)
print(new_num)

numbers = [3, 6, 1, 8, 4]
print([num * 2 for num in numbers])

# 문제 2. 문자열의 길이 구해서 새 리스트 만들기
words = ['apple', 'banana', 'kiwi', 'grape']
length = []
for i in words:
    length.append(len(i))
print(length)

words = ['apple', 'banana', 'kiwi', 'grape']
len_words = [len(word) for word in words]
print(len_words)


# 문제 3. 좌표 튜플에서 x, y 좌표 나누기
x_values = []
y_values = []
coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]
for x, y in coordinates:
    x_values.append(x)
    y_values.append(y)
print('x_values:', x_values)
print('y_values:', y_values)


coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]
x_values = [x for x, y in coordinates]
y_values = [y for x, y in coordinates]

print('x_values:', x_values)
print('y_values:', y_values)

