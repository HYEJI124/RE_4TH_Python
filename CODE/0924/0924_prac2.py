# 문제 1: 나이 입력 프로그램
# 사용자로부터 나이를 입력받아 연령대를 출력하는 프로그램을 작성하세요.
# • 숫자가 아니면 다시 입력 요청
# • 음수나 150 초과는 오류 메시지
# • 정상 입력 시 연령대 출력 (미성년자/청년/중년/노년)

print('=========문제1=========')
def get_age_group():
    """나이를 입력받아 연령대 반환"""
    # 여기에 코드 작성
    try:
        age = int(input('나이를 입력하세요: '))
    except ValueError:
        print('숫자로 다시 입력하세요: ')
        age = int(input('나이를 입력하세요: '))
    except IndexError:
        if age < 0 or age > 150:
            print('나이를 잘못 입력하셨습니다.')
    if 0 < age <= 19:
        print('미성년자')
    elif 19 < age < 35:
        print('청년')
    elif 35 <= age < 60:
        print('중년')
    elif 60 <= age < 150:
        print('노년')
    else:
        print('정상 나이 범주 벗어남')
print()

# 테스트
get_age_group()

# 문제 2:리스트 안전 접근
# 리스트의 특정 인덱스 값을 안전하게 가져오는 함수를 작성하세요.

print('=========문제2=========')
def safe_get(lst, index, default=None):
    """
    리스트에서 안전하게 값 가져오기
    - lst: 리스트
    - index: 인덱스
    - default: 기본값
    """
    # 여기에 코드 작성
    try:
        return lst[index]
    except IndexError:
        return default


# 테스트
numbers = [10, 20, 30]
print(safe_get(numbers, 1))      # 20
print(safe_get(numbers, 10))     # None
print(safe_get(numbers, 10, -1)) # -1
print()