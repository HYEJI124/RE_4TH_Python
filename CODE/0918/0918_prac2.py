# 실습 1. 사칙연산 계산기 함수 만들기
# 문제 1. 사칙연산 계산기 함수 만들기
# 두 개의 숫자와 연산자를 인자로 받아, 해당 연산 결과를 반환하는 함수를 작성하세요.
# 요구사항
# 함수 이름은 calculate로 합니다.
# 매개변수는 a, b, operator 세 개입니다.
# operator는 문자열이며, 다음 중 하나입니다: "+", "-", "*", "/"
# 나눗셈은 결과를 실수(float) 로 반환합니다.
# 올바르지 않은 연산자가 들어오면 "지원하지 않는 연산입니다"라는 문자열을 반환하세요

a = int(input('숫자를 입력해주세요:'))
b = int(input('숫자를 입력해주세요:'))
operator = input('연산자를 입력해주세요:')

if operator == '+':
    print(f'a + b = {a + b}')
elif operator == '-':
    print(f'a - b = {a - b}')
elif operator == '*':
    print(f'a * b = {a * b}')
elif operator == '/':
    if b != 0:
        print(f'a / b = {a / b}')
    else:
        print('0으로 나눌 수 없습니다.')
else:
    print('지원하지 않는 연산입니다.')



a = int(input('숫자를 입력해주세요:'))
b = int(input('숫자를 입력해주세요:'))
operator = input('연산자를 입력해주세요:')

# 결과값
result = 0

if operator == '+':
    result = a + b
elif operator == '-':
    result = a - b
elif operator == '*':
    result = a * b
elif operator == '/':
    result = a / b 

print(result)


def calculate(a, b, op):
    # 결과값
    result = 0
    
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        result = a / b 
    else:
        result = '지원하지 않는 연산입니다.'
    
    return result

print(calculate(2, 3, '+'))
print(calculate(2, 3, '-'))
print(calculate(2, 3, '*'))
print(calculate(2, 3, '/'))
print(calculate(2, 3, '//'))

