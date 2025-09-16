# 실습 1. set 종합 연습
# 문제 1. 중복 제거 및 개수 세기

submissions = ['kim', 'lee', 'kim', 'park', 'choi', 'lee', 'lee']
sub = set(submissions)
print(f"제출한 학생 수: {len(sub)}")
print(f"제출자 명단: {sub}")

# 문제 2. 공통 관심사 찾기

user1 = {'SF', 'Action', 'Drama'}
user2 = {'Drama', 'Romance', 'Action'}

# 교집합
print(f'공통 관심 장르: {user1.intersection(user2)}') # user1 & user2
# 대칭차집합
print(f'서로 다른 장르: {user1.symmetric_difference(user2)}') # user1 ^ user2
# 합집합
print(f'전체 장르: {user1.union(user2)}') # user1 | user2

# 문제 3. 부분집합 관계 판단

my_certificates = {'SQL', 'Python', 'Linux'}
job_required = {'SQL', 'Python'}

print(f"지원 자격 충족 여부: {my_certificates.issuperset(job_required)}") # my_certificates >= job_required