# 람다 함수(Lambda Function)
'''
    람다 함수는 이름 없는 한 줄짜리 간단한 함수
'''

print((lambda x: x ** 2)(5))

# 일반 함수
def square(x):
    return x ** 2

# 람다 함수(같은 기능)
square_lambda = lambda x: x ** 2

print('square(5)', square(5))
print('square_lambda(5)', square_lambda(5))


# 여러 매개변수
add = lambda x, y: x + y
print(add(5, 3))

# map(): 모든 요소에 함수 적용
numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x ** 2, numbers))
# [1, 4, 9, 16, 25]

def increment_func(x):
    return x + 1

incre_numbers = list(map(increment_func, numbers))
print(incre_numbers)

# filter
evens = list(filter(lambda x: x > 3, numbers)) # True 값만 반환
print(evens)

# sorted() 정렬 기준 지정

students = [
    {'name': '홍길동', 'score': 80},
    {'name': '김철수', 'score': 92},
    {'name': '이영희', 'score': 72},
]

students.sort(key=lambda x: x['name'], reverse=True)
for student in students:
    print(f'{student['name']}:{student['score']} 점')