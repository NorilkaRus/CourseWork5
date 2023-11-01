from parsing_utils import *
from postgresql_utils import *


#Список компаний (их id)
employees_id = [740, 78638, 1122462, 5385759, 4352, 3805, 1095544, 23427, 2180, 2071925]

PostgreSQL.drop_tables()
PostgreSQL.create_tables()


#Создаем список экземпляров работодателей
employees = []
for id in employees_id:
    employees.append(Employer.create_employer(id))


#Заполняем таблицы PostgreSQL
for e in employees:
    PostgreSQL.full_table_e(e.id, e.name, e.description, e.area, e.open_vacancies)
    headers = {'User-Agent': 'Norilka'}
    parametres_vacancies = {'employer_id' : e.id, 'per_page': 100}
    vacancies = requests.get(url_vacancies, headers=headers, params=parametres_vacancies).json()
    for vacancy in vacancies['items']:
        v = Vacancy.create_vacancy(vacancy)
        url = f"https://rostov.hh.ru/vacancy/{v.url}"
        PostgreSQL.full_table_v(v.url, e.id, v.name, v.salary_from, v.salary_to, v.requirement, v.responsibility, url)

PostgreSQL.commit_table()

#Начинаем взаимодействие с пользователем:
print("База данных работодателей и вакансий сформирована.")
while True:
    try:
        command = int(input("""
            1. Получить список всех компаний и количество вакансий у каждой компании;
            2. Получить список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию;
            3. Получить среднюю зарплату по вакансиям;
            4. Получить список всех вакансий, у которых зарплата выше средней по всем вакансиям;
            5. Получить список всех вакансий по ключевому слову;
            6. Закрыть программу.
            Введите команду: """))
    except ValueError:
        print("Команда должна быть цифрой от 1 до 6")
        continue

    if command == 1:
        DBManager.get_companies_and_vacancies_count()
    elif command == 2:
        DBManager.get_all_vacancies()
    elif command == 3:
        DBManager.get_avg_salary()
    elif command == 4:
        DBManager.get_vacancies_with_higher_salary()
    elif command == 5:
        keyword = input("Введите ключевое слово: ")
        DBManager.get_vacancies_with_keyword(keyword)
    elif command == 6:
        break

