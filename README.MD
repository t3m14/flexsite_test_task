Высылаю тестовое задание

====ТЕСТОВОЕ ЗАДАНИЕ:====

Создать Django REST framework приложение, с переопределённым пользователем и списком организаций в которых он состоит.

Две модели

Пользователь:
- Емайл 
- Пароль
- Фамилия
- Имя
- Телефон
- Аватар(фотография).
- Связь на список организаций(может быть больше одной)
*Базовые (технические) поля django, кроме логина, он не должен использоваться

Организация:
- Название
- Краткое описание

Функционал:
// все запросы делаются через через curl/postman/вебинтерфейс DRF, по RestAPI. Формат данных передаётся в json.

Создание нового пользователя(регистрация)
Авторизация пользователя только по емайлу и паролю
Редактирование своего профиля (изменение данных в профиле)
Вывод списка всех пользователей и связанные с ними организации
Вывод одного пользователя по его ID, со списком связанных с ним организаций
Добавление новой организации
Вывод списка всех организаций

Дополнительный функционал, по желанию:

Вывод списка всех организаций(п.6 выше), со списком пользователей, которые связаны с каждой из них.
Аватар/фотография пользователя, картинка должна при загрузке переименовываться [a-zA-Z0-9]. А так же resize(уменьшить) до размеров не больше 200х200 px.
Авторизация пользователя должна происходить через JWT, передача приватных данных(изменения профиля), происходят через этот токен. Можно использовать отдельную библиотеку.
Добавить unit-test

Требования:

Python 3.8+
Проект должен быть залит на Github/Bitbucket и быть публичным.
Проект должен быть в виртуальном окружении venv. Должен присутствовать файл со списком используемых в проекте пакетов и их версий.
База данных по умолчанию от django: sqlite3
Описание какие методы есть, какие параметры они принимают, какие отдают.

====КОНЕЦ ТЕСТОВОГО ЗАДАНИЯ====