# 실습3. 전역 변수 연습하기

# 로그인/로그아웃 전역 상태 관리
# 전역 변수로 로그인한 사용자 저장 및 로그아웃 기능을 구현해 봅시다.

# 요구사항
# 전역 변수 current_user는 로그인한 사용자의 이름을 저장합니다.
# login(name) 함수는 사용자를 로그인시키고, logout() 함수는 로그아웃 상태로 만듭니다.
# 이미 로그인된 상태에서 다시 로그인하면 "이미 로그인되어 있습니다"를 출력합니다.
# 로그아웃하지 않고 로그인을 여러 번 시도할 수 없도록 합니다.

current_user = ''

def login(name):
    global current_user

    if current_user == '':
        current_user = name
        print(f'{name}님 로그인 성공')
    else: 
        print('이미 로그인되어 있습니다.')

def logout():
    global current_user
    current_user = ''
    print('로그아웃되었습니다.')

login('Ian')
login('CodingOwl')
logout()
logout()
login('codingowl')
print('현재 사용자:', current_user)

# 다른 방법
# 전역 변수: 현재 로그인한 사용자 저장
current_user = None  

def login(name):
    global current_user
    if current_user is not None:
        print("이미 로그인되어 있습니다.")
    else:
        current_user = name
        print(f"{name}님이 로그인했습니다.")

def logout():
    global current_user
    if current_user is None:
        print("로그인 상태가 아닙니다.")
    else:
        print(f"{current_user}님이 로그아웃했습니다.")
        current_user = None


# 실행 예시
login("Hyeji")    # Hyeji님이 로그인했습니다.
login("Park")     # 이미 로그인되어 있습니다.
logout()          # Hyeji님이 로그아웃했습니다.
logout()          # 로그인 상태가 아닙니다.

# 리더님 방법
current_user = None # 로그아웃 상태

def login(name):
    global current_user
    if current_user != None:
        print('이미 로그인 되어 있습니다.')
    else:
        current_user = name
        print(f'{name}님 로그인 성공!')

def logout():
    global current_user
    if current_user == None:
        print('로그인 되어 있지 않습니다.')
    else:
        print(f'{current_user}님 로그아웃 성공!')
        current_user = None

login('Ian')
login('CodingOwl')
logout()
logout()
login('codingOwl')
print('현재 사용자:', current_user)


