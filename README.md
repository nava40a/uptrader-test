# Тестовое задание для Uptrader

## Установка
1. Склонируйте репозиторий  ```git@github.com:nava40a/uptrader-test.git```
2. Создайте и активируйте виртуальное окружение: ```python -m venv venv``` ```source venv\Scripts\activate```
3. Установите зависимости: ```pip install -r requirements.txt```

### Запуск
1. Примените миграции ```python manage.py migrate```
2. Загрузите данные в базу ```python manage.py loaddata initial_data.json```
3. Запустите проект: ```python manage.py runserver```
4. Проект доступен по адресу: ```http://127.0.0.1:8000/```
5. Данные для входа в админку: ```username: admin``` ```password: admin```
