#Задача "Все ли равны?":
#   - На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно
#first = int
#second = int
#third = int
print("Введите первое целое число: ")# в данном случае вложенность из if обусловлена тем, что программа должна
                                     # завершиться в случае, если одно из чисел введено некорректно!
parsing_var = input()
if parsing_var.isnumeric():
    first = int(parsing_var)

    print("Введите второе целое число: ")
    parsing_var = input()
    if parsing_var.isnumeric():
        second = int(parsing_var)

        print("Введите третье целое число: ")
        parsing_var = input()
        if parsing_var.isnumeric():
            third = int(parsing_var)

            if first == second and second == third:
                print(3)
            else:
                if first == second or first == third or second == third:
                    print(2)
                else: print(0)




