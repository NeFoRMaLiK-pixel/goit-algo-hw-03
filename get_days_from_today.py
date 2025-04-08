from datetime import datetime

def get_days_from_today(date):
    if isinstance(date, str):
        try:
            input_date = datetime.strptime(date, '%Y-%m-%d').date()
            today_date = datetime.today().date()
            delta = today_date - input_date
            return delta.days
        except ValueError:
            return "Ошибка: Неверный формат даты. Используйте формат 'ГГГГ-ММ-ДД'."
    else:
        return "Ошибка: Дата должна быть строкой в формате 'ГГГГ-ММ-ДД'."

print(get_days_from_today('2025-05-01'))
print(get_days_from_today('2025-03-10'))
    