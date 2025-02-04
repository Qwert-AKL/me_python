def fake_divide(first,second):
    global div_fake_dive
    try:
        div_fake_dive = first / second
        print(f'При делении первого числа: {first} на второе: {second} Ответ: {div_fake_dive }')
    except ZeroDivisionError:
        div_fake_dive ='Ошибка'
        print(f'При делении первого числа: {first} на второе: {second} Ответ: {div_fake_dive }')
        print("На 0 делить в классической математике нельзя")


# fake_divide(1,10)
# fake_divide(1,0)