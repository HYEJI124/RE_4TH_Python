# 실습3. 로그인 성공 시 전화번호 저장하기
# 1. 로그인 성공 시, 사용자에게 "전화번호를 입력하세요."라는 메시지를 출력한 뒤
# 전화번호 입력 받기
# 2. 사용자로부터 입력 받은 전화번호를 이름과 함께 member_tel.txt에 기록
# 3. 새로운 사람이 로그인 성공 시 member_tel.txt에 전화번호 추가하기
# 4. member_tel.txt에 이미 존재하는 사람이 로그인 성공 시 전화번호 수정하기

def saved_phone(input_id):
    input_phone = input('전화번호를 입력하세요: ')
    members = {} # dict을 생성
    # try 시도하다. 에러가 발생하면 except으로 처리
    try:
        with open('member_tel.txt', 'r+', encoding='utf-8') as f2: # member_tel.txt가 존재하지 않으면 에러 발생
            for line in f2:
                saved_name, saved_phone = line.strip().split() # split 하면 이름과 전화번호로 나눠짐
                # 딕셔너리에 추가
                members[saved_name] = saved_phone
                # {
                #   철수: 123456789,
                #   영희: 010-2345-5959
                # }
    except:
        pass
            
    # 딕셔너리에 추가, 있으면 수정
    members[input_id] = input_phone
    # input_id: 철수 input_phone: 010-2345-3349
    # {
    #   철수: 010-2345-3349,
    #   영희: 010-2345-5959
    # }

    with open('member_tel.txt', 'w', encoding='utf-8') as f2:
         for name, phone in members.items():
             f2.write(f'{name} {phone} \n')


# 실습1. 회원 명부 작성하기
# 1. 사용자에게 3명의 회원에 대한 이름 비밀번호 입력 받기
# 2. 사용자로부터 입력된 정보를 member.txt에 기록 (파일 쓰기모드)
# 3. member.txt에 저장된 회원명부 출력 (파일 읽기모드)

with open('member.txt', 'w', encoding='utf-8') as f:
    for i in range(3):
        user_id = input('아이디를 입력해주세요: ')
        user_pw = input('비밀번호를 입력해주세요: ')
        f.write(f'{user_id} {user_pw}\n')


with open('member.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.split()[0]) # 아이디만 출력
        print(line.strip()) # 비밀번호 같이 출력


# 실습2. 회원 명부를 이용한 로그인 기능
# 앞에서 만든 member.txt 회원 명부를 활용해서
# 1. 사용자에게 "이름을 입력하세요."라는 메세지를 출력한 뒤 이름 입력 받기
# 2. 사용자에게 "비밀번호를 입력하세요."라는 메세지를 출력한 뒤 비번 입력 받기
# 3. member.txt 에서 한 줄씩 "이름"과 "비번"을 검사하여 로그인 성공 시 "로그인 성공" 실패 시 "로그인 실패" 출력

with open('member.txt', 'r', encoding='utf-8') as f:
    input_id = input('아이디를 입력해주세요: ')
    input_pw = input('비밀번호를 입력해주세요: ')
    for line in f:
        user_id, user_pw = line.strip().split()
        if user_id == input_id and user_pw == input_pw:
            print('로그인 성공')
            # 전화번호 저장 함수
            saved_phone(input_id)
            break
    else:
        print('로그인 실패')


