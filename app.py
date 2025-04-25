from flask import Flask, render_template
from flask_login import LoginManager, login_required, current_user
from models import users_db
from auth import auth

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Flask-Login config
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

# Registrar Blueprints
app.register_blueprint(auth)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username, role=current_user.role)

@login_manager.user_loader
def load_user(user_id):
    return next((u for u in users_db.values() if str(u.id) == str(user_id)), None)

if __name__ == '__main__':
    app.run(debug=True)
