# README.md

## Salary Prediction Program

This program predicts the average salary for programming jobs in Moscow based on data obtained from HeadHunter and SuperJob. The program uses the following programming languages: JavaScript, Python, Java, Typescript, C#, C++, PHP, Shell, C, Ruby.

### Dependencies

* requests
* terminaltables
* python-dotenv
* statistics

### Setup

1. Clone this repository to your local machine.
2. Create a virtual environment: python3 -m venv env
3. Activate the virtual environment: source env/bin/activate
4. Install dependencies: pip install -r requirements.txt
5. Create a .env file in the root directory of the project and add your SuperJob API key:
```
SUPERJOB_APIKEY=<your_superjob_api_key>
```

### Usage

To run the program, execute the following command in the terminal:
```
python main.py
```

The program will then output two tables: one for HeadHunter and another for SuperJob. The tables contain the following columns:
* Programming language
* Number of vacancies found
* Number of vacancies processed
* Average salary

### Example Output
```
+----------------------+------------------+----------------------+-----------------+
| Язык программирования | Вакансий найдено | Вакансий обработано | Средняя зарплата |
+----------------------+------------------+----------------------+-----------------+
| JavaScript           | 1972             | 929                  | 152131          |
| Python               | 1464             | 856                  | 164728          |
| Java                 | 1785             | 676                  | 169645          |
| Typescript           | 676              | 340                  | 173488          |
| C#                   | 762              | 337                  | 174154          |
| C++                  | 478              | 246                  | 166893          |
| PHP                  | 731              | 334                  | 137038          |
| Shell                | 95               | 57                   | 173247          |
| C                    | 97               | 64                   | 144734          |
| Ruby                 | 270              | 158                  | 162622          |
+----------------------+------------------+----------------------+-----------------+

SuperJob Moscow
+----------------------+------------------+----------------------+-----------------+
| Язык программирования | Вакансий найдено | Вакансий обработано | Средняя зарплата |
+----------------------+------------------+----------------------+-----------------+
| JavaScript           | 45               | 7                    | 57285           |
| Python               | 42               | 11                   | 72500           |
| Java                 | 56               | 20                   | 84000           |
| Typescript           | 5                | 2                    | 60000           |
| C#                   | 15               | 4                    | 105000          |
| C++                  | 8                | 3                    | 91000           |
| PHP                  | 9                | 3                    | 66666           |
| Shell                | 1                | 1                    | 70000           |
| C                    | 3                | 2                    | 37500           |
| Ruby                 | 10               | 4                    | 81250           |
+----------------------+------------------+----------------------+-----------------+
```

### License
This program is licensed under the MIT License. See the LICENSE file
