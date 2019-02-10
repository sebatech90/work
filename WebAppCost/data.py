from models import Users, Expenses
import datetime


def add_expense(user_id, expense_name, cost):
    now = datetime.datetime.now()
    curr_month = now.strftime('%Y-%m-%d')
    exp_data = Expenses(user=user_id, name=expense_name, date=curr_month, cost=cost)
    exp_data.save()


def get_curr_cost():
    now = datetime.datetime.now()
    curr_month = now.strftime('%B')
    return curr_month
