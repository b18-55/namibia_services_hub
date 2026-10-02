from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///services.db'
db = SQLAlchemy(app)

class ServiceProvider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    opening_hours = db.Column(db.String(100))
    description = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "location": self.location,
            "phone": self.phone,
            "email": self.email,
            "opening_hours": self.opening_hours,
            "description": self.description
        }

@app.route('/')
def home():
    return {"message": "Namibia Services Hub API is running"}

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)