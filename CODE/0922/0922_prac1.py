# 실습1. class 기본 문법 연습
# 문제1. 책 클래스 만들기
# Book 클래스를 정의하세요.
# 인스턴스 변수로 title, author, total_pages, current_page를 가집니다.
# 메서드:
# • read_page(pages): 현재 페이지를 읽음. 총 페이지 수를 넘지 않도록 처리.
# • progress(): 전체에서 얼마나 읽었는지를 퍼센트(%)로 소수점 1자리까지 출력

class Book:
    def __init__(self, title, author, total_pages):
        # 변수로 title, author, total_pages, current_page
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_pages = 0
        
    def read_page(self, pages):
        # 현재 페이지를 읽음. 총 페이지 수를 넘지 않도록 처리.
        if pages < 0:
            return
        
        self.current_page = min(self.total_pages, self.current_pages + pages)

    def progress(self):
        # 전체에서 얼마나 읽었는지를 퍼센트(%)로 소수점 1자리까지 출력
        pct = (self.current_page / self.total_pages) * 100
        return round(pct, 1) # 소수점 1자리까지 출력
    
    def __repr__(self):
        return f"<Book {self.title} by {self.author}"

# 객체 생성
b = Book('파이썬 클린코드', '홍길동', total_pages=320)
b.read_page(100)
print('책 정보')
print(b)
print(b.progress(), '%')
print()
b.read_page(1000)
print()
print(b.progress(), '%')
print()

# 실습1. class 기본 문법 연습
# 문제2. Rectangle 클래스 구현
# 다음 조건에 맞는 Rectangle 클래스를 작성해 보세요.
# 인스턴스 변수: width, height
# 메서드:
# • area() : 사각형의 넓이 반환
# 사용자 입력:
# • 프로그램 실행 시 사용자로부터 가로(width)와 세로(height) 값을 입력 받아 객체를 생성하고 area() 메서드를 호출하여 넓이를 출력

class Rectangle:
    # 생성자!!
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        ''' 사각형의 넓이 반환'''
        return self.width * self.height

w = int(input('가로(width)를 입력하세요:'))
h = int(input('세로(height)를 입력하세요:'))

rect = Rectangle(w, h)
print('사각형의 넓이:', rect.area())
   
# rect = Rectangle(10, 20)
# print('사각형의 넓이:', rect.area())

# 실습2. 클래스 변수, 메서드 연습
# 문제1. User 클래스 구현
# User 클래스를 정의하세요.
# 인스턴스 변수: username, points (초기값은 0)
# 클래스 변수: total_users (생성된 유저 수 저장)
# 메서드:
# • add_points(amount): 포인트 추가
# • get_level(): 포인트 기준으로 레벨 반환
# • 0~99: Bronze, 100~499: Silver, 500 이상: Gold
# • 클래스 메서드: get_total_users() → 총 유저 수 출력

class User:
    total_users = 0

    def __init__(self, username):
        self.username = username
        self.points = 0

        # total_users는 생성될 때마다 추가됨 -> 클래스 변수 업데이트
        User.total_users += 1

    def add_points(self, amount):
        # 포인트 추가
        if amount > 0:
            self.points += amount

    def get_level(self):
        # 포인트 기준으로 레벨 반환
        if 0 <= self.points < 100:
            return 'Bronze'
        elif 100 <= self.points < 500:
            return 'Silver'
        elif 500 <= self.points:
            return 'Gold'
        
    @classmethod
    def get_total_users(cls):
        print(f'총 유저 수: {cls.total_users}')

    def __del__(self):
        User.total_users -= 1

user1 = User('홍길동')
user2 = User('이영희')
user3 = User('김철수')

User.get_total_users() # 3

del user2

User.get_total_users() # 3 -> 삭제된다고 값 내려가지 않음(삭제하려면 del 써야 함)



