list1 = [1, 2, 3, 4, 5]
list2 = ['banana', 'apple', 'mango', 'oranges']
list1.extend(list2)
# print(list1)
list2.append('strawberries')
# print(list2)
# print(len(list1))
# list2.()
# print(len(list2))
# print(list2.index('mango'))

# print(list2.count('mango'))

list3 = [1, 2, 4, 10, 6]
list4 = list3
list4.sort()
print(list4)
list4 = list3
list4.reverse()
print(list4)
list5 = list3.copy()
print(list5)
list5.pop()
print(list5)
print(list5.pop(1))
print(list5)
del list5[0]
print(list5)