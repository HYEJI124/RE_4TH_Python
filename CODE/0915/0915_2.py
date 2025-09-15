# Set
# 중복되지 않는 요소들의 순서가 없는 집합
# 수학의 집합 개념을 구현한 자료구조
# 해시 테이블 기반으로 빠른 멤버십 테스트 가능

# 왜 Set이 필요한가?
# 중복 제거가 필요한 경우
visitors = ['철수', '영희', '철수', '민수', '영희', '철수']

# 리스트로 중복 제거(비효율적) O(n) 검색
unique_visitors_list = []
for visitor in visitors:
    if visitor not in unique_visitors_list:
        unique_visitors_list.append(visitor)
print(unique_visitors_list)

# Set으로 중복 제거(효율적) O(1) 검색
unique_visitors_set = set(visitors)
print(unique_visitors_set)

# 특징
# 1. 순서 없음: 요소들의 순서가 보장되지 않음
# 2. 중복 불가: 같은 값은 하나만 저장
# 3. 변경 가능: 요소 추가 / 삭제 가능
# 4. 인덱싱 불가: 순서가 없어 인덱스로 접근 불가능
# 5. 빠른 검색 O(1) 시간 복잡도로 요소 확인

# Set 생성 방법
# 1. 빈 set 생성
# empty_set = {} # 이것은 딕셔너리!!
empty_set = set()

# 2. 값이 있는 set 생성
numbers = {1, 2, 3, 5, 4, 3, 2, 4}
fruits = {'사과', '바나나', '오렌지'}

# 3. 리스트 / 튜플에서 set 생성
list_numbers = [11, 2, 13, 5, 4, 3, 2, 4]
set_numbers = set(list_numbers)
print(set_numbers)

# 4. 문자열에서 set 생성
chars = set('hello')
print(chars)

# Comprehension
for i in range(10):
    print(i)

com_set = {i for i in range(10)}
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

com_set1 = {i * 2 for i in range(10)}
# {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}

com_set2 = {(i ** 2 + 1) for i in range(10)}
# {1, 2, 5, 10, 17, ... , 82}

com_set3 = {i * 3 + 2 - 1 for i in range(10)}
# {1, 4, 7, 10, 13, ... , 28}

com_set4 = set()
for i in range(10):
    com_set4.add((i * 3 + 2 - 1))

com_list = [i for i in range(2, 10, 2)]
# [2, 4, 6, 8]

# set에 저장 가능한 데이터 타입
# Hashable 타입만 가능(불변 타입)
valid_set = {1, "문자열", (1,2), 3.14, True}

# # Unhashable 타입 불가능(가변 타입) - 리스트, 딕셔너리, 세트
# invalid_set = {[1, 2], {'key': 'value'}, {1, 2}}

# 중첩 set을 만들려면 frozenset() 사용
nested_set = {frozenset([1,2]), frozenset([3, 4])}
print(nested_set)

# set 메서드
colors = {"빨강", "노랑", "파랑"}

colors.add("초록")
print(colors)

colors.add("초록")
print(colors)

colors.update(['보라', '주황'])
print(colors)

colors.update(['검정'], {'하양', '회색'})
print(colors)

colors.remove('검정')
print(colors)

# colors.remove('검정')
# print(colors)

colors.discard('검정')
print(colors)

colors.discard('주황')
print(colors)

popped = colors.pop()
print(popped)
print(colors)

colors.clear()
print(colors)

# 집합 연산
A = {1, 2, 3, 4, 5}
B = {1, 2, 6, 7, 8}

# 교집합 - 공통 요소
intersection1 = A & B
intersection2 = A.intersection(B)

print('intersection1', intersection1)
print('intersection2', intersection2)

# 합집합 - 모든 요소
union1 = A | B
union2 = A.union(B)

print('union1', union1)
print('union2', union2)

# 차집합(Difference) - 기준 집합에만 있는 요소
difference1 = A - B
difference2 = A.difference(B)

print('difference1', difference1)
print('difference2', difference2)

# 대칭 차집합(Symmetric Difference) - 공통 요소 제외한 나머지 요소
sym_diff1 = A ^ B
sym_diff2 = A.symmetric_difference(B)

print('sym_diff1', sym_diff1)
print('sym_diff2', sym_diff2)

A = {1, 2, 3}
B = {3, 4, 5}

# A를 교집합으로 업데이트
A.intersection_update(B)
A &= B
print("A", A)

A = {1, 2, 3}
# 차집합으로 업데이트
A.difference_update(B) # {1, 2}
A -= B
print("A", A)

A = {1, 2, 3}
# 대칭차집합으로 업데이트
A.symmetric_difference_update(B) # {1, 2, 4, 5}
A ^= B
print("A", A)

A = {1, 2, 3}
# 합집합으로 업데이트
A.update(B) # {1, 2, 3, 4, 5}
A |= B
print("A", A)

# 집합 관계 확인
# 부분집합, 상위집합

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {6, 7, 8}

# 부분집합인지 확인
print(A.issubset(B)) # True
print(A <= B) # True

print(B.issubset(A)) # False

# 상위집합인지 확인
print(A.issuperset(B)) # False

print(B.issuperset(A)) # True
print(A <= B) # True
print(B >= A) # True

# 진부분집합 확인
# A == B이면 False
print(B > A)
print(B < A)

# 서로수 집합
# 교집합이 없는지 확인
print(A.isdisjoint(C))

# frozenset() (불변집합)
fs1 = frozenset([1, 2, 3, 3, 4])

# 불변이므로 수정, 삭제, 추가 불가
# fs1.add(5)
# fs1.remove()
# fs1.discard()

