import psycopg2

CONN = psycopg2.connect(
            host="localhost",
            database="vacancies",
            user="postgres",
            password="12345")

CUR = CONN.cursor()

class PostgreSQL:

    def commit_table():
        CONN.commit()


    def create_tables():
        CUR.execute("CREATE TABLE employees"
                    "(employer_id int PRIMARY KEY,"
                    "name varchar(50) NOT NULL,"
                    "description text,"
                    "area varchar(20),"
                    "open_vacancies int);");

        CUR.execute("CREATE TABLE vacancies"
                    "(vacancy_id int PRIMARY KEY,"
                    "employer_id int REFERENCES employees(employer_id),"
                    "title text,"
                    "salary_from int,"
                    "salary_to int,"
                    "requirement text,"
                    "responsibility text,"
                    "url text);");


    def full_table_e(employer_id, name, description, area, open_vacancies):
        CUR.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s)",
                    (employer_id, name, description, area, open_vacancies))


    def full_table_v(vacancy_id, employer_id, name, salary_from, salary_to, requirement, responsibility, url):
        CUR.execute("INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                    (vacancy_id, employer_id, name, salary_from, salary_to, requirement, responsibility, url))


    def drop_tables():
        CUR.execute("DROP TABLE IF EXISTS employees CASCADE;"
                    "DROP TABLE IF EXISTS vacancies")


class DBManager:
    def get_companies_and_vacancies_count():
        """
        Получает список всех компаний и количество вакансий у каждой компании
        """
        CUR.execute("SELECT name, open_vacancies FROM employees "
                    "ORDER BY name")
        rows = CUR.fetchall()
        for row in rows:
            print(row)


    def get_all_vacancies():
        """
        Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
        """
        CUR.execute("SELECT name, title, salary_from, salary_to, url FROM employees, vacancies "
                    "ORDER BY name")
        rows = CUR.fetchall()
        for row in rows:
            print(row)


    def get_avg_salary():
        """
        Получает среднюю зарплату по вакансиям
        """
        CUR.execute("SELECT AVG (salary_from) as avg_salary FROM vacancies")
        rows = CUR.fetchall()
        for row in rows:
            print(row)

    def get_vacancies_with_higher_salary():
        """
        Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям
        """
        CUR.execute("SELECT name, title, salary_from, salary_to, url FROM vacancies, employees "
                    "WHERE salary_from > (SELECT AVG (salary_from) FROM vacancies)"
                    "ORDER BY salary_from")
        rows = CUR.fetchall()
        for row in rows:
            print(row)

    def get_vacancies_with_keyword(keyword):
        """
        Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python
        """
        CUR.execute("SELECT name, title, salary_from, salary_to, url FROM vacancies, employees "
                    f"WHERE title LIKE '%{keyword}%'")
        rows = CUR.fetchall()
        for row in rows:
            print(row)

