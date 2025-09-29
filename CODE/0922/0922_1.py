# 클래스
'''
    클래스는 객체를 만들기 위한 설계도
    클래스 = 붕어빵 틀
    객체(인스턴스) = 실제로 만들어진 붕어빵

    클래스를 사용하면 관련된 데이터와 기능을 하나로 묶어서 관리
'''

'''
    코드 재사용성: 한 번 작성한 코드를 여러 곳에서 활용
    유지보수 용이: 수정사항이 있을 때 클래스만 수정하면 됨
    코드 구조화: 복잡한 프로그램을 체계적으로 구성
    현실 세계 모델링: 실제 사물이나 개념을 프로그램으로 표현
'''

class 클래스_이름:
    def __init__(self):
        pass

    def 메서드이름(self):
        # 메서드 코드
        pass

class Car:
    def __init__(self, brand, model, color):
        self.brand = brand # 브랜드
        self.model = model # 모델명
        self.color = color # 색상
        self.speed = 0 # 현재 속도

    def accelerate(self, increase):
        '''속도를 증가시키는 메서드'''
        # 최대 속도가 150
        self.speed = min(150, self.speed + increase) # 최대 속도가 150
        print(f'속도가 {increase}km/h 증가했습니다. 현재 속도: {self.speed}km/h')

    def brake(self, decrease):
        '''속도를 감소시키는 메서드'''

        self.speed = max(0, self.speed-decrease) # 속도는 0 미만이 될 수 없음
        print(f'속도가 {decrease}km/h 감소했습니다. 현재 속도: {self.speed}km/h')

    def info(self):
        '''차량 정보를 출력하는 메서드'''
        print(f'브랜드: {self.brand}')
        print(f'모델명: {self.model}')
        print(f'색상: {self.color}')
        print(f'현재 속도: {self.speed}km/h')

# 객체 생성 및 사용
my_car = Car('tesla', 'model 3', '빨간색')
# my_car 객체(인스턴스)의 정보 출력
my_car.info()
print()
# my_car 객체(인스턴스)의 속도 증가
my_car.accelerate(80)
print()
# my_car 객체(인스턴스)의 속도 감소
my_car.brake(30)
print()
my_car.info()
print()
print()
print()
print()


class Student:
    def __init__(self, name, age, student_id):
        '''생성자: 학생 객체를 초기화'''
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = [] # 성적 리스트 초기화
        print(f'학생 {name}의 정보가 등록되었습니다.')

    def add_grade(self, grade):
        '''성적 추가 메서드'''
        self.grades.append(grade)
        print(f'{self.name}의 성적 {grade}점이 추가되었습니다.')

    def get_averate(self):
        '''평균 성적 계산'''
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

    def __del__(self):
        '''
            소멸자
            객체가 메모리에서 삭제될 때 호출되는 메서드
        '''
        print(f'{self.name}의 정보가 삭제되었습니다.')


# 객체(인스턴스) 생성
student1 = Student('김철수', 20, '20250001')
print()
student1.add_grade(70)
print()
student1.add_grade(60)
print()

student2 = Student('이영희', 22, '20230001')
print()

student1.get_averate()
print()
print('평균 점수', student1.get_averate())

del student2

# 인스턴스 변수, 클래스 변수
'''
    인스턴스 변수: 각 개체마다 독립적으로 가지는 변수
    클래스 변수: 모든 객체가 공유하는 변수

'''

class BannkAccount:
    # 클래스 변수
    bank_name = '파이썬 은행'
    total_accounts = 0
    interest_rate = 0.02 # 이자율

    def __init__(self, owner, balance):
        self.owner = owner # self. owner -> 속성에 해당
        self.balance = balance
        self.account_number = BannkAccount.total_accounts + 1

        # 클래스 변수 업데이트 -> 없으면 모두 total_accounts가 1
        BannkAccount.total_accounts += 1

    def deposit(self, amount):
        '''입금 메서드'''
        if amount > 0:
            self.balance += amount
            print(f'{amount}원이 입금되었습니다. 잔액: {self.balance}원')
        else:
            print('입금액은 0보다 커야 합니다.')


    def withdraw(self, amount):
        '''출금 메서드'''
        if self.balance >= amount:
            self.balance -= amount
            print(f'{amount}원이 출금되었습니다. 잔액: {self.balance}원')
        else:
            print('잔액이 부족합니다.')

    def apply_interest(self):
        '''이자 적용'''
        interest = self.balance * BannkAccount.interest_rate
        self.balance += interest
        print(f'이자 {interest}원이 적용되었습니다. 잔액: {self.balance}원')

    @classmethod # 함수 바로 위에 적어야 함
    def change_interest_rate(cls, new_rate):
        '''클래스 메서드: 이자율 변경'''
        cls.interest_rate = new_rate
        print(f'이자율 {new_rate * 100}%로 변경되었습니다.')


    def __del__(self):
        # 클래스 변수 업데이트
        BannkAccount.total_accounts -= 1
        print(f'{self.owner}님 계좌를 삭제했습니다')
        print(f'남은 계좌 수: {BannkAccount.total_accounts}')


# 객체 생성
account1 = BannkAccount('홍길동', 10000)
account2 = BannkAccount('김철수', 15000)

print(f'은행 이름:{BannkAccount.bank_name}')
print()
print(f'총 계좌 수:{BannkAccount.total_accounts}')

account1.deposit(50000) # 입금
print()

account2.apply_interest() # 이자 적용
print()

BannkAccount.change_interest_rate(0.03) # 이자 변경
print()

account1.apply_interest() # 이자 적용
print()

del account1
# 프로그램이 종료될 때 모든 객체 삭제됨

class Calculator:
    # 클래스 변수
    calculation_count = 0
    
    def __init__(self, name):
        self.name = name
        self.history = []

    # 인스턴스 메서드
    def add_to_history(self, operation, result):
        '''계산 기록 저장'''
        self.history.append(f'{operation} = {result}')
        Calculator.calculation_count += 1

    # 클래스 메서드
    @classmethod
    def get_total_calculations(cls):
        '''전체 계산 횟수 반환'''
        return cls.calculation_count
    
    @staticmethod
    def add(a, b):
        '''두 수의 합'''
        return a + b
    
    @staticmethod
    def multiply(a, b):
        '''두 수의 곱'''
        return a * b
    
    @staticmethod
    def is_even(number): # is 들어가는 건 대부분 결과 불리언으로 리턴됨
        '''짝수 판별'''
        return number % 2 == 0
    
    def calculate_and_save(self, a, b, operation):
        '''계산하고 기록 저장'''
        if operation == 'add':
            result = self.add(a,b)
            self.add_to_history(f'{a} + {b}', result)
        elif operation == 'multiply':
            result = self.multiply(a,b)
            self.add_to_history(f'{a} X {b}', result)
        return result


# 객체 생성
calc1 = Calculator('계산기1')
calc2 = Calculator('계산기2')
print()

# 정적 메서드 사용(인스턴스 없이도 호출 가능)
print(Calculator.add(5, 3))
print(Calculator.is_even(5))
print()

# 인스턴스 메서드 사용
result = calc1.calculate_and_save(10, 20, 'add')
print(f'결과: {result}')
print()

# 클래스 메서드 사용
print(f'총 계산 횟수: {Calculator.get_total_calculations()}')
print()
