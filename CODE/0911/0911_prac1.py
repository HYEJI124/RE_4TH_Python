# 실습 1. 날씨에 따른 준비물 안내

weather = input("오늘 날씨를 입력하세요(비/맑음): ")

if weather == "비":
    print("우산을 챙기세요!")
if weather == "맑음":
    print("선크림을 바르세요!")

# 실습 2. 짝수 홀수 판별하기

number = int(input("정수를 입력해주세요: "))

if (number % 2) == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

num = int(input("정수를 입력해주세요: "))

if num % 2:
    print("홀수입니다.")
else:
    print("짝수입니다.")
          
# 실습 3. 나이에 따른 영화 관람 가능 여부

age = int(input("나이를 입력하세요: "))

if age >= 19:
    print("청소년 관람불가 가능")
elif  16 <= age <= 18:
    print("15세 이상 관람가")
elif  13 <= age <= 15:
    print("12세 이상 관람가")
else:
    print("전체 관람가")

if age >= 19:
    print("청소년 관람불가 가능")
elif age >= 16:
    print("15세 이상 관람가")
elif age >= 13:
    print("12세 이상 관람가")
else:
    print("전체 관람가")

# 실습 4. 시, 분, 초 구하기
second = int(input("초를 입력해주세요"))

# 시간을 구하는 식 (60초 * 60분): 1시간
if second >= 3600:
    print(f"{second // 3600} 시", end=' ')

# 분을 구하는 식 (60초)
second %= 3600

if second >= 60:
    print(f"{second // 60} 분", end=' ')

second %= 60
print(f"{second} 초")

# 실습 5. 편의점 도시락 구매하기

김밥 = 2500
삼각김밥 = 1500
도시락 = 4000

price = int(input("금액을 입력하세요: "))
foodname = input("식품명을 입력하세요(김밥, 삼각김밥, 도시락): ")

if foodname == "도시락":
    if price >= 도시락:
        print("구매 성공")
    else:
        print("금액이 부족합니다.")
elif foodname == "김밥":
    if price >= 김밥:
        print("구매 성공")
    else:
        print("금액이 부족합니다.")
elif foodname == "삼각김밥":
    if price >= 삼각김밥:
        print("구매 성공")
    else:
        print("금액이 부족합니다.")

price_kimbab = 2500
price_samgak = 1500
price_dosirak = 4000

money = int(input("금액을 입력하세요: "))
food = input("식품명을 입력하세요(김밥, 삼각김밥, 도시락): ")

if food == "김밥":
    if money >= price_kimbab:
            print("구매 성공")
    else:
        print("금액이 부족합니다.")
elif food == "삼각김밥":
    if money >= price_samgak:
        print("구매 성공")
    else:
        print("금액이 부족합니다.")
elif food == "도시락":
    if money >= price_dosirak:
        print("구매 성공")
    else:
        print("금액이 부족합니다.")
else:
    print("잘못된 메뉴입니다.")

