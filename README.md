# CourseWork5
Программа получает данные о компаниях и вакансиях с сайта hh.ru, проектирует таблицы в БД PostgreSQL и загружает полученные данные в созданные таблицы.
После чего пользователь может отображать полученные результаты различным образом.

Модуль parsing_utils содержит классы методы для осуществления запросов на hh.ru.
Модуль postgresql_utils содержит классы методы для работы с БД PostgreSQL.
Файл main является основной программой, которая импортирует модули и выполняет основной код
