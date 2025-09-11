a = 10
a += 5
print(a) #15

a -= 4
# a = a - 4
# a = 15 - 4
print(a) #11

a *= 3
print(a) #33

a /= 11
print(a) #3

a //= 2
print(a) #1

a **= 200
print(a) #1

a = 10
a %= 3
print(a) #1

# input
name = input("이름을 입력하세요: ")
print(name)

# input 문자형 -> 정수형
score = int(input("점수를 입력하세요: "))
print(f'점수는: {score + 10}')

# split() 공백을 구분자로 나누는 것
fruit = "사과 참외 수박".split()
print(fruit)

fruit1, fruit2, fruit3 = input().split()
print(fruit1, fruit2, fruit3, sep=',')

