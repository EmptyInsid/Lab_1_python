#задание 1: Замена пропущенного элемента средним арифметическим

numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

wrong_num = numbers.index(None)
sum_before = sum(numbers[:wrong_num])
sum_after = sum(numbers[wrong_num + 1:])
count_of_num = len(numbers)

numbers[wrong_num] = (sum_after + sum_before) / count_of_num

print("Измененный список:", numbers)
