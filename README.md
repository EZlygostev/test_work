# Тестовое задание на должность Python разработчик Junior
## Установка с помощью Docker-сompose:
1) Находясь в каталоге проекта, содержащий файл docker-compose.yml выполнить следующую команду:

```sh
docker-compose up
```
> Перезапустите docker-compose файл, если возникла ошибка при создании контейров.
2) Ожидайте запуска всех контейнеров
> Контейнер API после запуска устанавливает все необходимые зависимости, ожидайте их завершения.

## Postgres DB:
Файл конфигурации доступа данных предоставлен в файле:
```sh
.env
```
Для визуализации БД можно использовать Adminer находяшийся по следующему адресу:
```sh
http://127.0.0.1:8080/
```

## Начало работы:
1) URL для POST метода:
> ```sh
> http://127.0.0.1:80
> ```
> ** для изменения хоста и номера порта, измените файл "run.sh" и "docker-compose.yml"
2) Тело запроса в формате:
> 
> {
>    "questions_num": integer
> }
## Пример запроса:
Запрос:
```sh
import requests
import json

url = "http://127.0.0.1:80"

payload = json.dumps({
  "questions_num": 4
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```
Ответ:
```sh
[
    {
        "before_answer": "Diego Rivera",
        "all_answer": [
            "South America",
            "Alicia Keys",
            "Diego Rivera",
            "bubble gum (or chewing game)"
        ]
    }
]
```
### Примечание:
В целях безопасности необходимо добавить следующие файлы в файл .gitignore во избежания утечки данных:
```sh
./app/.env
.env
```
