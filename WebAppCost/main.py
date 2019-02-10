import os
from app import app, base
from models import *
from views import *
#from dane import *

if __name__ == '__main__':
    if not os.path.exists(app.config['DATABASE']):
        base.create_tables([Users, Expenses], True)
        #dodaj_pytania(pobierz_dane('pytania.csv'))
    app.run(debug=True)