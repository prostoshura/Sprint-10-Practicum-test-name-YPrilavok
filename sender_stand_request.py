import BODY  # импортируем данные из BODY
import URL_PATH  # импортируем данные из URL_PATH
import requests  # импортируем библиотеку requests


def post_new_user(body):  # Функция для изменения значения в параметре body в теле запроса
    return requests.post(URL_PATH.URL_SERVICE+URL_PATH.CREATE_USER_PATH,
                         json=BODY.new_user_body,  # указываем тело запроса
                         headers=BODY.headers)  # указываем заголовок запроса


# В переменную response сохраняется результат запроса на создание нового пользователя
response = post_new_user(BODY.new_user_body)
# Проверяется полный ответ на запрос
print(response.json())


def post_new_client_kit(kit_body, authToken):  # Функция для изменения значения в параметре kit_body в теле запроса
    headers_dict = BODY.Authorization_code.copy()
    headers_dict = {"Content-Type": "application/json",
    "Authorization": "Bearer ddf42b13-385c-4024-a198-9c3b7c52fca5"}
    return requests.post(URL_PATH.URL_SERVICE+URL_PATH.CREATE_USER_MAIN_KITS,  # указываем данные запроса - URL и путь
                         json=kit_body,  # указываем тело запроса
                         headers=headers_dict)


# В переменную response сохраняется результат запроса на создание нового набора
response = post_new_client_kit(BODY.post_new_client_kit, BODY.Authorization_code)
# Проверяется полный ответ на запрос
print(response.json())
