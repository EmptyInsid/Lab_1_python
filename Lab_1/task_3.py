#задание 3: Разделение игроков на две команды

list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

count_of_players = len(list_players)
half_players = count_of_players // 2

command_one = list_players[:half_players]
command_two = list_players[half_players:]

print(command_one)
print(command_two)
