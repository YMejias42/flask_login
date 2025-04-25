from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# Simulación de base de datos en memoria
users_db = {}

class User(UserMixin):
    def __init__(self, id, username, password, role):
        self.id = id
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.role = role

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return str(self.id)

# Crear usuarios de prueba
users_db['admin'] = User(id=1, username='admin', password='1234', role='admin')
users_db['user'] = User(id=2, username='user', password='abcd', role='viewer')
