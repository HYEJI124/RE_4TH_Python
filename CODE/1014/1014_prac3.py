import pandas as pd
# 실습3. 정렬(1)

df = pd.DataFrame({
'name': ['Alice', 'Bob', 'Charlie', 'David'],
'score': [88, 95, 70, 100]
})
# 1. 주어진 DataFrame에서, score 컬럼 기준으로 오름차순 정렬한 결과를 출력하세요.
df_sorted_score = df.sort_values(by='score')
print('문제 1')
print(df_sorted_score)
print()

# 2. score 컬럼 기준 내림차순으로 정렬한 후, 정렬된 인덱스를 무시하고 0부터 재정렬한 결과를 출력하세요.
df_sorted_score = df.sort_values(by='score', ascending=False).reset_index(drop=True)
df_index_score = df_sorted_score.sort_index()
print('문제 2')
print(df_index_score)
print()

df = pd.DataFrame({
'이름': ['가', '나', '다', '라', '마'],
'반': [2, 1, 1, 2, 1],
'점수': [90, 85, 80, 95, 85]
})
# 3. 주어진 DataFrame에서,반(class) 기준 오름차순, 같은 반 내에서는 점수(score) 기준 내림차순으로 정렬한 결과를 출력하세요.
df_sorted_class = df.sort_values(by=['반', '점수'], ascending=[True, False])
print('문제 3')
print(df_sorted_class)
print()

# 4. 열(컬럼) 이름을 알파벳순으로 정렬해서 출력하세요.
df_col_sorted = df.sort_index(axis=1)
print('문제 4')
print(df_col_sorted)
print()

df = pd.DataFrame({
'value': [10, 20, 30, 40]
}, index=[3, 1, 4, 2])
# 5. 인덱스 기준으로 오름차순 정렬한 결과를 출력하세요.
df_index_sorted = df.sort_index()
print('문제 5')
print(df_index_sorted)
print()

# 6. 인덱스 기준 내림차순 정렬, value 컬럼 기준 오름차순 정렬 두 가지 정렬 결과를 각각 출력하
# 세요.
df_index_sorted = df.sort_index(ascending=False)
print('문제 6 - 1')
print(df_index_sorted)
print()
df_val_sorted = df.sort_values(by='value')
print('문제 6 - 2')
print(df_val_sorted)
print()