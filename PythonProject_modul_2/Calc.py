import tkinter as tk     # "as tk"  сокращение библиотеки, для удобства


# создание окошка.
window = tk.Tk()     # создание окошка. берём библиотеку tk  и используем из неё класс Tk
window.title('Калькулятор')
window.geometry('350x350')
window.resizable(False,False) # блокировка изменения размера окна
button_add=tk.Button(window,text='+',width=4,height=2) #создание кнопки и привязка к окну под названием window
button_add.place(x=10,y=150) # создание кнопки в координатах
button_sub=tk.Button(window,text='-',width=4,height=2)
button_sub.place(x=50,y=150)
button_mul=tk.Button(window,text='*',width=4,height=2)
button_mul.place(x=90,y=150)
button_div=tk.Button(window,text='/',width=4,height=2)
button_div.place(x=130,y=150)

#Первое поле для ввода
number1=tk.Label(window,text='Введите первое число')
number1.place(x=10,y=20)
number1_entry=tk.Entry(window,width=30)   #подключение библиотеки Entry из tk  для создание односстрочного поля
number1_entry.place(x=10,y=50)

#Второе поле для ввода
number2=tk.Label(window,text='Введите второе число')
number2.place(x=10,y=75)
number2_entry=tk.Entry(window,width=30)
number2_entry.place(x=10,y=100)

#Поле Ответа
answer=tk.Label(window,text='Ответ')
answer.place(x=10,y=220)
answer_entry=tk.Entry(window,width=30)
answer_entry.place(x=10,y=250)

window.mainloop()    # обновление событий. обновление инф. на экране

