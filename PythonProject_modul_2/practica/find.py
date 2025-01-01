def find_indexes(a_string, substring):
    start = 0

    indexes = []

    while start < len(a_string):
        start = a_string.find(substring, start)

        if start == -1:
            return indexes

        indexes.append(start)

        start += 1

    return indexes


string = 'bobby hadz bobbyhadz.com'
print(find_indexes(string, 'bob'))

string = 'bobobobob'
print(find_indexes(string, 'bob'))



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
string = str(input(''))


indexes = [
    index for index in range(len(string))
    if string.startswith('bobby', index)
]

print(indexes)  # 👉️ [0, 11]