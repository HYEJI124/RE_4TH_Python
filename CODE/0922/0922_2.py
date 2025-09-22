# 접근 제어자
'''
    객체 지향 프로그래밍에서 클래스의 멤버(속성, 메서드)에 
    대한 접근 권한을 제어하는 메커니즘

    Python의 철학:
    Python은 프로그래머를 신뢰하는 철학을 가짐
    강제적 제한보다는 컨벤션과 문서화를 중시
    필요하다면 모든 것에 접근 가능(하지만 하지 말아야 할 것을 명확히 표시)
'''

class Car:
    def __init__(self, brand, model):
        self.brand = brand # public 속성
        self.model = model # public 속성
        self.speed = 0 # public 속성

    def accelerate(self, amount): # public 메서드
        '''외부에서 자유롭게 호출 가능'''
        self.speed += amount
        return f'속도가 {self.speed}km/h가 되었습니다.'
    
    def get_info(self): # public 메서드
        return f'{self.brand} {self.model}'
    
# 객체 생성
car = Car('tesla', 'model 3')
print(car.brand) # 정상 접근
print(car.model) # 정상 접근
print(car.get_info()) # 정상 호출
car.speed = 200 # 직접 수정 가능

# Private 속성/메소드(언더스코어 2개 __)
class SecuritySystem:
    def __init__(self, password):
        self.__password = password # private 속성
        self.__security_level = 'HIGH' # private 속성
        self.__failed_attempts = 0 # private 속성

    def __encrypt_password(self, pwd): # private 메서드
        '''내부적으로만 사용되는 암호화 메서드'''
        return pwd[::1] + 'encrypted'

    def __check_security(self): # private 메서드
        '''내부 보안 체크'''
        return self.__failed_attempts < 3
    
    
    def authenticate(self, password): # public 메서드
        if not self.__check_security(): # private 메서드 호출
            return '계정이 잠겼습니다.'
        # 인자로 받은 password를 암호화
        encrypted = self.__encrypt_password(password) # private 메서드 호출
        # 이미 password를 암호화 하고 비교
        if encrypted == self.__encrypt_password(self.__password):
            self.__failed_attempts = 0
            return '인증 성공'
        else:
            self.__failed_attempts += 1
            return f'인증 실패 {self.__failed_attempts}/3'
    
security = SecuritySystem('secret123')
# print(security.__password)
# security.__check_security()

print(security.authenticate('wrong')) # 인증 실패 (1/3)

# 절대 권장하지 않음!!!!!
print(security._SecuritySystem__password)



# property를 사용하지 않은 경우
class Circle1:
    def __init__(self, radius):
        self.__radius = radius

    def get_area(self): # 메서드로 접근
        return 3.14 * self.__radius ** 2
    
    def set_radius(self, radius):
        self.__radius = radius


# property를 사용한 경우
class Circle2:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def area(self): # 메서드로 접근
        return 3.14 * self.__radius ** 2
    
    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, radius):
        self.__radius = radius

c1 = Circle1(5)
print('c1', c1.get_area()) # 메서드 호출: 괄호 필요
c1.set_radius(10)
print()
print('c1', c1.get_area()) # 메서드 호출: 괄호 필요
print()

c2 = Circle2(4)
print('c2', c2.area) # 속성 접근: 괄호 없음!!!
c2. radius = 10
print('c2', c2.area) # 속성 접근: 괄호 없음!!!


class Vector:
    def __init__(self, x, y):
        '''생성자: 속성 초기화'''
        self.x = x
        self.y = y

    def __str__(self):
        '''print() 함수 호출 시'''
        return f'Vector {self.x} {self.y}'
    
    def __repr__(self):
        '''개발자를 위한 문자열 표현'''
        return f'Vector (x = {self.x} y = {self.y})'
    
    # 연산자 오버로딩
    def __add__(self, other):
        '''+ 연산 오버로딩'''
        return Vector(self.x + other.x, self.y + other.y)
    '''
    __sub__, __mul__, __eq__
    '''

    def __len__(self):
        '''len() 함수 호출시'''
        return int((self.x ** 2 + self.y ** 2) ** 0.5)
    
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1) ## __str__ 호출
print(repr(v1))

v3 = v1 + v2
print(v3)

print(len(v1))
