# # ХОД ЛАДЬИ
# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# if (x1==x2 and y1!=y2) or (x1!=x2 and y1==y2):
#     print('YES')
# else:
#     print('NO')

# ХОД короля
# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# if (x1==x2+1 or x1==x2-1 or x1==x2) and (y1==y2+1 or y1==y2-1 or y1==y2):
#     print('YES')
# else:
#     print('NO')


# Определяет, имеют ли указанные клетки один цвет или нет v.1
# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# if (x1+y1+x2+y2)%2==0:
#     print('YES')
# else:
#     print('NO')


# # Определяет, имеют ли указанные клетки один цвет или нет v/2
#  x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

# if x1==x2+:
#     print("YES")
# else:
#     print("NO")
#
# #
# a1,b1,a2,b2=int(input()),int(input()),int(input()),int(input())
# if a1-a2==b1-b2 or a1-a2==b2-b1:
#     print('YES')
# else:
#     print('NO')

# ХОД коня
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if abs((x1 - x2) * (y1 - y2)) == 2:
    print("YES")
else:
    print("NO")


# Ход ладьи:
# x1 == x2 or y1 == y2

# Ход коня:
# abs((x1 - x2) * (y1 - y2)) == 2

# Ход слона:
# abs(x1 - x2) == abs(y1 - y2)

# Ход ферзя (слон or ладья):
# abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2

# Ход короля:
# abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1
