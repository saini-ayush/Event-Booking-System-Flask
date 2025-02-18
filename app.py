
from flask import Flask, render_template
from flask_login import LoginManager, login_required
from app.models.user import User
from app.routes.auth_routes import auth_bp
from app.routes.event_routes import event_bp
from app.routes.booking_routes import booking_bp
import os

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"

@login_manager.user_loader
def load_user(user_id):
    return User.get_user_by_id(user_id)

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(event_bp)
app.register_blueprint(booking_bp)

@app.route("/")
@login_required
def home():
    return render_template("base.html")

if __name__ == "__main__":
    app.secret_key = os.getenv("SECRET_KEY")
    app.run(debug=True)
