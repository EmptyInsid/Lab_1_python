#задание 4: Статистика посещений сайта

users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

statistics_visits = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

statistics_visits["Общее количество"] = len(users)
statistics_visits["Уникальные посещения"] = len(set(users))

print(statistics_visits)
