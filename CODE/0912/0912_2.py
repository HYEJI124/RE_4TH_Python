# 요소 추가 메소드
numbers = [10, 21, 15, 22, 54]

numbers.append(20)
print(numbers)

numbers.append(12)
print(numbers)

numbers.extend([19])
print(numbers)

numbers.extend([5, 29])
print(numbers)


# append - extend 차이점
# append - 리스트 자체가 추가됨
numbers.append([1,2,3]) # 리스트 형식으로 마지막에 하나의 요소로 추가됨
print(numbers)

# extend - 요소들이 추가됨
list2 = [6, 7, 8]
numbers.extend(list2)
print(numbers)

numbers.insert(2, 30)
print(numbers)

# 요소 삭제 메소드

fruits = ["사과", "바나나", "오렌지", "바나나", "포도"]
fruits.remove("바나나")
print(fruits)

removed = fruits.pop()
print(removed)
print(fruits)

removed = fruits.pop(1) # 오렌지
print(removed)
print(fruits)

fruits.clear() # 모든 요소 제거
print(fruits)

# 요소 검색, 정렬 메소드
numbers = [1, 2, 6, 9, 5, 3, 2, 4, 7]

idx = numbers.index(6) # 6의 위치 찾기
print("idx:", idx)

idx = numbers.index(9) # 9의 위치 찾기
print("idx:", idx)

count = numbers.count(2)
print("count:", count)

numbers.sort() # 오름차순
print("numbers:", numbers)

numbers.sort(reverse=True) # 내림차순
print("numbers:", numbers)

# Sorted
original = [3, 2, 5, 7, 1]
sorted_list = sorted(original)
sorted_r_list = sorted(original, reverse=True)


print("original", original)
print("sorted_list", sorted_list)
print("sorted_r_list", sorted_r_list)

# 연산 메소드
numbers = [5, 2, 7, 3, 11, 45, 5, 2, 7, 3, 11, 45]
max_num = max(numbers)
min_num = min(numbers)

print("max_num", max_num)
print("min_num", min_num)

sum_num = sum(numbers)
print("sum_num", sum_num)




