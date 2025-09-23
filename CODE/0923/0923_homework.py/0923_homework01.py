# # 실습2. math 모듈 사용해보기
# # 문제 1. 실제 거리 계산: 좌표 두 점 사이 거리 구하기
# # 문제 설명
# # • 두 점 (x1, y1), (x2, y2)의 좌표를 입력받아 두 점 사이의 실제 거리를 소수 둘째 자리까지 출력하세요.
# # 힌트:
# # • 피타고라스 정리: 거리 = sqrt((x2-x1)^2 + (y2-y1)^2)
# # • math.sqrt(), math.pow() 함수 활용

# from math import sqrt, pow

# x1, y1 = int(input('첫 번째 점의 x좌표를 입력하세요:')), int(input('첫 번째 점의 y좌표를 입력하세요:'))
# x2, y2 = int(input('두 번째 점의 x좌표를 입력하세요:')), int(input('두 번째 점의 y좌표를 입력하세요:'))


# distance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
# print(round(distance, 2))

# # 실습2. math 모듈 사용해보기
# # 문제 2. 상품 나누기: 최소 공배수와 최대 공약수
# # 문제 설명
# # • 어떤 학급에 학생이 18명, 선생님이 24명 있습니다.
# # • 두 집단이 모두 공평하게 나눠 가질 수 있는 최대의 간식 개수(최대 공약수)와
# # • 포장 단위별로 동시에 맞게 나누어 떨어지는 최소 간식 개수(최소 공배수)를
# # 구하는 코드를 작성하세요.
# # 힌트:
# # • math.gcd(), math.lcm() (lcm은 Python 3.9+)

# from math import gcd, lcm

# print(f'두 집단이 모두 공평하게 나눠 가질 수 있는 최대의 간식 개수(최대공약수): {gcd(18, 24)}개')
# print(f'포장 단위별로 동시에 맞게 나누어 떨어지는 최소 간식 개수(최소공배수): {lcm(18, 24)}개')

# # 실습3. 로또 번호 뽑기
# # 문제 설명
# # 1. 2. 1~45까지의 수 중에서 랜덤으로 6개의 숫자를 뽑는다.
# # 6개의 숫자 중 중복되는 숫자가 없도록 한다.
# # 3. 오름차순으로 정렬한 결과를 출력한다.

# import random

# def lotto():
#     numbers = random.sample(range(1, 46), 6) # 리스트 (혹은 범위)에서 원하는 개수만큼 무작위로, 중복 없이 선택
#     numbers.sort()
#     return numbers

# print(lotto())

# # 실습4. 가위 바위 보 게임 만들기
# # 문제 설명
# # 1. 컴퓨터는 ‘가위’, ‘바위’, ‘보’ 중 하나를 무작위로 선택합니다.
# # 2. 사용자는 키보드로 ‘가위’, ‘바위’, ‘보’ 중 하나를 직접 입력합니다.
# # 3. 둘의 결과를 비교해 승, 무, 패를 판단하여 출력하세요.
# # 요구 사항
# # 1. 2. 3. random 모듈의 함수를 사용할 것
# # 사용자 입력은 input()으로 받을 것
# # 승패 판정(비교) 로직은 if/elif/else로 직접 구현할 것

# import random

# rsp = ['가위', '바위', '보']
# computer = random.choice(rsp)

# user = input('가위, 바위, 보 중 하나르 입력하세요: ')

# print(f'컴퓨터: {computer}, 사용자: {user}')

# if computer == user:
#     print('비겼습니다.')

# elif computer == '가위':
#     if user == '보':
#         print('졌습니다.')
#     else:
#         print('이겼습니다.')

# elif computer == '바위':
#     if user == '가위':
#         print('졌습니다.')
#     else:
#         print('이겼습니다.')

# elif computer == '보':
#     if user == '주먹':
#         print('졌습니다.')
#     else:
#         print('이겼습니다.')

# else:
#     print('잘못 입력하셨습니다. 가위, 바위, 보 중 하나를 입력하세요.')

# # 실습5. 다음 생일까지 남은 날짜 계산하기
# # 문제 설명
# # 1. 사용자로부터 생일(월-일, 예: 07-25)을 입력 받으세요.
# # 2. 오늘 날짜를 기준으로 올해 또는 내년의 생일까지 남은 날짜(일 수)를 계산해서 출력하세요.
# # • 올해 생일이 지났으면 내년까지 남은 일수로, 아직 안 지났으면 올해 생일까지 남은 일수로 계산
# # 요구 사항
# # • 날짜 연산에는 반드시 datetime 모듈을 사용할 것.

# from  datetime import datetime, timedelta

# birthday = input('생일(MM-DD)을 입력하세요: ')

# today = datetime.today()
# current_year = today.year

# this_year_birthday = datetime.strftime(f'{current_year} - {birthday}', '%Y-%m')

# if this_year_birthday < today:
#     birthday_next = datetime.strftime(f'{current_year + 1} - {birthday}', '%Y-%m')
#     remaining_days = (birthday_next - today).days
# else:
#     remaining_days = (this_year_birthday - today).days

# print(f'다음 생일까지 {remaining_days}일 남았습니다.')

# 실습6. 타자 연습 게임 만들기
# 문제 설명
# 1. 영단어 리스트 중 무작위로 단어가 제시됩니다.
# 2. 사용자는 해당 단어를 정확히 입력해야 다음 문제로 넘어갈 수 있습니다.
# 3. 10문제를 모두 맞히면, 게임이 종료되고 총 소요 시간이 출력됩니다.
# 4. 틀린 경우에는 "오타! 다시 도전!" 메시지를 출력하고, 같은 문제를 다시 도전하게 합니다.
# 5. 게임이 시작되기 전, 엔터키를 누르면 시작합니다.
# 요구 사항
# 1. 단어는 미리 주어진 리스트에서 random.choice()로 무작위 선택
# 2. input()으로 사용자 입력
# 3. time.time()으로 시작~종료 시간 측정, 소요 시간 계산
# 4. 문제마다 번호가 함께 출력
# 5. 통과/오타 메시지, 총 타자 시간까지 출력

# import random

# word = 

# # sys.exit(0) 파이썬 프로그램 종료
# import sys

# x = input('수 입력: ')
# n = int(x)

# if n == 0:
#     print('0으로 나눌 수 없습니다.')
#     sys.exit(0)

# result = 10 / n

# print(result)

# # 새 폴더 생성 후, 파일 목록 출력하기
# import os

# # 1. 현재 작업 디렉터리 확인
# print('현재 작업 디렉터리:', os.getcwd())

# # 2. 새 폴더 생성(이미 있으면 예외 발생 가능)
# folder_name = 'sample_folder'
# if not os.path.exists(folder_name):
#     os.mkdir(folder_name)
#     print(f'{folder_name} 폴더를 생성했습니다.')
# else:
#     print(f'{folder_name} 폴더가 이미 존재합니다.')

# # 3. 현재 디렉터리 내 파일/폴더 목록 출력
# print('현재 디렉터리 내 파일 및 폴더 목록:')
# print(os.listdir())
