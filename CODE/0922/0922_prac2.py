# 실습3. 접근 제어와 정보은닉 연습
# 문제1. UserAccount 클래스 : 비밀번호 보호
# ▪ UserAccount 클래스를 정의하세요.
# ▪ 인스턴스 변수:
# • username: 사용자 이름
# • __password: private 변수로, 비밀번호 저장
# ▪ 생성자에서 사용자 이름과 비밀번호를 초기화하세요.
# ▪ 다음 메서드를 정의하세요:
# • change_password(old_pw, new_pw): 현재 비밀번호가 old_pw와 같을 때만 변경 허용, 틀리면 "비밀번호 불일치" 출력
# • check_password(password): 비밀번호 일치 여부를 반환 (True/False)

class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
        
    def change_password(self, old_pw, new_pw):
        if self.__password == old_pw:
            print('비밀번호가 변경 가능합니다.')
            self.__password = new_pw
            print(f'새로운 비밀번호: {self.__password}')
        else:
            print('비밀번호 불일치')
    
    def check_password(self, password):
        return self.__password == password
    
user1 = UserAccount('admin', 'admin123')

print('비밀번호 일치 여부: ', user1.check_password('admin1234'))
print('비밀번호 일치 여부: ', user1.check_password('admin123'))

user1.change_password('admin123', 'admin12345')

            

# 실습3. 접근 제어와 정보은닉 연습
# 문제 2. Student 클래스: 성적 검증(@property 사용)
# ▪ Student 클래스를 정의하세요.
# ▪ 인스턴스 변수 __score는 private으로 선언합니다.
# ▪ score에 대한 getter/setter를 @property를 사용하여 정의하세요.
# • 점수는 0 이상 100 이하만 허용되며, 범위를 벗어나면 ValueError를 발생시킵니다.(raise ValueError 사용)

class Student:
    
    def __init__(self, name):
        self.name = name
        self.__score = 0

    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self, value):
        if 0 <= value <= 100:
            self.__score = value
        else:
            raise ValueError
        
student1 = Student('홍길동')
student1.score = 49
print(f'{student1.name}님의 점수: {student1.score}')

student2 = Student('이영희')
student1.score = 120


