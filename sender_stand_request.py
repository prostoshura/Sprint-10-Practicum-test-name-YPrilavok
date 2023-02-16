import BODY
import URL_PATH
import requests


def post_new_user(body):
    return requests.post(URL_PATH.URL_SERVICE+URL_PATH.CREATE_USER_PATH,
                         json=body,
                         headers=BODY.headers_non_authorisation)


response = post_new_user(BODY.new_user_body)
print(response.json())


def post_new_client_kit(kit_body):
    return requests.post(URL_PATH.URL_SERVICE+URL_PATH.CREATE_USER_MAIN_KITS,
                         json=kit_body,
                         headers=BODY.headers_authorised)


response = post_new_client_kit(BODY.post_new_client_kit)
print(response.json())
