from flask_sqlalchemy import SQLAlchemy
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Scientist(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    first_name= db.Column(db.String(200) , nullable=False)
    last_name = db.Column(db.String(100) , nullable=False)
    theory= db.relationship('Theory' , backref='theories' , lazy='dynamic')


    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


    def __repr__(self):
        return f'<Scientist {self.get_full_name}>'


class Theory(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.Text)
    scientist_id = db.Column(db.Integer , db.ForeignKey('scientist.id'))



    def __repr__(self):
        return f'<Theory {self.title}>'

