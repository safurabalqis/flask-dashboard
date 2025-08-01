from flask import Flask, render_template
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from models import db, Sales

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)

@app.route('/')
def dashboard():
    data = Sales.query.all()
    labels = [row.product for row in data]
    values = [row.amount for row in data]
    return render_template('dashboard.html', labels=labels, values=values)

if __name__ == '__main__':
    app.run(debug=True)
