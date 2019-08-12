from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True)
  email = db.Column(db.String(120), unique=True)

# Use it initially to create the table
db.create_all()
db.session.commit()

# Insert element
admin = User('admin1', 'admin1@example.com')
guest = User('guest1', 'guest1@example.com')
# Insert queries
db.session.add(admin)
db.session.add(guest)
db.session.commit()
# Select operations
print(User.query.filter_by(username='admin').first())
print(User.query.filter_by(username='admin').all())
print(User.query.filter(User.email.endswith('@example.com')).all())
print(User.query.filter(User.email.startswith('a')).all())
print(User.query.filter(User.email.startswith('%admin%')).all())

if __name__ == '__main__':
	app.run(debug=True)