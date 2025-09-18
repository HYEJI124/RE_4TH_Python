# 실습 2. 가변인자 연습하기
# *args 사용 연습
# 문제 1. 숫자 여러 개의 평균 구하기
# 숫자를 몇 개든 받을 수 있는 average() 함수를 만들어보세요.
def average(*args):
    if len(args) == 0:
        return 0
    return sum(args)/len(args)

print(average(1,2,3,4))
print(average(340, 495, 239, 123))

# 리더님 방법
def average(*args):
    total = sum(args)
    size = len(args)
    return total / size

print(average(1, 2, 3, 4, 5,))
print(average(31, 22, 37, 24, 25, 32))

# 문제 2. 가장 긴 문자열 찾기(max 함수에 대해 찾아보고 풀기)
# 여러 개의 문자열을 받아, 가장 긴 문자열을 반환하는 함수를 만들어보세요.
# max() 함수에서 key=len을 쓰면 문자열 길이 기준으로 최대값 찾을 수 있음
def longest_string(*args):
    if len(args) == 0:
        return None
    return max(args, key=len)

print(longest_string('melong', 'hi', 'hahaha', 'hohohoho'))

# 리더님 방법 1
def max_len_word(*args):
    return max(args, key=len)

print(max_len_word('hello', 'banana', 'car', 'apple'))

# 리더님 방법 2
def max_len_word(*args):
    pass

print(max(['hello', 'banana', 'car', 'apple'], key=len))

# **kwargs 사용 연습
# 문제 3. 사용자 정보 출력 함수
# 사용자의 이름, 나이, 이메일 등의 정보를 받아 출력하는 함수를 **kwargs로 구현하세요.
# 정보가 몇 개가 들어오든 모두 출력해야 합니다.

def information(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} {value}')

information(name = '홍길동', age = 30, email = 'ethan@gmail.com', city = '서울')

# 문제 4. 할인 계산기
# 상품 가격 목록을 **kwargs로 받아, 각각 10%씩 할인된 가격을 출력하는 함수를 작성하세요.

def discount(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} {0.9 * value}')

discount(item1 = 49400, item2 = 69000, item3 = 50000)

# 리더님 방법
def product_info_print(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} {0.9 * value}')

product_info_print(product1=1000, product2=2500, product3=3200, product4=1600)