# 실습4. 상속과 오버라이딩 연습
# 문제 1. Shape 클래스 오버라이딩
# [Shape 클래스 조건]
# ▪ 생성자를 통해 다음 두 값을 초기화하세요:
# • 변의 개수 (sides)
# • 밑변의 길이 (base)
# ▪ printInfo() 메서드를 정의하여 다음과 같이 출력:
# • 변의 개수: 4
# • 밑변의 길이: 10
# ▪ area() 메서드를 정의하여 "넓이 계산이 정의되지 않았습니다."라는 메시지를 출력
# → 자식 클래스에서 이 메서드를 오버라이딩해야 합니다.
# [Rectangle 클래스 조건]
# ▪ Shape를 상속받습니다.
# ▪ 생성자에서 sides, base, height를 모두 초기화합니다.
# ▪ area() 메서드를 오버라이딩하여 base * height 값을 출력합니다.
# [Triangle 클래스 조건]
# ▪ Shape를 상속받습니다.
# ▪ 생성자에서 sides, base, height를 모두 초기화합니다.
# ▪ area() 메서드를 오버라이딩하여 (base * height) / 2 값을 출력합니다.
# [실행]
# ▪ Rectangle과 Triangle 객체를 생성합니다.
# ▪ 각 객체에 대해 printInfo()와 area() 메서드를 차례로 호출하세요.

class Shape:
    def __init__(self, sides, base):
        self.sides = sides
        self.base = base

    def printInfo(self):
        print(f'변의 개수:{self.sides}, 밑변의 길이:{self.base}')
    
    def area(self):
        print('넓이 계산이 정의되지 않았습니다.')

class Rectangle(Shape):
    def __init__(self, sides, base, height):
        super().__init__(sides, base)
        self.height = height


    def area(self):
        print(f'area: {self.base} X {self.height} = {self.base * self.height}')

class Triangle(Shape):
    def __init__(self, sides, base, height):
        super().__init__(sides, base)
        self.height = height

    def area(self):
        print(f'area: ({self.base} X {self.height}) / 2 = {self.base * self.height / 2}')
        
shapes = [Rectangle(5, 3, 7), Triangle(4, 6, 8)]
for shape in shapes:
    shape.printInfo()
    shape.area()


# 리더님 방식
class Shape:
    def __init__(self, sides, base):
        '''
        변의 개수 (sides)
        밑변의 길이 (base)
        '''
        self.sides = sides
        self.base = base

    def printInfo(self):
        print(f'변의 개수: {self.sides}')
        print(f'밑변의 길이: {self.base}')


    def area(self):
        print(f'넓이 계산이 적용되지 않습니다.')

class Triangle(Shape):
    '''
        생성자에서 sides, base, height를 모두 초기화합니다.
        area() 메서드를 오버라이딩하여 (base * height) / 2 값을 출력합니다.
    '''
    def __init__(self, sides, base, height):
        super().__init__(sides, base)
        self.height = height

    def area(self):
        print(f'넓이: {self.base * self.height / 2}')
        
class Rectangle(Shape):
    '''
        생성자에서 sides, base, height를 모두 초기화합니다.
        area() 메서드를 오버라이딩하여 base * height 값을 출력합니다.
    '''
    def __init__(self, sides, base, height):
        super().__init__(sides, base)
        self.height = height
        print('삼각형 생성')

    def area(self):
        print(f'넓이: {self.base * self.height}')
        print('사각형 생성')

print()
rect = Rectangle(4, 10, 5)
tri = Triangle(3, 10, 5)

rect.area()
print()
tri.area()

# 실습5. 추상 클래스 연습 문제
# 문제. 추상 클래스 Payment 구현
# 아래 조건을 만족하는 클래스를 구현하세요.
# ▪ 추상 클래스 Payment를 정의하고, pay(amount)를 추상 메서드로 선언하세요. (abc 모듈 사용)
# ▪ CardPayment 클래스와 CashPayment 클래스는 Payment를 상속받아 pay() 메서드를 오버라이딩하세요.
# • CardPayment: 카드로 {amount}원을 결제합니다. 출력
# • CashPayment: 현금으로 {amount}원을 결제합니다. 출력

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CardPayment(Payment):
    def pay(self, amount):
        self.amount= amount
        print(f'카드로 {self.amount}원을 결제합니다.')

class CashPayment(Payment):
    def pay(self, amount):
        self.amount= amount
        print(f'현금으로 {self.amount}원을 결제합니다.')

print()
card = CardPayment()
card.pay(50000)
print()
cash = CashPayment()
cash.pay(50000)
print()

# 리더님 방법
from abc import ABC, abstractmethod

class PAyment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CardPayment(Payment):
    def pay(self, amount):
        print(f'카드로 {amount}원을 결제합니다.')


class CashPayment(Payment):
    def pay(self, amount):
        print(f'현금으로 {amount}원을 결제합니다.')

card_pay = CardPayment()
card_pay.pay(10000)
print()
cash_pay = CashPayment()
cash_pay.pay(20000)
