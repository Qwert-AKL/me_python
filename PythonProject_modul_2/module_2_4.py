numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
n = len(numbers)
is_prime = []
not_prime = []
for i in range(2, int(n*0.5)+ 1,1):
    k = 0
    for j in range(1, i + 1):
        if i % j == 0 and i != 1:
            k += 1
    if k == 2:
       is_prime.append(i)
    else:
        if i != 1 and i != 0:
            not_prime.append(i)
print("Primes: ", is_prime)
print("Not Primes: ", not_prime)



# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# n = len(numbers)
# is_prime = []
# not_prime = []
# for i in range(0,len(numbers)):
#     if numbers[i]<=1:
#         del numbers[i]
#         break
# print(numbers)
