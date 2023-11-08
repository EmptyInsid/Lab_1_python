#Задание №2: Поиск общих участников
def find_common_participants(first_group_str, second_group_str, separator = ','):
    first_group_set = set(first_group_str.split(separator))
    second_group_set = set(second_group_str.split(separator))

    intersection_group = list(first_group_set.intersection(second_group_set))
    intersection_group.sort()

    return intersection_group


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, '|')
print("Общие участники:", ', '.join(common_participants))
