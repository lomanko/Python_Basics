import requests
import os


# Задача 2
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json',
                'Authorization': 'OAuth {}'.format(self.token)}

    def get_file_name(self, file_path):  # получаем имя файла из ссылки на него
        return os.path.basename(file_path)

    def upload(self, file_path):
        # получаем ссылку для загрузки файла
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": self.get_file_name(file_path), "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        href = response.json().get("href")  # ссылка для загрузки

        # загружаем файл
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")
        else:
            print('Not Success')


print('Задача 2')
path_to_file = 'files/test_upload.txt'
TOKEN = ''  # здесь должен быть токен
uploader = YaUploader(TOKEN)
uploader.upload(path_to_file)
