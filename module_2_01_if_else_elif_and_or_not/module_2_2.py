#Задача "Все ли равны?":
#   - На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно;
#   - Если все числа равны между собой, то вывести 3
#   - Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
#   - Если равных чисел среди 3-х вообще нет, то вывести 0
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




