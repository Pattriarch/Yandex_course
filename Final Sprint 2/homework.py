import datetime as dt


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.datetime.today().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, object_record):
        self.records.append(object_record)

    def get_today_stats(self):
        today = dt.datetime.today().date()
        return sum(i.amount for i in self.records if i.date == today)

    def get_week_stats(self):
        week = (dt.datetime.today() - dt.timedelta(days=7)).date()
        today = (dt.datetime.today()).date()
        result = 0
        for i in self.records:
            if week < i.date <= today:
                result += i.amount
        return result

    def get_today_spent(self):
        return self.limit - self.get_today_stats()


class CashCalculator(Calculator):
    USD_RATE = 60.00
    EURO_RATE = 70.00
    RUB_RATE = 1

    dictionary_of_currencies = {"usd": (USD_RATE, 'USD'),
                                "eur": (EURO_RATE, 'Euro'),
                                "rub": (RUB_RATE, 'руб')}

    def __init__(self, limit):
        super().__init__(limit)

    def get_today_cash_remained(self, currency):
        if currency in self.dictionary_of_currencies:
            divider = self.dictionary_of_currencies[currency][0]
            name_of_currency = self.dictionary_of_currencies[currency][1]
            user_spend = self.get_today_spent()
            if user_spend > 0:
                return f"На сегодня осталось {round(user_spend / divider, 2)} {name_of_currency}"
            elif user_spend == 0:
                return "Денег нет, держись"
            return f"Денег нет, держись: твой долг - {round(abs(user_spend / divider), 2)} {name_of_currency}"


class CaloriesCalculator(Calculator):

    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        calories = self.get_today_spent()
        if calories > 0:
            return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {calories} кКал"
        else:
            return "Хватит есть!"
        pass


if __name__ == '__main__':
    # Тест калькулятора калорий
    calories_calculator = CaloriesCalculator(2200)
    calories_calculator.add_record(Record(amount=700, comment='Булгур с овощами и белыми грибами.'))
    print(calories_calculator.get_calories_remained())
    calories_calculator.add_record(Record(amount=240, comment='Салат с ростбифом'))
    print(calories_calculator.get_calories_remained())
    calories_calculator.add_record(Record(amount=1180, comment='Вафли с жировыми начинками'))
    print(calories_calculator.get_calories_remained())
    calories_calculator.add_record(Record(amount=350, comment='Желе'))
    print(calories_calculator.get_calories_remained())

    # Тест калькулятора денежных расходов
    print()
    cash_calculator = CashCalculator(1000)
    cash_calculator.add_record(Record(amount=120, comment='Метро'))
    print(cash_calculator.get_today_cash_remained("rub"))
    print(cash_calculator.get_today_cash_remained("usd"))
    print(cash_calculator.get_today_cash_remained("eur"))
    print()
    cash_calculator.add_record(Record(amount=110, comment='Кофе'))
    cash_calculator.add_record(Record(amount=80, comment='Кусок торта'))
    print(cash_calculator.get_today_cash_remained("rub"))
    cash_calculator.add_record(Record(amount=500, comment='Занял Диме денег'))
    print(cash_calculator.get_today_cash_remained("rub"))
    cash_calculator.add_record(Record(amount=190, comment='Шампунь'))
    print(cash_calculator.get_today_cash_remained("rub"))
    cash_calculator.add_record(Record(amount=270, comment='Комплексный обед в ВУЗе'))
    print(cash_calculator.get_today_cash_remained("rub"))



