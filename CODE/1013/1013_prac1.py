import pandas as pd

# 다음 데이터를 CSV로 저장하고 다시 읽어오세요
# 1. 'practice.csv'로 저장 (인덱스 제외)
# 2. 저장한 파일 읽어오기
# 3. 읽어온 데이터 출력

practice_data = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['Seoul', 'Busan', 'Daegu']
})

practice_data.to_csv('practice.csv', index=False)

df_practice = pd.read_csv('practice.csv')
print('==== practice.csv 파일 읽어오기 ====')
print(df_practice)
print()

# 한글 데이터를 UTF-8로 저장하고 읽어오세요
# 1. UTF-8 인코딩으로 저장
# 2. 같은 인코딩으로 읽어오기
# 3. 한글이 깨지지 않았는지 확인

korean_data = pd.DataFrame({
    '이름': ['김철수', '이영희', '박민수'],
    '직급': ['사원', '대리', '과장']
})

korean_data.to_csv('korean.csv', index=False, encoding='utf-8-sig')

df_korean = pd.read_csv('practice.csv', encoding='utf-8-sig')
print('==== korean.csv 파일 읽어오기 ====')
print(df_korean)
print()
