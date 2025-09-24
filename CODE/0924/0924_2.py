# 예외
'''
    예외는 프로그램 실행 중에 발생하는 예상치 못한 상황
    예외가 발생하면 프로그램이 즉시 멈추지만, 예외 처리를 하면 프로그램을 계속 실행 가능
'''

# 오류 vs 예외의 차이
'''
    구문 오류(Syntax Error): 코드를 잘못 작성한 경우
        프로그램이 시작조차 못함
        코드를 수정해야만 해결
'''
# print('hello' -> 구문 오류

'''
    예외: 문법은 맞지만 실행 중 발생하는 문제
        프로그램 실행 중 발생
        try-except으로 처리 가능
'''

# result = 10 / 0 

# 예외 처리가 필요한 이유
# age = int(input('나이를 입력해주세요: '))

# 예외 처리
while True:
    try:
        age = int(input('나이를 입력해주세요: '))
        # 윗줄에서 예외 발생시 밑줄 코드는 실행이 안됨
        break
    except:
        print('숫자로 입력해주세요!')
        
# try 블록은 최소한으로
name = input('이름: ')

try:
    age = int(input('나이: '))
except:
    print('오류!')

print(f'안녕하세요 {name}님')

# try:
#     risky_code()
# except: # 모든 예외를 잡음(위험!)
#     pass # 예외 무시


num = int(input('숫자를 입력해주세요: ')) 
if num == 0:
    raise ZeroDivisionError('0 에러가 발생했습니다.')
result = 10 / num


try:
    int('abs') # ValueError
    # new_list = [1, 2, 3, 4]
    # print(new_list[5]) # IndexError
    # result = 10 / 0 # ZeroDivisionError
    num = int(input('숫자를 입력해주세요: ')) 
    if num == 0:
        raise ZeroDivisionError('0 에러가 발생했습니다.')
    result = 10 / num
except ValueError: # 특정 예외만
    print('값 오류 발생')
except IndexError:
    print('인덱스 범위를 초과했습니다.')
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except Exception as e: # 다른 예외는 로깅
    print(f'예상치 못한 오류: {e}')
else:
    # 정상적으로 실행이 끝나면 실행됨
    print('정상 작동 했습니다.')

finally:
    # 무조건 실행됨
    print('끝났습니다.')

