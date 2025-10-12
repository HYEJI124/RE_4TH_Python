import pandas as pd

print(pd.__version__)

# 데이터 분석

'''
    과정
        : 데이터 수집 -> 데이터 정제 -> 데이터 탐색 -> 데이터 분석 -> 시각화 -> 인사이트 도출
'''

'''
    1. 데이터 수집
        분석할 자료를 모으는 단계
    2. 데이터 정제
        분석 가능한 형태로 만드는 단계
    3. 데이터 탐색
        데이터의 특성을 파악하는 단계
    4. 데이터 분석
        가설을 검증하고 패턴을 찾는 단계
    5. 시각화
        결과를 이해하기 쉽게 표현하는 단계
    6. 인사이트 도출
        분석 결과를 의사결정에 활용하는 단계
'''

'''
    편의점 사장님의 고민
    문제: 어떤 제품을 더 많이 주문해야할까?
    데이터: 지난 3개월 판매 기록
    분석: 요일별, 시간대별 판매 패턴 파악
    인사이트: 금요일 저녁에 맥주가 가장 많이 팔림
    행동: 금요일 전에 맥주 재고 확충
'''

# Excel, pandas 비교

'''
    Excel로 100만개 데이터를 처리한다면?
    2019 버전 1000000행 까지만 제한이 됨
    파일 열기만 해도 5분 이상 소요
    수식 계산 시 프로그램 멈춤
    반복 작업을 매번 수동으로 해야 함
'''

# Series
# Pandas의 가장 기본이 되는 1차원 데이터 구조
'''
    1. 1차원 배열: 데이터가 일렬로 나열되어 있음
    2. 레이블(인덱스) 보유: 각 데이터에 이름을 붙일 수 있음
    3. 동일 타입: 하나의 series 안의 모든 데이터는 같은 타입
'''

simple_series = pd.Series([10, 20, 30, 40, 50])
print(simple_series)
print()

'''
    Series = Value(값) + Index(인덱스) + Name(이름)
'''

data_series = pd.Series(
    data = [10, 20, 30, 40, 50], # 1. 값: 실제 저장된 데이터
    index = ['Alice', 'Bob', 'Charlie', 'David', 'Eve'], # 2. 인덱스: 각 값의 레이블
    name='Test_Score' # 이름: Series 전체의 이름
)
print(data_series)
print()

'''
    pd.Series(data=None, index=None, name=None)
    
    매개변수 설명
    data=None: 실제 데이터(필수)
        - 리스트, 딕셔너리, 스칼라값, Numpy 배열
    index=None: 인덱스 레이블(선택)
        - 기본값 0, 1, 2...
        - 리스트, 배열 등으로 지정
    dtype=None: 데이터 타입(선택)
        - 자동 추론되지만 명시 가능
    name=None: Series 이름(선택) 
'''

'''
    각 구성요소의 역할:
    Value(값)
        실제 데이터가 저장되는 부분
        Numpy 배열로 저장됨
        빠른 수치 연산 가능
    Index(인덱스)
        각 값을 식별하는 레이블
        기본값: 0, 1, 2, ...(정수)
        사용자 정의 가능(문자열, 날짜 등)
    Name(이름)
        Series 전체를 설명하는 이름
        선택사항(없어도 됨)
        DataFrame 결합 시 컬럼명이 됨
'''

int_series = pd.Series([1, 2, 3, 4, 5])
print(f'Integer Series dtype: {int_series}') # int64

float_series = pd.Series([1.1, 2.2, 3.3, 4.4, 5.5])
print(f'Float Series dtype: {float_series}') # float64

str_series = pd.Series(['Apple', 'Banana', 'Cherry'])
print(f'Str Series dtype: {str_series}') # object

bool_series = pd.Series([True, False, True])
print(f'Boolean Series dtype: {bool_series}') # bool

mixed_series = pd.Series([1, 2.5, 3])
print(f'Mixed Series dtype: {mixed_series}') # 자동 변환

# dtype이 중요한 이유
'''
    1. 메모리 사용량 결정
    2. 연산 가능 여부
    3. 성능에 영향
'''

# 리스트 생성
temp_list = [15.5, 17.2, 18.9, 19.1, 20.1]
temp = pd.Series(temp_list, name = '4월_기온')
print(temp)
print()

'''
0    15.5
1    17.2
2    18.9
3    19.1
4    20.1
Name: 4월_기온, dtype: float64
'''

date = pd.date_range('2025-04-01', periods=5)
print(date)
print()
'''
DatetimeIndex(['2025-04-01', '2025-04-02', '2025-04-03', '2025-04-04',
               '2025-04-05'],
              dtype='datetime64[ns]', freq='D')
'''

temp_date = pd.Series(temp_list, index=date, name='4월_기온')
print(temp_date)
print()
'''
2025-04-01    15.5
2025-04-02    17.2
2025-04-03    18.9
2025-04-04    19.1
2025-04-05    20.1
Freq: D, Name: 4월_기온, dtype: float64
'''

# 딕셔너리 생성
product = {
    '노트북' : 15,
    '마우스' : 40,
    '키보드' : 20
}

product_series = pd.Series(product, name='현재재고')
print(product_series)
print()

scalar_series = pd.Series(0,
                          index=['월', '화', '수', '목'],
                          name='판매량')

print(scalar_series)
print()

test_scores = pd.Series(
    data=[85, 86, 59, 97, 65],
    index=['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    name='Exam'
)

print('=== Series 속성 전체 ===')
# 1. value - 실제 데이터(Numpy 배열)
print('1. values (값들)')
print(test_scores.values)
print()

# 2. index (인덱스)
print('2. index (인덱스)')
print(test_scores.index)
print()

# 3. name (이름)
print('3. name (이름)')
print(test_scores.name)
print()

# 4. dtype (타입)
print('4. dtype (타입)')
print(test_scores.dtype)
print()

# 5. shape (모양)
print('5. shape (모양)')
print(test_scores.shape)
print()

# 6. size (크기)
print('6. size (크기)')
print(test_scores.size)
print()

# 7. ndim (차원)
print('7. ndim (차원)')
print(test_scores.ndim) # 1
print()

# 인덱싱과 슬라이싱

# 인덱싱
# Series에서 특정 데이터를 선택하는 방법
# 위치 기반 0, 1, 2,
# 레이블 기반: 인덱스 이름으로 접근

sales = pd.Series(
    [100, 200, 150, 300],
    index=['Mon', 'Tue', 'Wed', 'Thu'],
    name='Daily_Sales'
)

wed_sales = sales['Wed']
print('sales["Wed"] 수요일 매출', wed_sales)
print()
print('sales.loc 수요일 매출', sales.loc['Wed'])
print()

# wed_sales2 = sales[2]
# print('수요일 매출', wed_sales2)
# print()
print('sales.iloc[2] 수요일 매출', sales.iloc[2])

selected_days = sales[['Mon', 'Wed', 'Thu']]
print(selected_days)
print()

print('sales.loc 수요일까지 매출', sales.loc[:'Wed'])
print()

# 슬라이싱
print('처음부터 수요일까지:')
print(sales.loc[:'Wed'])
print()

print('수요일부터 끝까지:')
print(sales.loc['Wed':])
print()

print('처음부터 끝까지:')
print(sales.iloc[:])
print()

print('역순:')
print(sales.iloc[::-1])
print()

# Boolean 인덱싱
sales = pd.Series(
    [100, 200, 150, 300],
    index=['Mon', 'Tue', 'Wed', 'Thu'],
    name='Daily_Sales'
)

condition = sales >= 200
print(condition)
print()

# result = sales[sales >= 200]
result = sales[condition]
print(result)
print()

# 비교 연산자
print('sales[sales == 200]')
print(sales[sales == 200])
print()

print('sales[(sales >= 150) & (sales <= 350)]')
print(sales[(sales >= 150) & (sales <= 350)])
print()

print('sales[(sales < 150) | (sales >= 300)]')
print(sales[(sales < 150) | (sales >= 300)])
print()

print('sales[(sales != 200)]')
print(sales[(sales != 200)])
print()

# 복합 조건
sales = pd.Series(
    [100, 200, 150, 300, 250],
    index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    name='Daily_Sales'
)

weekday_high = sales[(sales >= 200) & (sales.index != 'Fri')]
print('weekday_high')
print(weekday_high)
print()

weeked_or_low = sales[(sales < 200) | sales.index.isin(['Mon', 'Fri'])]
print('weeked_or_low')
print(weeked_or_low)
print()

# 벡터화 연산
prices = pd.Series(
    [3000, 1500, 4000, 2000],
    index=['apple', 'banana', 'orange', 'grape'],
    name='Price'
)

print('1. 500원 추가:')
print(prices + 500)
print()

print('2. 1000원 할인:')
print(prices - 1000)
print()

print('3. 20% 할인(곱셈):')
print(prices * 0.8)
print()

print('4. 반값 할인(나눗셈):')
print(prices / 2)
print()

store_a = pd.Series(
    [1000, 2000, 1500],
    index = ['Apple', 'Pear', 'Orange']
)
store_b = pd.Series(
    [900, 2200, 1400, 2500],
    index = ['Apple', 'Pear', 'Orange', 'Grape']
)

print(store_a)
print()
print(store_b)
print()
print(store_a + store_b)
print()
price_diff = store_a - store_b
print('price_diff')
print(price_diff)
print()

# Nan 결측값 처리하며 연산하기
# 1. fill_value 사용
price_diff_filled = store_b.sub(store_a, fill_value=0) # store_b에는 있지만 store_a에는 없는 것의 값을 0으로 채움
print('price_diff_filled')
print(price_diff_filled)
# Grape 2500 - 0으로 계산됨
print()

# 2. reindex로 먼저 맞추기
store_a_reindexed = store_a.reindex(store_b.index, fill_value=0) # b에 있는 index를 기준으로 a의 index를 다시 만들어서 a에 없던 index 값은 0으로 채움
print('store_a_reindexed')
print(store_a_reindexed)
print()
price_diff_reindexed = store_b - store_a_reindexed
print()

# 3. dropna로 결측값 제거 후 연산
price_diff_cleaned = price_diff.dropna() # 결측값 제거
print('price_diff_cleaned')
print(price_diff_cleaned)
print()

# 비교 연산
store_a = pd.Series(
    [1000, 2000, 1500],
    index = ['Apple', 'Pear', 'Orange']
)
store_b = pd.Series(
    [900, 2200, 1400],
    index = ['Apple', 'Pear', 'Orange']
)

is_b_cheaper = store_a > store_b
print('B상점이 더 저렴한 제품:')
print(is_b_cheaper)
print()

# 저렴한 상점의 가격만 선택
best_prices = store_a.where(is_b_cheaper, store_b)
print('best_prices')
print(best_prices)
print()