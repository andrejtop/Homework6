from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date


# today = date.today()
# print(f'Сегодня {today}')

if __name__ == '__main__':
    print(date.today())
    calculate_salary()
    get_employees()