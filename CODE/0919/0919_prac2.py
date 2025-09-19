# 실습4. 거듭 제곱

# 자연수 a와 b가 주어졌을 때, a의 b제곱을 계산하는 재귀 함수를 만들어 봅시다.
# 거듭 제곱은 다음과 같이 정의됩니다:

def square(a, b):
    if b == 1:
        return a
    
    return a * square(a, b - 1)

print(square(2, 3))

# 리더님 방식
def power(a, b):
    if b == 0:
        return 1
    
    return a * power(a, b - 1)

power(2, 3)
# 2 X power(2,2)
# 2 X 2 X power(2,1)
# 2 X 2 X power(2,0)
# 2 X 2 X 2 X 1

# 실습5. 팩토리얼(Factorial)
# 먼저 반복문을 활용해서 팩토리얼을 구현합니다.
# 1번을 바탕으로 작동 원리를 파악하고, 재귀함수를 이용해서 팩토리얼을 구현
# 합니다.
# 디버거를 이용해 재귀함수의 작동을 확인합니다.

# 연습 1. 1부터 n까지의 합
# 1 + 2 + 3 + ... + n을 구하세요.
def sum_to_n(n):
    '''
    예: sum_to_n(5) = 1 + 2 + 3 + 4 + 5 = 15
    '''
    if n == 1:
        return 1
    return n + sum_to_n(n - 1) # return sum(range(1, n+1)) 

result = sum_to_n(5)
print(result)


# 연습 2. 문자열 뒤집기
# 문자열을 재귀로 뒤집으세요.

def reverse_string(s):
    '''
    예: reverse_string('hello') = 'olleh'
    '''
    if len(s) <= 1:
        return s
    
    return s[-1] + reverse_string(s[:-1])
    
text = reverse_string('hello')
print(text)

# 리더님 방식
def reverse_string(s):
    '''
    예: reverse_string('hello') = 'olleh'
    '''
    if len(s) == 0:
        return ''
    
    return s[-1] + reverse_string(s[:-1]) # return s[::-1]

text = reverse_string('hello')
print(text)