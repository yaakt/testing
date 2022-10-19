import datetime as dt


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount =  float(amount)
        self.comment = str(comment)
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()

class Calculator:
    def __init__(self, limit):
        self.limit = limit #дневной лимит трат или калорий
        self.records = [] #хранение записей
        self.current_date = dt.date.today()
        self.days_ago = self.current_date - dt.timedelta(7)

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        day_stats = []
        for record in self.records:
            if record.date == self.current_date:
                day_stats.append(record.amount)
        return sum(day_stats)
    def get_week_stats(self):
        week_stats = []
        for record in self.records:
            if self.days_ago <= record.date <= self.current_date:
                week_stats.append(record.amount)
        return sum(week_stats)


class CashCalculator(Calculator):
    rub = 1
    dollar = 60.73
    euro = 59.79
    def get_today_cash_remained(self, currency):
        currencies = {'usd': ('dollars', self.dollar), 'eur': ('euros', self.euro),
                       'rub': ('руб', self.rub)}
        delta_cash = self.limit - self.get_today_stats()
        if delta_cash == 0:
            message = f'No money left'
        name, rate = currencies.get(currency)
        delta_cash = delta_cash / rate
        if delta_cash > 0:
            message = f'You can spend {delta_cash} {name}'
        else:
            delta_cash = abs(delta_cash)
            message = f'No money left, your debt is {delta_cash} {name}'
        return message

class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        delta_calories = self.limit-self.get_today_stats()
        if delta_calories > 0:
            message = f'You can eat {delta_calories} calories'
        else:
            message = f'Limit is over'
        return message

cash_calculator = CashCalculator(1000)
cash_calculator.add_record(Record(amount=145, comment='кофе'))
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000,comment='бар в Танин др',date='08.11.2019'))

print(cash_calculator.get_today_cash_remained(currency='rub'))
# должно напечататься
# На сегодня осталось 555 руб
