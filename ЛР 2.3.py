import random

def find_intersection(set1, set2):
    common_elements = set1 & set2
    return common_elements

set_a = set(random.sample(range(1, 20), 8))
set_b = set(random.sample(range(1, 20), 8))

result_set = find_intersection(set_a, set_b)

print("Перша множина:", set_a)
print("Друга множина:", set_b)
print("Спільні елементи в обох множинах:", result_set)
