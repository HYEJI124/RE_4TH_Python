# 실습 1. 딕셔너리 종합 연습 문제
# 문제 1. 딕셔너리 핵심 개념 통합 실습
# 1. user라는 이름의 빈 딕셔너리 생성
# user = {}
user = dict()

# 2. 사용자 기본 정보 추가
user['username'] = 'skywaler'
user['email'] = 'sky@example.com'
user['level'] = 5
print('user', user)

# user = {
#     'username' : 'skywalker',
#     'email' : 'sky@example.com',
#     'level' : 5
# }
# print('user', user)

# 3. 값 읽기
email_value = user['email']
print('email_value:', email_value)

# 4. 값 수정
user['level'] = 6
print('user', user)

# 5. 안전하게 키 조회
print(user.get('phone', '미입력'))

# 6. 항목 추가 및 삭제
user.update({'nickname' : 'sky'})
print('user', user)

# 7. 이메일 항목 삭제
del user['email']
print('user', user)

# 값 추가
print(user.setdefault('signup_date', '2025-07-10'))

# 최종 딕셔너리 출력
print('user', user)


# 문제 2. 학생 점수 관리
# 1. 빈 딕셔너리 생성
students = {}
# 2. 값 추가
names = ['Alice', 'Bob', 'Charlie']
score = [85, 90, 95]

students = dict(zip(names, score))

# students = {'Alice' : 85, 'Bob' : 90, 'Charlie' : 95}

# 3. 값 추가
students.update({'David' : 80})
# students['David'] = 80

# 4. 값 수정
students['Alice'] = 88

# 5. 값 삭제
del students['Bob']

# 6. 최종 딕셔너리 출력
print('students', students)
