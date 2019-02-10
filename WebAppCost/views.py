from flask import render_template, request, redirect, url_for, abort, flash
from app import app
from models import Users, Expenses
from data import add_expense, get_curr_cost
import datetime
# from forms import *


@app.route('/')
def index():
    exp_data = Expenses().select().join(Users)
    user_data_all = []
    for row in exp_data:
        user_data_all.append({"name": row.user.name, "date": row.date.strftime('%Y-%m-%d'), "cost": row.cost})
    currentfv_cost = get_curr_cost()
    return render_template('index.html', exp_data=user_data_all, current_fvcost=currentfv_cost)


@app.route('/stats', methods=['GET', 'POST'])
def stats():
    users_data = Users().select()
    user_data_all = []
    if request.method == 'POST':
        res = request.form
        if not res['User'] or not res['Cost']:
            print('throwing error')
            print(res)
        else:
            add_expense(res['User'], 'T-mobile', res['Cost'])
            flash('write {0}'.format('OK'))
            return redirect(url_for('stats'))
    elif request.method == 'GET':
        exp_data = Expenses().select().join(Users)

        for row in exp_data:
            print(row)
            user_data_all.append({"name": row.user.name, "date": row.date.strftime('%Y-%m-%d'), "cost": row.cost})
            print(user_data_all)
    return render_template('stats.html', user_data=users_data, exp_data=user_data_all)


@app.route('/expenses', methods=['GET'])
def expenses():
    users_data = Users().select()

    for name in users_data:
        print(name.name)
    #if not pytania.count():
        #flash('Brak pytań w bazie.', 'kom')
        #return redirect(url_for('index'))

    return render_template('expenses.html')