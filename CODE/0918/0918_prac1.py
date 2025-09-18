# 실습 3. 중첩 while문 연습문제
# 문제 1. 로그인 시스템 구현
# 로그인 시스템을 만들고 있습니다. 순서대로 ID와 비밀번호를 입력 받고, ID와 비밀번호 모두 맞으면 로그인 성공 메시
# 지를 출력하세요.
# 조건
# 임의의 ID와 비밀번호를 세팅합니다.
# 잘못된 ID일 경우 "ID가 존재하지 않습니다." 를 출력하고 다시 ID를 입력 받습니다.
# ID가 맞으면 비밀번호를 입력 받고, 비밀번호가 틀리면 "비밀번호가 틀렸습니다." 를 출력하고 다시 입력 받습니다.
# 둘 다 맞으면 "로그인 성공!" 을 출력하고 프로그램을 종료합니다.

key_ID = 'hyeji'
key_PW = 'gpwl'

id = input('ID를 입력하세요:')

while True:
        if key_ID == id:
              password = input('PW를 입력하세요:')
              if key_PW != password:
                    print('비밀번호가 틀렸습니다.')
                    password = input('PW를 다시 입력해주세요:')
              else:
                    print('로그인 성공!')
                    break
        else:
            print('ID가 존재하지 않습니다.')
            id = input('ID를 다시 입력해주세요:')

# 리더님 방법

saved_id = 'admin'
saved_pw = 'admin123'

input_id = ''
input_pw = ''

while True:
    input_id = input('ID를 입력하세요:')

    if saved_id == input_id:
        while True:
            input_pw = input('PW를 입력하세요:')
            if saved_pw == input_pw:
                print('로그인 성공!')
                break # PW while문 탈출
            else:
                print('비밀번호가 틀렸습니다.')
        break # ID while문 탈출
    else:
        print('ID가 존재하지 않습니다.')