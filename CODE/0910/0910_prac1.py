# 실습 1-1. 영화정보 출력하기
"""
영화 정보를 변수로 만들어 한 번에 출력해보세요.
출력 문장 형식에 맞게 f-string을 사용하고, 1줄로 작성하세요.
변수: 영화이름(title), 감독(director), 개봉년도(year), 장르(genre)
"""

title = "Inception"
director = "Christopher Nolan"
year = 2010
genre = "Sci-Fi"

print(f'Title: {title} Director: {director} Year: {year} Genre: {genre}')


# 실습 1-2. 자기소개 하기
"""
f-string을 사용해서 자기소개를 하세요.
print를 '한 번만 사용'해서, 여러 줄의 문장이 아래와 같이 출력되도록 합시다.
변수: 이름, 나이, MBTI
"""

name = "박혜지"
age = 23
MBTI = "ESTP"

# 나
print(f"안녕하세요.\n제 이름은 {name}이고,\n{age}살 입니다.\n제 MBTI는 {MBTI}에요.")

# 리더님
print(f"""안녕하세요
제 이름은 {name}
{age} 살
제 MBTI는 {MBTI} 에요.
""")

# 실습 2-1. 대학생의 용돈 관리
"""
1. 시작 용돈은 30만원 입니다.
2. 개강 첫 주에 책을 사느라 8만원을 썼습니다.
3. 평일 점심값으로 매일 9천원씩 5일간 사용했습니다.
4. 과외 아르바이트를 하며 12만원을 벌었습니다.
5. 부모님이 용돈을 더 주셔서 현재 금액의 20%를 추가로 받았습니다.
6. 하지만 전기요금 등 공과금으로 남은 돈의 1/3이 빠져나갔습니다.
"""

# 나
money = 300000 # 시작 용돈
print(money)

money -= 80000 # 책값: 8만원 사용
print(money)

money -= (9000 * 5) # 평일 점심값: 9천원씩 5일 사용
print(money)

money += 120000 # 과외: 12만원 벎
print(money)

money *= 1.2 # 추가 용돈: 현재 금액의 20%
print(money)

money *= (1-1/3) # 공과금 1/3 빠져 나가고 남은 돈
print(money)
# 리더님: money -= money / 3

print("남은 용돈은", int(money),"원 입니다.")



# 실습 2-2. EDM 리듬 트랙 만들기
"""
1. 아래는 EDM 리듬을 표현한 단어들입니다.

intro = "둠칫"
drop = "두둠칫"

2. +, * 연산자만 사용해서 아래와 같이 출력해주세요.
둠칫두둠칫두둠칫두둠칫
"""

intro = "둠칫"
drop = "두둠칫"
print(intro + drop * 3)



# 실습 2-3. input 연습하기

name = input("이름을 입력하세요: ")
age = input("나이를 입력하세요: ")
print(f"안녕하세요. 저는 {name}이고, {age}살입니다.")

name, age = input('이름과 나이를 입력하세요: ').split()
print(f'안녕하세요. 저는 {name} 이고, {age}살 입니다.')


# 실습 2-4. 입력과 연산 연습하기
# 1. 사용자로부터 가로와 세로를 입력 받아 넓이와 둘레를 계산하세요.

width = int(input("가로 길이를 입력하세요: "))
length = int(input("세로 길이를 입력하세요: "))

area = width * length
perimeter = 2 * (width + length)

print(f"넓이:{area} \n둘레:{perimeter}")

width = int(input("가로 길이를 입력하세요: "))
height = int(input("세로 길이를 입력하세요: "))
print(f'넓이: {width * height}')
print(f'둘레: {(width + height) * 2}')

# 2. 네 자릿수 정수를 입력 받고, 각 자리수를 분리하여 출력하세요.

number = int(input("네 자릿수 정수를 입력하세요: "))

천의자리 = number // 1000
백의자리 = (number % 1000) // 100
십의자리 = (number % 100)  // 10
일의자리 = number % 10

print(f"""천의 자리:{천의자리}
백의 자리:{백의자리}
십의 자리:{십의자리}
일의 자리:{일의자리}""")

num = int(input("네 자릿수 정수를 입력하세요: "))
print(f'천의 자리: {num // 1000}')
num %= 1000
print(f'백의 자리: {num // 100}')
num %= 100
print(f'십의 자리: {num // 10}')
num %= 10
print(f'일의 자리: {num // 1}')

# 실습 2-5. 발표 순서와 발표 주제 정하기

name1, name2, name3 = input("이름을 입력하세요: ").split()
subject1, subject2, subject3 = input("주제를 입력하세요: ").split()
print(f"""발표 순서 안내입니다.

1조 발표자: {name1} - 주제: {subject1}
2조 발표자: {name2} - 주제: {subject2}
3조 발표자: {name3} - 주제: {subject3}
""")

name1, name2, name3 = input().split()
topic1, topic2, topic3 = input().split()

print(f'1조 발표자: {name1} - 주제: {topic1}')
print(f'2조 발표자: {name2} - 주제: {topic2}')
print(f'3조 발표자: {name3} - 주제: {topic3}')

# 실습 2-6. 날짜와 시간
year, month, day = input("년, 월, 일을 입력하세요(.으로 구분): ").split('.')
hour, minute, second = input("시, 분, 초를 입력하세요(:으로 구분): ").split(':')

print(f"""RE3의 개강일은 {year}년 {month}월 {day}일
시작 시간은 {hour}시 {minute}분 {second}초입니다.""")

year, month, day = input().split('.')
hour, minute, second = input().split(':')

print(f'RE4의 개강일은 {year}년 {month}월 {day}일')
print(f'시작 시간은 {hour}시 {minute}분 {second}초입니다.')

