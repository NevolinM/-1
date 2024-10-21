numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
none_ = numbers.index(None)

sum_of_numbers = sum(numbers[:none_]) + sum(numbers[none_ + 1:])
count_of_numbers = len(numbers)
average_of_numbers = sum_of_numbers / count_of_numbers

numbers[none_] = average_of_numbers
print("Измененный список:", numbers)
