import requests


# Задача 1
def get_power_stats(hero_list, url_all, url_power_stats, power_stats):
    resp_all = requests.get(url=url_all)
    if resp_all.status_code != 200: return 'Error'  # проверка, что получен статус 200
    resp_all = resp_all.json()
    id_dict = {}
    for hero in resp_all:  # создаём словарь имя героя - его id
        id_dict[hero['name']] = hero['id']

    hero_power_stats = {}
    for hero in hero_list:  # создаём словарь имя героя из списка - его power_stats
        url_hero_power_stats = url_power_stats + str(id_dict[hero]) + '.json'
        resp = requests.get(url=url_hero_power_stats)
        if resp.status_code != 200: return 'Error'  # проверка, что получен статус 200
        resp = resp.json()
        hero_power_stats[hero] = resp[power_stats]
    max_power_stats_hero = max(hero_power_stats, key=hero_power_stats.get)  # поиск героя с максимальным power_stats
    return max_power_stats_hero


print('Задача 1')
url_all = 'https://akabab.github.io/superhero-api/api/all.json'  # ссылка на json по всем героям
url_power_stats = 'https://akabab.github.io/superhero-api/api/powerstats/'  # ссылка на json по power_stats по id
hero_list = ['Hulk', 'Captain America', 'Thanos']  # список героев для анализа
power_stats = 'intelligence'  # показатель power_stats для сравнения
result_hero = get_power_stats(hero_list, url_all, url_power_stats, power_stats)
if result_hero != 'Error':  # обработка случая, если какой-то запрос не вернул статус 200
    print(f'''Даны герои: {hero_list}.
Герой с самым сильным показателем {power_stats} - {result_hero}''')
else:
    print('Error')
