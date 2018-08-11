from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/civic_twitter_bot_development'
db = SQLAlchemy(app)

# Create our database model
class Question(db.Model):
    __tablename__ = "questions"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(140), unique=True)

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return '<Content %r>' % self.content

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
