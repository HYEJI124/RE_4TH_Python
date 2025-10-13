import pandas as pd

# CSV
# CSV(Comma-Separated Values) 가장 널리 사용되는 데이터 파일 형식

'''
    특징
    쉼표(,)로 값을 구분
    텍스트 파일이라 어디서나 열람 가능
    가볍고 빠름
    Excel, Google Sheets 등과 호환 가능
'''

# CSV 파일 예시 내용
'''
name,   age,   city,   salary
John,   25,   Seoul,   50000
Jane,   30,   Busan,   60000
Park,   35,   Daegu,   55000
'''

sample_data = pd.DataFrame({
    'name':['John', 'Jane', 'Park'],
    'age':[25, 30, 35],
    '도시':['서울', '부산', '대구'],
    'Salary':[50000, 60000, 55000]
})

# UTF-8로 저장 (기본값, 권장)
sample_data.to_csv('sample_data.csv', index=False,
                   encoding='utf-8-sig')
# utf-8-sig: UTF8 + BOM (Excel 호환)

# CP949로 저장 (Window 한글)
# sample_data.to_csv('sample_data.csv', index=False,
#                    encoding='cp949')

df = pd.read_csv('sample_data.csv', encoding='utf-8-sig')
# df = pd.read_csv('sample_data.csv', encoding='cp949')
print('==== CSV 파일 읽기 ====')
print(df)
print(f'데이터 타입:\n {df.dtypes}')
print(f'데이터 크기:\n {df.shape}')
print()

# sep - 구분자 설정
sample_data.to_csv('tab_separated.txt', sep='\t', index=False)

df_tab = pd.read_csv('tab_separated.txt', sep='\t')
print('==== CSV sep=탭 파일 읽기 ====')
print(df_tab)
print(df_tab.head()) # head(): 처음 5개 행(기본값)
print()

# Excel
# 엑셀은 마이크로소프트의 스프레드시트 프로그램
'''
    특징
    여러 시트(Sheet) 지원
    서식, 수식 포함 가능
    비즈니스에서 가장 많이 사용
    확장자 최신:(.xlsx), 구버전:(.xls)
    pip install openpyxl
'''

sample_data = pd.DataFrame({
    'name':['John', 'Jane', 'Park'],
    'age':[25, 30, 35],
    '도시':['서울', '부산', '대구'],
    'Salary':[50000, 60000, 55000]
})

sample_data.to_excel('sample_data.xlsx', index=False, sheet_name='Default')
print('샘플 엑셀 파일 생성 완료')
print()

df_excel = pd.read_excel('sample_data.xlsx')
print('==== Excel 파일 읽기 ====')
print(df_excel)
print()

sample_data = pd.DataFrame({
    'name':['John', 'Jane', 'Park'],
    'age':[25, 30, 35],
    '도시':['서울', '부산', '대구'],
    'Salary':[50000, 60000, 55000]
})

# 여러 시트 다루기
with pd.ExcelWriter('multi_sheet.xlsx') as writer:
    sample_data.to_excel(writer, sheet_name='Default1', index=False)
    sample_data['name'].to_excel(writer, sheet_name='name', index=False)

print('2개의 시트를 가진 엑셀 파일 생성 완료')
print()

# JSON
# JSON(JavaScript Object Notation)
# 웹에서 많이 사용되는 데이터 형식

sample_data = pd.DataFrame({
    'name':['John', 'Jane', 'Park'],
    'age':[25, 30, 35],
    '도시':['서울', '부산', '대구'],
    'Salary':[50000, 60000, 55000]
})

sample_data.to_json('sample_data.json', orient='records', indent=2)
print('JSON 파일 저장')
print()

df_json = pd.read_json('sample_data.json')
print('==== JSON 파일 읽기 ====')
print(df_json)
print()


data = {
    '이름': ['홍길동', '이순신', '김유신', '강감찬', '장보고', '이방원'],
    '나이': [23, 35, 31, 40, 28, 34],
    '직업': ['학생', '군인', '장군', '장군', '상인', '왕자']
}
df = pd.DataFrame(data)

# 인덱싱
print('==== 인덱싱 ====')
print(df['이름'])
print()
print(df[['이름', '직업']])
print()
print(df[['이름', '나이', '직업']])
print()

# 슬라이싱
print(df[1:3])
print()
print(df[-2:])
print()

# DataFrame의 슬라이싱은 행(Row) 기준으로 동작
# 열 단위 슬라이싱은 명시적으로 지정
print(df[-2:]['이름'])
print()

# iloc
print('==== iloc ====')
print(df)
print()
print(df.iloc[0]) # 0번 행 전체
print()
print(df.iloc[:, 1]) # 모든 행의 1번(컬럼) 나이
print()
print(df.iloc[[0, 2, 4], [0, 2]])
print()

# loc
print('==== loc ====')
print(df.loc[0]) # 0번 행 전체
print()
print(df.loc[:, '나이'])
print()
print(df.loc[:, ['이름', '나이']])
print()
print(df.loc[1:3, ['이름', '나이']]) # 1 ~ 3행까지(끝 포함)
print()

