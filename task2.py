# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено двузначных натуральных чисел,
# и сколько других.
a=int(input())
x=0
z=0
while a!=0:
    if a>=10 and a<=99:
        x+=1
    else:
        z+=1
    a = int(input())
print('Двузначных чисел:', x)
print('Других чисел:',z)