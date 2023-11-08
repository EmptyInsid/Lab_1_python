#Задание №1: Найти сумму произведений из списка словарей
import json


def sum_of_mul_score_weight() -> float:
    """Поиск суммы произведений значений score и weight"""
    filename = "input.json"

    with open(filename, "r", encoding='utf-8') as in_file:
        json_data = json.load(in_file)

    first_arg = "score"
    second_arg = "weight"
    ans = sum([data[first_arg] * data[second_arg] for data in json_data])
    return round(ans, 3)


print(sum_of_mul_score_weight())
