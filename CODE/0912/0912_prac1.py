# 실습 1. 인덱싱, 슬라이싱 복습문제
# 1-1.
nums = [10, 20, 30, 40, 50]
print(nums[0])
print(nums[-1])

# print("첫번째 요소:", nums[0])
# print("마지막 요소:", nums[-1])

# 1-2.
nums = [100, 200, 300, 400, 500, 600, 700]
print(nums[2:5])

nums = [100, 200, 300, 400, 500, 600, 700]
mid = 7 // 2
print("가운데 세 개의 요소", nums[mid-1:mid+2]) # 300, 400, 500

# 1-3.
nums = [1, 2, 3, 4, 5]
for i in range(5):
    nums[i] *= 2
print("nums", nums)


# 1-4.
items = ["a", "b", "c", "d", "e"]
print("리스트 뒤집기", items[::-1])

# 1-5.
data = ["zero", "one", "two", "three", "four", "five"]
print("짝수 인덱스 요소", data[::2])

# 1-6.
movies = ["인셉션", "인터스텔라", "어벤져스", "라라랜드", "기생충"]
movies[2:4] = ["매트릭스", "타이타닉"]
print("movies", movies)

# 1-7.
subjects = ["국어", "수학", "영어", "물리", "화학", "생물", "역사", "지구과학", "윤리"]
result = subjects[3::2] # 세 개 하나씩 적어서 뽑아내는 방법도 있음
print(result)

# 1-8.
data = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
data1 = data[:3]
data2 = data[3:6]
data3 = data[6:]
print(f"{data1[::-1]}{data2[::-1]}{data3[::-1]}")

# data1 = data[:3][::-1]
# data2 = data[3:6][::-1]
# data3 = data[6:][::-1]
# print(data1, data2, data3, sep=' ')

# 실습 2. 리스트 연산 복습문제
# 2-1.
fruits = ["apple", "banana", "cherry", "grape", "watermelon", "strawberry"]
del fruits[1:4]
print(fruits)

# 2-2.
letters = ["A", "B"]
result = letters * 3
del result[2]
print(result)

# 실습 3. 리스트 주요 메서드 복습 문제
# 3-1.
passenger = ["철수", "영희"]

passenger.extend(["민수", "지훈"])
passenger.remove("영희")
passenger.insert(1, "수진")
passenger.remove("민수")
passenger.reverse()

print(passenger)

# 3-2.
card = [5, 3, 7]
card.extend([4, 9])
print("max:", max(card))
print("min:", min(card))
print("sum:", sum(card))
card.sort()
card.pop()
print("최종 리스트:", card)