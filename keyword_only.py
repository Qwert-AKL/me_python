def total(initial=15,*numbers,extra_number):
    count=initial
    for number in numbers:
        count+=number
    count+=extra_number
    print(count)
total(10,1,2,3,extra_number=50)
# total(10,1,2,3)