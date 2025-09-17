# break
print("=======break=======")
for i in range(3):
    if i == 2:
        # break를 만나면 for문을 종료
        break
    print(i)

for i in range(10):
    break
    print(i)

print('for문 종료')

for i in range(10):
    print(i) # i = 0 다음 break 만나서 빠져나감
    break
    

print('for문 종료')
print()

print("=======continue=======")
for i in range(10):
    if i % 2: # 0이면 if문이 수행되지 않음 -> print(i)로 감
        continue
    print(i)

print()

print("=======pass=======")
for i in range(10):
    print(i)
    pass # 다음에 추가적으로 작업할 것. 그대로 넘어가라 -> for문 종료되거나 하지 않음

print()

for i in range(10):
    pass
    print(i)

print()

print("=======for-else=======")
for i in range(10):
    print(i)
    if i == 10:
        break
else:
    print('루프 정상 종료')

print()


colors = ['red', 'blue']
fruits = ['apple', 'banana']

for color in colors:
    for fruit in fruits:
        print(f'{color},{fruit}')

new_list = [(c, f) for c in colors for f in fruits]