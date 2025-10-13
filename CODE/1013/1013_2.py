import pandas as pd
import numpy as np
# 데이터 정제

# 현실의 더러운 데이터 예시

dirty_data = pd.DataFrame({
    # 중복된 이름, 결측값(None) 존재
    'name': ['John Doe', 'Jane Smith', 'John Doe', 'Jane Smith', None, 'Bob Wilson'],

    # 형식 불일치: 숫자, 문자열, None 혼재 / 이상값: 250살
    'age': ['25', '30 years', 28, 'thirty', None, 250],

    # 중복 이메일, 형식 오류(@뒤 도메인 누락), None
    'email': ['john@email.com', 'jane@email', 'john@email.com',
              'jane@email.com', 'invalid@', None],

    # 날짜 형식이 제각각: YYYY-MM-DD, YYYY.MM.DD, MM/DD/YYYY 혼재
    # 날짜 오류: 13월 45일은 존재하지 않음
    'join_date': ['2024-01-01', '2024.01.15', '01/20/2024',
                  '2024-01-15', None, '2024-13-45']
})

'''
    중복 데이터
    결측값: None, Nan
    형식 불일치: age, join_date
    이상값: age 250
'''

# 결측값
'''
    결측값(Missing Value)
    비어있는, 알 수 없는, 기록되지 않은 데이터를 의미

    종류
    None: Python의 빈 객체
    np.nan: Numpy의 Not a Number
    pd.NA: Pandas의 결측값(최신)
    빈 문자열: '' 또는 " "(공백)
    특수값: -99999, 99999
'''

missing_types = pd.DataFrame({
    'none_type': [1, 2, None, 4],           # Python None
    'nan_type': [1, 2, np.nan, 4],         # NumPy NaN
    'empty_string': ['A', 'B', '', 'D'],   # 빈 문자열
    'whitespace': ['A', 'B', ' ', 'D'],    # 공백
    'special_value': [1, 2, -999, 4]       # -999를 결측값으로 사용하는 경우
})

print(missing_types)
print()

# 결측값 탐지
# isnull() / isna()
# 결측값이면 True

# notna() / notnull()
# 값이 있으면 True

print('==== isna() ====')
print(missing_types.isna())
print(missing_types.isnull())
print()


print('==== notna() ====')
print(missing_types.notna())
print(missing_types.notnull())
print()

# 결측값 통계 확인
print('==== 열별 결측값 개수 ====')
print(missing_types.isna().sum())
print()

# 전체 결측값 개수
print('==== 전체 결측값 개수 ====')
print(missing_types.isna().sum().sum())
print()

# 결측값 처리 전략

'''
    삭제 - 결측값이 있는 행/열 제거
    대체 - 다른 값으로 채우기
    예측 - 앞뒤 값이나 패턴으로 추정
'''

# 결측값이 있는 샘플 데이터
sales_data = pd.DataFrame({
    'date': pd.date_range('2024-01-01', periods=7),
    'sales': [100, 120, np.nan, 150, np.nan, 180, 200],
    'customers': [20, 25, 22, np.nan, 30, 35, 40],
    'region': ['Seoul', 'Busan', np.nan, 'Daegu', 'Seoul', np.nan, 'Busan']
})
print('==== 원본 ====')
print(sales_data)
print()

# 삭제
# 1-1 결측값이 있는 행 전체 삭제
drop_rows = sales_data.dropna()
print('결측값이 있는 행 삭제:')
print(drop_rows)
print()

# 1-2 결측값이 있는 열 전체 삭제
drop_cols = sales_data.dropna(axis=1)
print('결측값이 있는 열 삭제:')
print(drop_cols)
print()

# 1-3 특정 열 기준 삭제
drop_sales = sales_data.dropna(subset=['sales'])
print('sales열 기준 결측값 있는 행 삭제:')
print(drop_sales)
print()

# 대체
# 2-1 평균값으로 대체
fill_mean = sales_data.copy()
fill_mean['sales'] = fill_mean['sales'].fillna(fill_mean['sales'].mean())
print(fill_mean)
print()

# 2-2 중앙값으로 대체(이상값이 있을 경우 유용)
fill_median = sales_data.copy()
fill_median['sales'] = fill_mean['sales'].fillna(fill_mean['sales'].median())
print(fill_median)
print()


# 시계열 대체
# 시간 순서가 있는 데이터에서 앞뒤 값으로 결측값을 채움

# 3-1 Forward Fill(앞의 값으로 채우기)
fill_forward = sales_data.copy()
fill_forward['customers'] = fill_forward['customers'].fillna(method='ffill')
print(fill_forward)
print()

# 3-2 Backward Fill(뒤의 값으로 채우기)
fill_backward = sales_data.copy()
fill_backward['customers'] = fill_backward['customers'].fillna(method='bfill')
print(fill_backward)
print()