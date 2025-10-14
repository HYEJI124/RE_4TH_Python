import pandas as pd
# 실습1. 조건 필터링 연습(1)

df = pd.DataFrame({
'이름': ['민준', '서연', '지후', '서준', '지민'],
'점수': [78, 92, 85, 60, 88],
'반': [1, 2, 1, 2, 1]
})

# 1. 점수(score)가 80점 이상인 학생만 추출하세요.
score = df[df['점수'] >= 80]
print('문제 1')
print(score)
print()

# 2. 1반(반==1) 학생들 중, 점수가 85점 이상인 학생만 추출하세요.
class1 = df[(df['반'] == 1) & (df['점수'] >= 85)]
print('문제 2')
print(class1)
print()

# 3. 이름이 '서연' 또는 '지민'인 학생만 추출하세요.
extract = df[df['이름'].isin(['서연', '지민'])]
# extract = df[(df['이름'] == '서연') | (df['이름'] == '지민')]
print('문제 3')
print(extract)
print()

# 4. 문제 3에서 추출한 결과에서 인덱스를 0부터 재정렬하여 출력하세요.
reindex = extract.reset_index(drop=True)
# df_isin = df[df['이름'].isin(['서연', '지민'])]
# df_isin = df_isin.reset_index()
print('문제 4')
print(reindex)
print()

# 5. 점수가 80점 미만이거나 2반인 학생만 추출하세요.
class2 = df[(df['점수'] < 80) | (df['반'] == 2) ]
# class2 = class2.reset_index(drop=True)
print('문제 5')
print(class2)
print()

# 6. 문제 5의 결과에서 '점수' 컬럼이 70점 이상인 학생만 다시 추출하고, 인덱스를 재정렬하여 출력하세요.
reextract = class2[class2['점수'] >= 70].reset_index(drop=True)
print('문제 6')
print(reextract)
print()
