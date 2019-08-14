from app import app
from .models import Scientist , Theory
from flask import render_template


@app.route('/')
def index():
    return 'Hello'

@app.route('/scientist')
def scientist():
    queries = Scientist.query.all()
    return render_template('data.htm' , datas=queries)


