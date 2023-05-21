fir_number =int(input('Enter your first number: '))
sec_number =int(input('Enter your second number: '))
thr_number =int(input('Enter your third number: '))

if fir_number >= sec_number and fir_number>=thr_number:
    biggest_num = fir_number
elif sec_number>= fir_number and sec_number>=thr_number:
    biggest_num = sec_number
elif thr_number >=fir_number and thr_number >= sec_number:
    biggest_num = thr_number

print("the biggest number is: ", biggest_num)              