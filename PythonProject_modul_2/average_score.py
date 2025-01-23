#Средний бал ученика
grades=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]    #данные в типе список
students={"Johny",'Bolbo','Steve','Khendrik','Aaron'} #данные в типе множества
print('Список студентов: ', students,type(students))
students_sort=list(students)    #преобразовываем в список
students_sort.sort() #сортировка списка
print('Сортированный список студентов: ', students_sort,type(students_sort))
students_grades=dict([[students_sort[0],grades[0]],[students_sort[1],grades[1]],[students_sort[2],grades[2]],[students_sort[3],grades[3]],[students_sort[4],grades[4]]])
print('Оценки студента: ',students_grades)
average_score=sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])
students_grades=dict([[students_sort[0],average_score[0]],[students_sort[1],average_score[1]],[students_sort[2],average_score[2]],[students_sort[3],average_score[3]],[students_sort[4],average_score[4]]])
print('Средний бал студента: ', students_grades)