#
 Добрый день!
 
В моём проекте установлено ожидание (timeout=5).
Вы сможете его изменить при необходимости. 
Параметр располагается в /pages/base_page.py -> def __init__(...timeout=5):

 В conftest.py установлены default webdriver "Chrome()" и language "en".
Если Вы используете webdriver Firefox(), то для удобства рекомендуется изменить
значение parser.addoption(...default='firefox'...), для использования его по умолчанию.
Или же при запуске теста в командной строке добавить параметр browser_name=firefox

Спасибо за внимание.
