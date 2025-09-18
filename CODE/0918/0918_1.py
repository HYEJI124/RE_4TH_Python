# 함수(Function)

# 함수는 특정 작업을 수행하는 코드의 묶음
# 한 번 정의하면 필요할 때마다 호출하여 재사용 가능

# 함수를 사용하는 이유

# 코드 재사용성: 같은 코드를 반복 작성할 필요 없음
# 모듈화: 프로그램을 작은 단위로 나누어 관리
# 가독성 향상: 코드의 의도를 명확히 표현
# 유지보수 용이: 수정이 필요할 때 함수만 변경
# 추상화: 복잡한 로직을 단순한 인터페이스로 제공

print('=' * 20)
print('첫 번째 섹션')
print('=' * 20)

print('=' * 20)
print('두 번째 섹션')
print('=' * 20)

# 함수 사용 - 코드 재사용

def print_section(title):
    print('=' * 20)
    print(f' {title} 섹션')
    print('=' * 20)

print_section('첫 번째')
print_section('두 번째')

# 함수 정의와 호출
# 함수 정의(Definition)
def 함수이름(매개변수):
    # 실행 코드
    return #반환값

# 함수 호출(Call)
# 결과 = 함수인자(이름)

def say_hello():
    print('안녕하세요')

say_hello()

def greet(name):
    print(f'안녕하세요 {name}님!')

greet('김철수')
greet('이영희')
print("greet('이영희')", greet('이영희'))

def add(a, b):
    result = a + b
    return result

sum_result = add(3, 5)
print('sum_result', sum_result)
print('add(10, 5)', add(10, 5))

# 사각형 넓이
def calculate_area(width, height):
    # 문서화 문자열(Docsting)
    '''
    직사각형의 넓이를 계산합니다.

    Parameters:
    width (float): 직사각형의 너비
    height(float): 직사각형의 높이

    Return:
      float: 직사각형의 넓이
    '''
    return width * height

print(calculate_area(10, 20))

# Dpcsting 확인
# print(calculate_area.__doc__)
# help(calculate_area)

def greet(name, message="안녕!"):
    print(f'{name} {message}')


greet('ethan')
greet('김철수', '안녕하세요!')

def add(a, b, c=15, d=10):
    print('a', a)
    print('b', b)
    print('c', c)
    print('d', d)

add(1, 2, d=12)

def add_all(*new_tuple):
    return sum(new_tuple)

result = add_all(1, 2, 3, 4, 5)
print('result', result)

def print_info(**new_dict):
    for key, value in new_dict.items():
        print(f'{key} {value}')

print_info(name = '홍길동', age = 25, city = '서울')

# 매개변수와 인자
# 매개변수(Parameter): 함수 정의 시 사용하는 변수
# 인자(Argument): 함수 호출 시 전달하는 실제 값

def multiply(x, y): # x, y는 매개변수
    return x * y

result = multiply(3, 5) # 3, 5는 인자

# 위치 인자(Positinal Arguments)
def introduce(name, age, city):
    print(f'{name} {age} {city}')

# name = 김철수, age = 25, city = 서울
introduce('김철수', 25, '서울')

# 키워드 인자(Keyword Arguments)
def introduce(name, age, city):
    print(f'{name} {age} {city}')

# 순서와 상관없이 이름을 전달
introduce(city = '서울', age = 25, name = '김철수')


def introduce(name, age, city):
    print(f'{name} {age} {city}')

# 위치 인자, 키워드 혼용
introduce('김철수', city = '서울', age = 25)
# 주의: 위치 인자는 키워드 인자보다 앞에 와야함!

# introduce(20, city = '부산', name = '이영희') # 혼용 불가

# 반환값(return)
# 단일 값 반환
def square(n):
    return n ** 2

result = square(5)
print(result) # 25

# 여러 값 반환
def calculate_stats(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    max_num = max(numbers)
    min_num = min(numbers)

    return total, avg, max_num, min_num

numbers = [100, 140, 230, 200] # list
total, avg, max_num, min_num = calculate_stats(numbers)

print('total:', total)
print('avg:', avg)
print('max_num:', max_num)
print('min_num:', min_num)

stats = calculate_stats(numbers)
print(stats) # (670, 167.5, 230, 100)

# return의 특징
def check_positive(number):
    if number > 0:
        return '양수'
    elif number < 0:
        return '음수'
    else:
        return '0'
    print('코드가 실행이 될까요???')

# return: 함수를 종료시킴(break(반복을 종료시킴)와 비슷)

print(check_positive(4))
print(check_positive(-1))
print(check_positive(0))

# 조기 반환(Early Return)

def divide(a, b):
    # 예외 상황을 먼저 처리
    if b == 0:
        return '0으로 나눌 수 없습니다.'
    
    return a / b

print(divide(10, 2))
print(divide(10, 0))

# 기본값 매개변수
def greet(name, greeting = '안녕하세요'):
    print(f'{greeting}, {name} 님')

greet('김철수') # 출력: 안녕하세요, 김철수 님
greet('이영희', '반갑습니다') # 출력: 반갑습니다, 이영희 님

# 여러 기본값
def create_profile(name, age=25, city='서울', job='개발자'):
    return {'name' : name,
            'age' : age,
            'city' : city,
            'job': job
            }
    
print(create_profile('박민수'))
# {'name': '박민수', 'age': 25, 'city': '서울', 'job': '개발자'}
print(create_profile('김철수', 30))
# {'name': '김철수', 'age': 30, 'city': '서울', 'job': '개발자'}
print(create_profile('이영희', job='모델'))
# {'name': '이영희', 'age': 25, 'city': '서울', 'job': '모델'}

# 가변 위치 인자(*args)
def sum_all(*numbers):
    print(type(numbers)) # <class 'tuple'>
    print(numbers) # (1, 2, 3) (1, 2, 3, 4, 5, 6, 7, 8) ()
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5, 6, 7, 8))
print(sum_all()) # 인자가 없어도 됨

# 가변 키워드 인자(**Kwargs)

def print_info(**user):
    # 키워드 인자를 딕셔너리로 받음
    print(type(user))
    print('user', user)
    for key, value in user.items():
        print(f'{key} {value}')

print_info(name='김철수', age=20, city='서울')
# 출력
# name: 김철수
# age: 20
# city: 서울

def create_student(**info):
    '''
       학생 정보를 생성합니다.
    '''
    student = {
        'name': info.get('name', '이름없음'), # get을 지워도 아래 name key 값 있으니까 에러 발생 안함
        'age': info.get('age'), # get을 지우면 key가 없으면 에러 발생
        'grade': info.get('grade', 1),
        'subjects': info.get('subjects', [])
    }
    return student

student1 = create_student(name='김철수', subjects=['python'])
print(student1)
# {'name': '김철수', 'age': 20, 'grade': 1, 'subjects': []}
# {'name': '김철수', 'age': 20, 'grade': 1, 'subjects': ['python']}
