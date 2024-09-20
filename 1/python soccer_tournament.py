import random

# Определение рейтингов команд
team_strength = {
    'Германия': 90,
    'Шотландия': 70,
    'Венгрия': 60,
    'Швейцария': 75,
    'Испания': 85,
    'Хорватия': 80,
    'Италия': 85,
    'Албания': 55,
    'Дания': 75,
    'Англия': 90,
    'Словения': 65,
    'Сербия': 70,
    'Франция': 90,
    'Нидерланды': 85,
    'Австрия': 70,
    'Польша': 75,
    'Бельгия': 85,
    'Словакия': 60,
    'Румыния': 65,
    'Украина': 70,
    'Турция': 70,
    'Грузия': 55,
    'Португалия': 85,
    'Чехия': 65
}

# Определение команд по группам
groups = {
    'A': ['Германия', 'Шотландия', 'Венгрия', 'Швейцария'],
    'B': ['Испания', 'Хорватия', 'Италия', 'Албания'],
    'C': ['Дания', 'Англия', 'Словения', 'Сербия'],
    'D': ['Франция', 'Нидерланды', 'Австрия', 'Польша'],
    'E': ['Бельгия', 'Словакия', 'Румыния', 'Украина'],
    'F': ['Турция', 'Грузия', 'Португалия', 'Чехия']
}

# Функция для генерации случайного результата матча с учетом рейтингов команд
def simulate_match(team1, team2):
    strength1 = team_strength[team1] ** 1.5
    strength2 = team_strength[team2] ** 1.5
    
    total_strength = strength1 + strength2
    
    prob_team1_wins = strength1 / total_strength
    
    random_value = random.random()
    if random_value < prob_team1_wins:
        score1 = random.randint(2, 4)
        score2 = random.randint(0, score1 - 1)
    else:
        score2 = random.randint(2, 4)
        score1 = random.randint(0, score2 - 1)
    
    return (team1, score1), (team2, score2)

# Функция для симуляции серии пенальти
def simulate_penalty_shootout(team1, team2):
    goals_team1 = 0
    goals_team2 = 0
    # Имитация серии пенальти, например, каждая команда бьет по 5 пенальти
    for _ in range(5):
        if random.random() < 0.5:  # Вероятность забить пенальти
            goals_team1 += 1
        if random.random() < 0.5:
            goals_team2 += 1
    # Если пенальти закончились в ничью, добавим по одному пенальти до победы одной из команд
    while goals_team1 == goals_team2:
        if random.random() < 0.5:
            goals_team1 += 1
        else:
            goals_team2 += 1
    return goals_team1, goals_team2

# Генерация результатов для всех матчей в группах
results = {}

for group, teams in groups.items():
    results[group] = []
    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):
            match_result = simulate_match(teams[i], teams[j])
            results[group].append(match_result)

# Подсчет очков в группах
group_points = {group: {team: 0 for team in teams} for group, teams in groups.items()}

for group, matches in results.items():
    for match in matches:
        (team1, score1), (team2, score2) = match
        if score1 > score2:
            group_points[group][team1] += 3
        elif score1 < score2:
            group_points[group][team2] += 3
        else:
            group_points[group][team1] += 1
            group_points[group][team2] += 1

# Определение мест в группах
group_rankings = {}
for group, points in group_points.items():
    group_rankings[group] = sorted(points.items(), key=lambda item: item[1], reverse=True)

# Определение команд, прошедших в плей-офф
playoff_teams = []
third_place_teams = []

for group, rankings in group_rankings.items():
    playoff_teams.append(rankings[0][0])
    playoff_teams.append(rankings[1][0])
    third_place_teams.append(rankings[2])

# Определение лучших 4 команд, занявших третьи места
third_place_teams = sorted(third_place_teams, key=lambda item: item[1], reverse=True)[:4]
playoff_teams.extend([team[0] for team in third_place_teams])

# Функция для симуляции результатов плей-офф с учетом рейтингов команд
def simulate_playoff_match(team1, team2):
    # Среднее количество голов в матче
    average_goals = 2.7
    
    # Генерация случайного числа голов с использованием среднего и дополнительной случайности
    goals_team1 = round(random.triangular(0, average_goals, average_goals * 2))
    goals_team2 = round(random.triangular(0, average_goals, average_goals * 2))
    
    return (team1, goals_team1), (team2, goals_team2)

# Плей-офф матчи
playoff_results = {}

# 1/8 финала
playoff_pairs = [
    (playoff_teams[0], playoff_teams[15]),
    (playoff_teams[1], playoff_teams[14]),
    (playoff_teams[2], playoff_teams[13]),
    (playoff_teams[3], playoff_teams[12]),
    (playoff_teams[4], playoff_teams[11]),
    (playoff_teams[5], playoff_teams[10]),
    (playoff_teams[6], playoff_teams[9]),
    (playoff_teams[7], playoff_teams[8])
]

playoff_results['1/8'] = []
for pair in playoff_pairs:
    team1, team2 = pair
    score_team1, score_team2 = simulate_playoff_match(team1, team2)
    if score_team1[1] == score_team2[1]:  # Если ничья, проводим серию пенальти
        penalty_score_team1, penalty_score_team2 = simulate_penalty_shootout(team1, team2)
        playoff_results['1/8'].append((team1, team2, score_team1, score_team2, penalty_score_team1, penalty_score_team2))
    else:
        playoff_results['1/8'].append((team1, team2, score_team1, score_team2))

# 1/4 финала
quarterfinalists = [match[0] if match[2][1] > match[3][1] else match[1] for match in playoff_results['1/8']]
playoff_pairs = [
    (quarterfinalists[0], quarterfinalists[3]),
    (quarterfinalists[1], quarterfinalists[2]),
    (quarterfinalists[4], quarterfinalists[7]),
    (quarterfinalists[5], quarterfinalists[6])
]

playoff_results['1/4'] = []
for pair in playoff_pairs:
    team1, team2 = pair
    score_team1, score_team2 = simulate_playoff_match(team1, team2)
    if score_team1[1] == score_team2[1]:
        penalty_score_team1, penalty_score_team2 = simulate_penalty_shootout(team1, team2)
        playoff_results['1/4'].append((team1, team2, score_team1, score_team2, penalty_score_team1, penalty_score_team2))
    else:
        playoff_results['1/4'].append((team1, team2, score_team1, score_team2))

# 1/2 финала
semifinalists = [match[0] if match[2][1] > match[3][1] else match[1] for match in playoff_results['1/4']]
playoff_pairs = [
    (semifinalists[0], semifinalists[1]),
    (semifinalists[2], semifinalists[3])
]

playoff_results['1/2'] = []
for pair in playoff_pairs:
    team1, team2 = pair
    score_team1, score_team2 = simulate_playoff_match(team1, team2)
    if score_team1[1] == score_team2[1]:
        penalty_score_team1, penalty_score_team2 = simulate_penalty_shootout(team1, team2)
        playoff_results['1/2'].append((team1, team2, score_team1, score_team2, penalty_score_team1, penalty_score_team2))
    else:
        playoff_results['1/2'].append((team1, team2, score_team1, score_team2))

# Финал
finalists = [match[0] if match[2][1] > match[3][1] else match[1] for match in playoff_results['1/2']]
team1, team2 = finalists
score_team1, score_team2 = simulate_playoff_match(team1, team2)
if score_team1[1] == score_team2[1]:
    penalty_score_team1, penalty_score_team2 = simulate_penalty_shootout(team1, team2)
    playoff_results['Финал'] = [(team1, team2, score_team1, score_team2, penalty_score_team1, penalty_score_team2)]
else:
    playoff_results['Финал'] = [(team1, team2, score_team1, score_team2)]

# Вывод результатов

# Групповой этап
print("Групповой этап:")
for group, matches in results.items():
    print(f"\nГруппа {group}:")
    for match in matches:
        (team1, score1), (team2, score2) = match
        print(f"{team1} {score1}:{score2} {team2}")

# Результаты групп
print("\nРезультаты групп:")
for group, rankings in group_rankings.items():
    print(f"\nГруппа {group}:")
    for team, points in rankings:
        print(f"{team} - {points} очков")

# Плей-офф
print("\nПлей-офф:")
for stage, matches in playoff_results.items():
    print(f"\n{stage}:")
    for match in matches:
        if len(match) == 4:
            (team1, team2, score1, score2) = match
            print(f"{team1} {score1[1]}:{score2[1]} {team2}")
        else:
            (team1, team2, score1, score2, penalty_score1, penalty_score2) = match
            print(f"{team1} {score1[1]}:{score2[1]} {team2} (Пенальти: {penalty_score1}-{penalty_score2})")









