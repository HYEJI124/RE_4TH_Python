# 실습 1. while문 연습문제
# 문제 1. 비밀 코드 맞추기(1)

# 변수 secret_code에는 “codingonre3”라는 문자열이 저장되어 있습니다.
# 사용자에게 "비밀 코드를 입력하세요:" 라고 안내 문구를 출력합니다.
# 사용자가 입력한 코드가 secret_code와 다를 경우, 계속해서 다시 입력 받습니다.
# 코드가 맞으면 "입장이 허용되었습니다!" 를 출력하고 프로그램을 종료합니다.

secret_code = "codingonre3"
code = input('비밀 코드를 입력하세요:')

while secret_code != code:
    print('비밀 코드를 다시 입력하세요')
    code = input('비밀 코드를 입력하세요:')
    if secret_code == code:
        break
print("입장이 허용되었습니다!")

# 다른 방법
secret_code = "codingonre3"

code = input('비밀 코드를 입력하세요:')

while code != "codingonre3":
    code = input('비밀 코드를 입력하세요:')

print("입장이 허용되었습니다!")

# 리더님 방법
secret_code = "codingonre3"

while secret_code != input('비밀코드를 입력하세요:'):
    print('비밀 코드가 틀렸습니다. 다시 시도하세요.')

print('입장 완료! 환영합니다.')

# 문제 2. 업다운 게임
# 입력한 숫자가 정답보다 크면: "입력한 숫자보다는 작아요."
# 입력한 숫자가 정답보다 작으면: "입력한 숫자보다는 커요."
# 숫자를 맞히면: "{입력 횟수}번 만에 정답을 맞췄습니다." 라고 출력합니다

# 리더님 방식
# 랜덤 숫자(1부터 100 사이의 무작위 정수)

import random
random_value = random.randrange(1, 101)

count = 1
num = int(input("숫자 입력:"))

while num != random_value:
    if num < random_value:
        print(f'{num}보다는 커요.')
    else:
        print(f'{num}보다는 작아요.')
    num = int(input("숫자 입력:"))
    count += 1
print(f'{count}번 만에 정답을 맞췄습니다!')



