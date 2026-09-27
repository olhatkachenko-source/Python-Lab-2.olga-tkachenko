def convert_to_integers(float_list):
    int_list = []
    for number in float_list:
        int_list.append(round(number))
    return int_list

user_input = input("Введіть дійсні числа через пробіл (наприклад, 2.3 4.8 7.1): ")

floats = []
for item in user_input.split():
    floats.append(float(item))

result = convert_to_integers(floats)
print("Вхідний список:", floats)
print("Список цілих чисел (з округленням):", result)
