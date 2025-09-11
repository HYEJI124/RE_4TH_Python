# # 비교 연산자
# x = 10
# y = 20

# print(f'x == y: {x == y}')
# print(f'x != y: {x != y}')
# print(f'x > y: {x > y}')
# print(f'x >= y: {x >= y}')
# print(f'x < y: {x < y}')
# print(f'x <= y: {x <= y}')

# x = 15
# y = 15
# print(f'x >= y: {x >= y}') # True
# print(f'x <= y: {x <= y}') # True

# # 논리 연산자
# # AND: 둘 다 True여야 True
# print(True and True) # True
# print(True and False) # False
# print(False and True) # False
# print(False and False) # False

# # OR: 하나라도 True면 True
# print(True or True) # True
# print(True or False) # True
# print(False or True) # True
# print(False or False) # False

# # 논리 부정
# print(f'not True: {not True}')
# print(f'not False: {not False}')

# print(True and False or True) # True
# print(True and (False or True) and False) # False

# # 단축 평가
# if False and print("단축 평가"):
#     print("실행")

# if True or print("단축 평가"):
#     print("실행")

# if False or print("단축 평가") or True:
#     print("실행")

# # 조건문
# a = 10
# if a != 10:
#     print(f'a: {a}')
#     print('if문 블럭 안')
# print('if문 블럭 밖')

# # 조건문 연습 1
# age = 20

# if age >= 18:
#     print("성인입니다.")

# # 조건문 연습 2
# name = "ethan"
# name = ""

# if name:
#     print("이름이 존재합니다.") # 이름이 존재합니다. 안나옴

# # 조건문 연습 3

# if True:
#     print("무조건 실행")

# if False:
#     print("실행되지 않습니다")

# if True:
#     pass # 다음에 작성하겠다.
# print('조건문과 상관없습니다.')

# # if-else 연습 1
# name = ""

# if name:
#     print(f"이름은: {name}")
# else:
#     print("이름을 작성해주세요")

# # if-else 연습 2
# if True:
#     print("if 실행")
# else:
#     print("else 실행")

# if False:
#     print("if 실행")
# else:
#     print("else 실행")

name = "철수"

if name == "김철수":
    print(f'김철수 입니다.')
elif name == "철수":
    print(f"철수 입니다.")
else:
    print(f"이름을 입력해주세요.")

age = 20
name = "철수"
grade = 2

if name:
    print(f"이름: {name}")

if age > 20:
    print("성인입니다.")
else:
    print("미성년자입니다.")

if grade > 3:
    print("고학년 입니다")
elif grade == 2:
    print("2학년 입니다")
else:
    print("1학년 입니다")
