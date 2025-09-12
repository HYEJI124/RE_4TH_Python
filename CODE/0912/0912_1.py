list1 = list()
list2 = list("Hello")

# H  e  l  l  o
# 0  1  2  3  4
# 0 -4 -3 -2 -1
print(list1)
print(list2)

print('인덱스 0: ', list2[0])
print('인덱스 3: ', list2[3])
print('인덱스 4: ', list2[4])

print('인덱스 -1: ', list2[-1])
print('인덱스 -3: ', list2[-3])

# 리스트
list2[4] = 'a'
print('list2', list2)

# # 문자열 -> 인덱스로 수정 불가
# text = 'python'
# text[1] = 'a'
# print('text', text)

# list3 = list("Python")
text3 = "Hello"

# H  e  l  l  o
# 0  1  2  3  4
#-5 -4 -3 -2 -1

# print('list3[:]', list3[:])
print('text3[:]', text3[:]) #Hello
print('text3[:3]', text3[:3]) # Hel
print('text3[2:4]', text3[2:4]) # ll
print('text3[-3:-1]', text3[-3:-1]) # ll

print('text3[::-1]', text3[::-1]) # olleH(문자열 뒤집기)
print('text3[::-2]', text3[::-2]) # olH
print('text3[:-4:-2]', text3[:-4:-2]) # ol

numbers = [10, 20, 30, 40, 50]
print('1. numbers', numbers)
# numbers = [10, 40, 20, 40, 50]

numbers[1:3] = [40, 20]
print('2. numbers', numbers)

numbers[1:3] = [40, 20, 30]
print('3. numbers', numbers)

# [10, 20, 30, 40, 50]
#   0   1   2   3   4
print('numbers[1:3]', numbers[1:3])
print('numbers[:3:2]', numbers[:3:2]) # 10, 30
print('numbers 뒤집기', numbers[::-1])


# # list1 = [10, 20, 30, 40, 50]

# # 3 인덱스 요소 삭제
# del list1[3]
# print(list1)

# del list1[1:3]
# print(list1)

# del list1
# print(list1)


list1 = [1,2,3,4,5]
list2 = [2,3,4,5]
result = list1 + list2
print(result)

result = list1 * 3
print(result)

print("1" in list1) # False
print(1 in list1) # True

print(1 not in list1) # False

