# # #Примечание 2. Последовательность символов \n называется управляющей последовательностью и задаёт перевод строки.
# # print('a', '\n', 'b', '\n', 'c', sep='*', end='#')
# # #Примечание 3. Параметры sep и end можно устанавливать одновременно.
# # print('a', 'b', 'c', sep='*', end='finish')
# # #Примечание 4. Для разных команд print() можно задавать разные параметры sep и end.
# # arg1 = 'Hello'
# # sep1 = '_-_'
# # end2 = '+++'
# # print(arg1, 'everyone', sep=sep1, end='! ')
# # print('How', 'are', 'you', 'in', '2024?', sep=' ', end=end2)

# # #Примечание 5. Чтобы убрать все дополнительные выводимые символы, можно установить параметры sep и end команды print() как пустые строки ('').
# # print('a', 'b', 'c', sep='', end='')
# # print('d', 'e', 'f', sep='', end='')

# # #Примечание 6. Если после вывода данных нужно более одного перевода строки, то можно использовать следующий код:
# # print('Python', end='\n\n\n')
# # print('31', '12', '2019', sep='/')

# # separ = '+'
# # print('a', 'b', sep=separ)
# # print('YES', sep='!', end='#')
# # print('NO', sep='#', end='!')

# # delimiter = '/'
# # print('a', 'b', sep=delimiter, end='+')
# # print('c', 'd', sep='*', end=delimiter)

# # print('Mercury', 'Venus', sep='*', end='!')
# # print('Mars', 'Jupiter', sep='**', end='?')



# # print('a', 'b', 'c', sep='*')
# # print('d', 'e', 'f', sep='**', end='')
# # print('g', 'h', 'i', sep='+', end='%')
# # print('j', 'k', 'l', sep='-', end='\n')
# # print('m', 'n', 'o', sep='/', end='!')
# # print('p', 'q', 'r', sep='1', end='%')
# # print('s', 't', 'u', sep='&', end='\n')
# # print('v', 'w', 'x', sep='%')
# # print('y', 'z', sep='/', end='!')
# # print('БЕСКОНЕЧНОСТЬ', 'НЕ', 'ПРЕДЕЛ', '!', sep='_')

# # print('БЕСКОНЕЧНОСТЬ_НЕ_ПРЕДЕЛ!')

# # print('БЕСКОНЕЧНОСТЬ', 'НЕ', 'ПРЕДЕЛ!', sep='_', end='!')

# # print('БЕСКОНЕЧНОСТЬ', 'НЕ', 'ПРЕДЕЛ', sep='_', end='')
# # print('!')

# # print('БЕСКОНЕЧНОСТЬ_НЕ_ПРЕДЕЛ', end='')
# # print('!')

# # print('БЕСКОНЕЧНОСТЬ_', 'НЕ_', 'ПРЕДЕЛ!', sep='', end='')

# print('I', 'like', 'Python',sep="***")

# separ=input()
# text1=input()
# text2=input()
# text3=input()
# print(text1,text2,text3,sep=separ)