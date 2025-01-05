# while True:
#     a = int(input('Введите первое число: '))
#     b = int(input('Введите второе число: '))
#     summa = a + b
#     print('Сумма чисел равна: ', summa)
#     str = str(input('Прервать? нажми клавишу Y  '))
#     if str == 'Y' or str == 'y' or str == 'Н' or str == 'н':
#         break
#     continue

# *******
#  *   *
#   * *
#    *
#   * *
#  *   *
# *******
# n = 7
# for i in range(0, n):
#     for j in range(0, n):
#         if (i == 0 or i==j or i==n-1):  #i == 0 or i == n - 1 or j == i or j == n - i - 1
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

#  **   **
# **** ****
# *********
#  *******
#   *****
#    ***
#     *
# h = 7
# w = h + 2
# m = w //4
# for i in range(1, h+1):
#     if (i <= m):
#         print(" " * (m-i) + "*" * (2*i) + " " * (w-2*i-2*m) + "*" *(2*i) + " " * (m-i))
#     else:
#          print(" " * (i - 2*m+1) + "*" * (w-2*(i-2*m+1)) + " " * (i - 2*m+1))

# n=20
# k=1
# counter=1
# for i in range(n):
#     for j in range(n):
#         if k % 2 == 0:
#             print(counter, end ="  ")
#             counter+=1
#         else: print("*",end="  ")
#         k+=1
#     print()

# i = 1
# j = 1
# while i < 10:
#     while j < 10:
#         print(i * j, end="\t")
#         j += 1
#     print("\n")
#     j = 1
#     i += 1

for c1 in  "ab":
    for c2 in "ba":
        print(f"{c1}{c2}")
