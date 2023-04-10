from itertools import count
from statistics import mean
import os

import requests
from terminaltables import AsciiTable
from dotenv import load_dotenv

PROGRAMMING_LANGUAGES = ['JavaScript', 'Python', 'Java', 'Typescript',
                         'C#', 'C++', 'PHP', 'Shell', 'C', 'Ruby']


def predict_salary(salary_from, salary_to):
    if salary_from and salary_to:
        return (salary_from + salary_to) / 2
    if salary_from:
        return salary_from * 1.2
    if salary_to:
        return salary_to * 0.8
    return None


def predict_rub_salary_hh(vacancy):
    salary = vacancy.get('salary')
    if not salary or salary['currency'] != 'RUR':
        return None
    salary_from = salary.get('from')
    salary_to = salary.get('to')
    return predict_salary(salary_from, salary_to)


def get_vacancies_headhunter():
    api_endpoint = 'https://api.hh.ru/vacancies'
    api_page_constraint = 100
    vacancies_area = '1'
    vacancies_processing_period = 30
    popular_vacancy = {}
    for language in PROGRAMMING_LANGUAGES:
        language_vacancies = []
        for page in count(0):
            if page >= api_page_constraint:
                break
            params = {
                'text': f'Программист {language}',
                'area': vacancies_area,
                'period': vacancies_processing_period,
                'page': page
            }
            response = requests.get(api_endpoint, params=params)
            response.raise_for_status()
            page_vacancies = response.json()['items']
            language_vacancies.extend(page_vacancies)

        salaries = [salary for vacancy in language_vacancies if
                    (salary := predict_rub_salary_hh(vacancy))]
        vacancies_processed = len(salaries)
        average_salary = int(mean(salaries)) if vacancies_processed else '-'
        popular_vacancy[language] = {
            'vacancies_found': len(language_vacancies),
            'vacancies_processed': vacancies_processed,
            'average_salary': average_salary
        }
    return popular_vacancy


def predict_rub_salary_sj(vacancy):
    if not (vacancy['payment_from'] and vacancy['payment_to']) or vacancy['currency'] != 'rub':
        return None
    salary_from = vacancy['payment_from']
    salary_to = vacancy['payment_to']
    return predict_salary(salary_from, salary_to)


def get_vacancies_superjob(api_key):
    api_endpoint = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {
        'X-Api-App-Id': api_key
    }
    api_page_constraint = 5
    vacancies_area = 4
    search_directory = 48
    number_vacancies_on_page = 100
    popular_vacancy = {}
    for language in PROGRAMMING_LANGUAGES:
        language_vacancies = []
        for page in count():
            if page >= api_page_constraint:
                break
            params = {
                'keyword': f'Программист {language}',
                'town': vacancies_area,
                'catalogues': search_directory,
                'page': page,
                'count': number_vacancies_on_page
            }
            response = requests.get(api_endpoint, params=params, headers=headers)
            response.raise_for_status()
            page_vacancies = response.json().get('objects')
            language_vacancies.extend(page_vacancies)

        salaries = [salary for vacancy in language_vacancies if
                    (salary := predict_rub_salary_sj(vacancy))]
        vacancies_processed = len(salaries)
        average_salary = int(mean(salaries)) if vacancies_processed else '-'

        popular_vacancy[language] = {
            'vacancies_found': len(language_vacancies),
            'vacancies_processed': vacancies_processed,
            'average_salary': average_salary
        }
    return popular_vacancy


def print_table(vacancies, site):
    titles = ['Язык программирования', 'Вакансий найдено', 'Вакансий обработано',
              'Средняя зарплата']
    title_table = f'{site} Moscow'
    table_completion = [titles]

    for key, value in vacancies.items():
        field_data = [key] + list(value.values())
        table_completion.append(field_data)

    table_instance = AsciiTable(table_completion, title_table)
    print(table_instance.table)


if __name__ == '__main__':
    load_dotenv()
    api_key = os.environ['SUPERJOB_APIKEY']
    print_table(get_vacancies_headhunter(), 'HeadHunter')
    print()
    print_table(get_vacancies_superjob(api_key), 'SuperJob')
