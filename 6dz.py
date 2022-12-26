# Дан список интов, повторяющихся элементов 
# в списке нет. Нужно преобразовать это множество в строку, 
# сворачивая соседние по числовому ряду числа в диапазоны.

# num = [1,4,5,2,3,9,8,11,0]
# num.sort()
# sortnum = [[num[0]]]
# j = num[0]
# for i in num[1:]:
#     if i-j == 1:
#             sortnum[-1].append(i)
#     else:
#             sortnum.append([i])
#     j = i
# print (sortnum)


# Решить задачу, в которой необходимо найти сумму нечетных элементов при помощи lambda

some_list = [1, 2, 3, 4, 5]
summ = int(map(lambda i: [i] % 2 == 0, some_list))
print(sum(summ))