from datetime import datetime
import Calc
import pytest


@pytest.fixture()
def test_cash_calculator_add_records():
    record = Calc.Record(amount=300, comment='Серёге за обед')
    Calc.CashCalculator.add_record(record)
    assert len(Calc.CashCalculator.records) == 1

@pytest.fixture()
def cash_calc():
    cash_calculator = Calc.CashCalculator(1000)
    cash_calculator.add_record(Calc.Record(amount=145, comment='кофе'))
    cash_calculator.add_record(Calc.Record(amount=300, comment='Серёге за обед'))
    cash_calculator.add_record(Calc.Record(amount=3000, comment='бар в Танин др', date='08.11.2019'))
    return cash_calculator.get_today_cash_remained(currency='rub')
def test_CashCalculator(cash_calc):
    assert cash_calc == 'You can spend 555.0 руб'

the_list = [{'amount': 145, 'comment': 'кофе','date':'08.11.2019'},
             {'amount': 300, 'comment': 'Серёге за обед'},
             {'amount': 3000,'comment': 'бар в Танин др','date':'08.11.2019'}]


@pytest.mark.parametrize("list_", the_list)
def test__init__(list_):
    result = Calc.Record(**list_)
    if 'date' in list_:
        assert result.date == datetime .strptime(list_['date'], '%d.%m.%Y').date()
    else:
        assert result.date == datetime .now().date()