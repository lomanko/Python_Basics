import requests
from datetime import datetime
from datetime import timedelta
import pandas as pd


class StackOverflow:

    def get_questions_data(self, period, tag, field='title'):
        '''
        Функция принимает на вход:
        - period - глубина запроса в днях (количество суток с текущего момента)
        - tag - тег, который должен быть в вопросе
        - field - интересующее поле (по умолчанию - заголовок вопроса)
        Функция возвращает dataframe из даты и поля field.
        '''
        url = "https://api.stackexchange.com/2.3/questions"
        todate = int(datetime.today().timestamp())  # текущий момент
        fromdate = int((datetime.today() - timedelta(days=period)).timestamp())  # текущий момент period дней назад
        params = {"fromdate": fromdate, "todate": todate, "tagged": tag,
                  "order": 'desc', "sort": 'creation', "site": 'stackoverflow', "pagesize": 100, "page": 1}
        response_dict = {}  # словарь для накопления
        while True:
            response = requests.get(url, params=params)
            if response.status_code != 200: return 'Error'  # проверка, что получен статус 200
            response = requests.get(url, params=params).json()
            for item in response['items']:  # записываем в словарь дату создания вопроса и параметр field
                response_dict[datetime.fromtimestamp(item['creation_date'])] = item[field]
            if not response['items']:  # если пусто, значит страницы кончились
                break
            else:
                params['page'] += 1  # в противном случае переходим на следующую страницу

        result_df = pd.DataFrame.from_dict(response_dict, orient='index', columns=[field])  # преобразуем в dataframe

        return result_df


questions = StackOverflow()
print(questions.get_questions_data(2, 'python'))
