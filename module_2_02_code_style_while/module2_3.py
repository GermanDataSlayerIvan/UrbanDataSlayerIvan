# Задача "Нули ничто, отрицание недопустимо!":
#   - Дан список чисел [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
#   Нужно выписывать из этого списка только положительные числа до тех пор, пока не встретите отрицательное или
#   не закончится список (выход за границу).
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
curr_index = -1

while curr_index < len(my_list):
    curr_index += 1
    curr_element = my_list[curr_index]

    if curr_element < 0:
        break

    if curr_element == 0:
        continue
    print(curr_element)