# 아스키코드 사용
# 소문자, 대문자 구분
print(chr(65))
print(chr(102))
print(chr(97))
print(chr(90))


new_list = [1, 2, 3]

try:
    print(new_list.index(3)) # error 발생
except:
    print('에러가 발생했습니다.')

# 함수 안의 것은 함수 안에서만 유효 -> 함수 밖에서는 못 씀
def add(a, b):
    a += 1
    return a + b

# print(a) # 불가


count = 10

def count_print():
    global count # 전역 변수임을 명시
    count = count + 1
    print(count)
    return count

count_print()
print(count)

a = 10
b = a # 10

a += 1
print('a', a)
print('b', b)

a = 10

def count_print(b):
    b += 1
    print('def count: ', b)
    return b

a = count_print(b=a)
print(b)

def outer():
    a = 10

    def inner():
        nonlocal a
        a += 5
        print(f'[inner] a: {a}') # 15
    inner()
    print(f'[outer] a: {a}')

outer()