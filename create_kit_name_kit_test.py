import BODY  # импортируем данные из BODY
import sender_stand_request  # импортируем данные из URL_PATH


def get_post_new_client_kit(name):
    # копирование словаря с телом запроса из файла BODY, чтобы не потерять данные в исходном словаре
    current_client_kit = BODY.post_new_client_kit.copy()
    # изменение значения в поле firstName
    current_client_kit["name"] = name
    return current_client_kit


def positive_assert(name):
    # В переменную post_new_client_kit сохраняется обновленное тело запроса
    post_new_client_kit = get_post_new_client_kit(name)
    # В переменную user_response сохраняется результат запроса на создание набора
    user_response = sender_stand_request.post_new_client_kit(post_new_client_kit)

    # Проверяется, что код ответа равен 201
    assert user_response.status_code == 201
    # Проверяется, что в ответе есть поле authToken, и оно не пустое
    assert user_response.json()["authToken"] != ""
    # Проверяется, что имя в ответе равено имени в запросе
    assert user_response.json()["name"] == post_new_client_kit(name)
    # Проверяется полный ответ на запрос
    print(user_response.json())


def negative_assert(name):
    # В переменную post_new_client_kit сохраняется обновленное тело запроса
    post_new_client_kit = get_post_new_client_kit(name)
    # В переменную user_response сохраняется результат запроса на создание набора
    user_response = sender_stand_request.post_new_client_kit(post_new_client_kit)

    # Проверяется, что код ответа равен 400
    assert user_response.status_code == 400
    # Проверяется, что в ответе есть поле authToken, и оно не пустое
    assert user_response.json()["authToken"] != ""
    # Проверяется полный ответ на запрос
    assert user_response.json()["message"] == "Не все необходимые параметры были переданы"

    # В переменную users_table_response сохраняется результат запроса на создание нового пользователя
    users_table_response = sender_stand_request.post_new_client_kit()
    # Строка, которая должна быть в ответе
    str_user = post_new_client_kit["name"] + "," + post_new_client_kit["card"] + "," + user_response.json()["authToken"]
    # Проверка, что такой пользователь есть, и он единственный
    assert users_table_response.text.count(str_user) == 1


# Допустимое количество символов (1):
def test_create_new_client_kit_1_letter_in_name_get_success_response():
    positive_assert("A")


# Допустимое количество символов (511):
def test_create_new_client_kit_511_letter_in_name_get_success_response():
    post_new_client_kit = get_post_new_client_kit("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabc")


# Количество символов меньше допустимого (0):
def test_create_new_client_kit_0_letter_in_name_get_error_response():
    post_new_client_kit = get_post_new_client_kit("")


# Количество символов больше допустимого (512):
def test_create_new_client_kit_512_letter_in_name_get_error_response():
    post_new_client_kit = get_post_new_client_kit("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc")


# Разрешены английские буквы: "QWErty"
def test_create_new_client_kit_QWErty_letter_in_name_get_success_response():
    post_new_client_kit = get_post_new_client_kit("QWErty")


# Разрешены русские буквы:"Мария"
def test_create_new_client_kit_russian_letter_in_name_get_success_response():
    post_new_client_kit = get_post_new_client_kit("Мария")


# Разрешены спецсимволы:"№%@,"
def test_create_new_client_kit_symbols_letter_in_name_get_success_response():
    post_new_client_kit = get_post_new_client_kit("№%@,")


# Разрешены пробелы:"Человек и КО"
def test_create_new_client_kit_space_letter_in_name_get_success_response():
    post_new_client_kit = get_post_new_client_kit("Человек и КО")


# Разрешены цифры:"123"
def test_create_new_client_kit_numbers_letter_in_name_get_success_response():
    post_new_client_kit = get_post_new_client_kit("123")


# Параметр не передан в запросе:
def test_create_new_client_kit_with_no_body_letter_in_name_get_error_response():
    post_new_client_kit = BODY.post_new_client_kit.copy()
    post_new_client_kit.pop("name")


# Передан другой тип параметра (число):123
def test_create_new_client_kit_with_wrong_type_in_name_get_error_response():
    post_new_client_kit = get_post_new_client_kit(123)
