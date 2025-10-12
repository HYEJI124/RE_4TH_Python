# 실습2. DataFrame 연습
import pandas as pd

# 1. 다음 데이터로 DataFrame을 생성하고, 컬럼명을 '이름', '나이', '도시'로 지정하세요.
person = pd.DataFrame([['홍길동', 28, '서울'], ['김철수', 33, '부산'], ['이영희', 25, '대구']]
                     , columns=['이름', '나이', '도시'])
print('문제 1')
print(person)
print()

# 2. 아래와 같은 딕셔너리로 DataFrame을 생성하세요.
num = {'A': [1, 2, 3], 'B': [4, 5, 6]}
data = pd.DataFrame(num)
print('문제 2')
print(data)
print()

# 3. 아래 데이터를 사용해 DataFrame을 만드세요.
exam = [{'과목': '수학', '점수': 90}, {'과목': '영어', '점수': 85}, {'과목': '과학', '점수': 95}]
data = pd.DataFrame(exam)
print('문제 3')
print(data)
print()

# 4. 아래 데이터를 사용해 DataFrame을 생성하되, 인덱스를 ['학생1', '학생2', '학생3']으로 지정하세요.
student = {'이름': ['민수', '영희', '철수'], '점수': [80, 92, 77]}
data = pd.DataFrame(student, index=['학생1', '학생2', '학생3'])
print('문제 4')
print(data)
print()

# 5. 아래 Series 객체 2개를 이용해 DataFrame을 만드세요.
kor = pd.Series([90, 85, 80], index=['a', 'b', 'c'])
eng = pd.Series([95, 88, 82], index=['a', 'b', 'c'])
data = pd.DataFrame({'kor': kor, 'eng': eng})
print('문제 5')
print(data)
print()

# 6. 아래 딕셔너리로 DataFrame을 만들고, 컬럼 순서를 ['B', 'A']로 지정해 출력하세요.
num = {'A': [1, 2], 'B': [3, 4]}
data = pd.DataFrame(num, columns=['B', 'A'])
print('문제 6')
print(data)
print()

# 7. 데이터를 DataFrame으로 만들고, 컬럼명을 ['product', 'price', 'stock']으로 변경하세요.
item = [['펜', 1000, 50], ['노트', 2000, 30]]
data = pd.DataFrame(item, columns=['product', 'price', 'stock'])
print('문제 7')
print(data)
print()

# 8. 아래 DataFrame을 생성한 뒤, '국가' 컬럼만 추출하세요.
nations = {'국가': ['한국', '일본', '미국'], '수도': ['서울', '도쿄', '워싱턴']}
data = pd.DataFrame(nations)
print('문제 8')
print(nations['국가'])
print()
