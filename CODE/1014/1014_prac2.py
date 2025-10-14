import pandas as pd
# 실습2. 행/열 추가·수정·삭제(1)

df = pd.DataFrame({
'이름': ['김철수', '이영희', '박민수'],
'국어': [90, 80, 70]
})

# 1. '수학' 점수 [95, 100, 88]을 새 열로 추가하세요.
df['수학'] = [95, 100, 88]
print('문제1')
print(df)
print()

# 2. 1번 문제의 DataFrame에서 '이름' 열을 삭제하세요.
df = df.drop('이름', axis=1)
print('문제2')
print(df)
print()

df = pd.DataFrame({
'제품': ['A', 'B'],
'가격': [1000, 2000]
})

# 3. 제품 'C', 가격 1500인 새 행을 추가하세요.
new_row = pd.DataFrame([{'제품': 'C', '가격': 1500}])
# new_row = pd.DataFrame([{'제품': ['C'], '가격': [1500]}])

df = pd.concat([df, new_row], ignore_index=True)
print('문제3')
print(df)
print()

df.loc[len(df)] = ['C', 1500]
print('문제3')
print(df)
print()

# 4. 3번 문제의 DataFrame에서 첫 번째 행(제품 'A')을 삭제하세요.
df = df.drop(0)
print('문제4')
print(df)
print()

df = pd.DataFrame({
'과목': ['국어', '영어', '수학'],
'점수': [85, 90, 78]
})

# 5. '점수'가 80 미만인 행을 모두 삭제하세요.
df = df[df['점수'] >= 80]
print('문제5')
print(df)
print()

df = df.drop(df[df['점수'] < 80].index)
print('문제5')
print(df)
print()

# 6. '학년' 열(값은 모두 1)을 추가하세요.
df['학년'] = 1
print('문제6')
print(df)
print()

df = pd.DataFrame({
'이름': ['A', 'B'],
'나이': [20, 22]
})

# 7. 이름이 'C', 나이가 25, 키가 NaN(결측값)인 새 행을 추가하세요.
# (단, '키'라는 새 열이 자동으로 추가되어야 함)
import numpy as np
new_row = pd.DataFrame([{'이름': 'C', '나이': 25, '키': np.nan}])
# new_row = pd.DataFrame({'이름': ['C'], '나이': [25], '키': [np.nan]})
df = pd.concat([df, new_row], ignore_index=True)
print('문제7')
print(df)
print()



df = pd.DataFrame({
'부서': ['영업', '기획', '개발', '디자인'],
'인원': [3, 2, 5, 1]
})

# 8. 인원이 2명 이하인 행을 모두 삭제하고,
df = df[df['인원'] > 2]
print('문제8')
print(df)
print()

df = df.drop(df[df['인원'] < 2].index)
print('문제8')
print(df)
print()

# 9. '평가' 열을 새로 추가해 모든 값을 '미정'으로 채우세요.
df['평가'] = '미정'
print('문제9')
print(df)
print()