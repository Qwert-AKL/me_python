# auto-py-to-exe
import tkinter as tk  # "as tk"  сокращение библиотеки, для удобства

# Функция возврата
def get_values():   # чисто для возврата данных из полей
    num1 = int(number1_entry.get())  # для получения данных из поля и передача в переменную num1
    num2 = int(number2_entry.get())
    print(num1 + num2)
    return num1,num2        #возвращает значение

def insert_values(value):
    answer_entry.delete(0, 'end')  # для очитски формы перед вставкой
    answer_entry.insert(0, value)
    pass

# функция для суммирования
def add():
    num1,num2=get_values()  # полчаем данные из возращающей функции
    # num1 = int(number1_entry.get())  # для получения данных из поля и передача в переменную num1
    # num2 = int(number2_entry.get())
    # print(num1 + num2)
    res = num1 + num2
    insert_values(res)   # передача в фунцию значения
    # answer_entry.delete(0,'end')  # для очитски формы перед вставкой
    # answer_entry.insert(0, res)  # вставление результата в поле "Ответ". указыается индекс, а потом что вставляем.

# функция для вычитания
def sub():
    num1, num2 = get_values()
    print(num1 - num2)
    res = num1 - num2
    insert_values(res)
    # answer_entry.delete(0,'end')  # для очитски формы перед вставкой
    # answer_entry.insert(0, res)  # вставление результата в поле "Ответ". указыается индекс, а потом что вставляем.

def mul():
    num1, num2 = get_values()
    print(num1 * num2)
    res = num1 * num2
    insert_values(res)
    # answer_entry.delete(0,'end')  # для очитски формы перед вставкой
    # answer_entry.insert(0, res)  # вставление результата в поле "Ответ". указыается индекс, а потом что вставляем.
def div():
    pass
    num1, num2 = get_values()
    print(num1 / num2)
    res = num1 / num2
    insert_values(res)

    # answer_entry.delete(0,'end')  # для очитски формы перед вставкой
    # answer_entry.insert(0, res)  # вставление результата в поле "Ответ". указыается индекс, а потом что вставляем.


# создание окошка.
window = tk.Tk()  # создание окошка. берём библиотеку tk  и используем из неё класс Tk
window.title('Калькулятор')
window.geometry('210x310')
window.resizable(False, False)  # блокировка изменения размера окна
button_add = tk.Button(window, text='+', width=4, height=2,
                       command=add)  # создание кнопки и привязка к окну под названием window
button_add.place(x=25, y=150)  # создание кнопки в координатах
button_sub = tk.Button(window, text='-', width=4, height=2,command=sub)
button_sub.place(x=65, y=150)
button_mul = tk.Button(window, text='*', width=4, height=2,command=mul)
button_mul.place(x=105, y=150)
button_div = tk.Button(window, text='/', width=4, height=2,command=div)
button_div.place(x=145, y=150)

# Первое поле для ввода
number1 = tk.Label(window, text='Введите первое число')
number1.place(x=10, y=20)
number1_entry = tk.Entry(window, width=30)  # подключение библиотеки Entry из tk  для создание односстрочного поля
number1_entry.place(x=10, y=50)

# Второе поле для ввода
number2 = tk.Label(window, text='Введите второе число')
number2.place(x=10, y=75)
number2_entry = tk.Entry(window, width=30)
number2_entry.place(x=10, y=100)

# Поле Ответа
answer = tk.Label(window, text='Ответ')
answer.place(x=10, y=220)
answer_entry = tk.Entry(window, width=30)
answer_entry.place(x=10, y=250)

window.mainloop()  # обновление событий. обновление инф. на экране
