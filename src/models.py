from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    birth_year = db.Column(db.String(120))
    eye_color = db.Column(db.String(120))
    hair_color = db.Column(db.String(120))
    homeworld_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    homeworld = db.relationship("Planets")
    gender = db.Column(db.String(120))
    height = db.Column(db.String(120))
    mass = db.Column(db.String(120))
    skin_color = db.Column(db.String(120))
    url = db.Column(db.String(120))
    created = db.Column(db.String(120))
    edited = db.Column(db.String(120))

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }
    

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    model = db.Column(db.String(120))
    vehicle_class = db.Column(db.String(120))
    manufacturer = db.Column(db.String(120))
    length = db.Column(db.String(120))
    cost_in_credits = db.Column(db.String(120))
    crew = db.Column(db.String(120))
    passengers = db.Column(db.String(120))
    max_atmosphering_speed = db.Column(db.String(120))
    cargo_capacity = db.Column(db.String(120))
    consumables = db.Column(db.String(120))
    url = db.Column(db.String(120))
    created = db.Column(db.String(120))
    edited = db.Column(db.String(120))


    def __repr__(self):
        return '<Vehicle %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    diameter = db.Column(db.String(120))
    rotation_period = db.Column(db.String(120))
    orbital_period = db.Column(db.String(120))
    gravity = db.Column(db.String(120))
    population = db.Column(db.String(120))
    climate = db.Column(db.String(120))
    terrain = db.Column(db.String(120))
    surface_water = db.Column(db.String(120))
    url = db.Column(db.String(120))
    created = db.Column(db.String(120))
    edited = db.Column(db.String(120))

    def __repr__(self):
        return '<Vehicle %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

   