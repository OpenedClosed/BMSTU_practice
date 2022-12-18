import datetime


def gift_count(budget, month, birthdays):
    birthdays_this_month = {
        key: val for key, val in birthdays.items() if val.month == month}
    birthdays_list = [
        '{} ({})'.format(
            key, datetime.datetime.strftime((val), "%d.%m.%Y"))
            for key, val in birthdays_this_month.items()
        ]
    birthdays_string = ', '.join(birthdays_list)
    if len(birthdays_this_month) != 0:
        amount_of_money = budget // len(birthdays_this_month)
        answer = (
            f'Именинники в месяце {month}: {birthdays_string}. '
            f'При бюджете {budget} они получат по {amount_of_money} рублей.'
        )
    else:
        answer = 'В этом месяце нет именинников.'
    print(answer)

if __name__ == "__main__":
    birthdays = {
        "Иванов Иван Иванович": datetime.date(1989, 5, 1),
        "Петров Петр Петрович": datetime.date(1998, 5, 6)
    }
    gift_count(20000, 5, birthdays)