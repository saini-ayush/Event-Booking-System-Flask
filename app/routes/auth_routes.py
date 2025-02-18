from flask import Blueprint, request, redirect, url_for, flash, render_template
from flask_login import login_user, logout_user, login_required
from app.models.user import User
from werkzeug.exceptions import BadRequest

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        try:
            username = request.form.get("username")
            password = request.form.get("password")
            
            if not username or not password:
                flash("Username and password are required", "danger")
                return render_template("login.html"), 400
            
            user = User.get_user_by_username(username)
            if user and user.check_password(password):
                login_user(user)
                # Get the next page from query parameters, defaulting to events page
                next_page = request.args.get('next', url_for('event.get_user_events'))
                return redirect(next_page)
            
            flash("Invalid username or password", "danger")
            return render_template("login.html"), 401
            
        except Exception as e:
            flash(f"An error occurred: {str(e)}", "danger")
            return render_template("login.html"), 500
            
    return render_template("login.html")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        try:
            username = request.form.get("username")
            password = request.form.get("password")
                
            if User.get_user_by_username(username):
                flash("Username already exists", "warning")
                return render_template("register.html"), 409
                
            User.create_user(username, password)
            flash("Account created successfully. Please log in.", "success")
            return redirect(url_for("auth.login"))
            
        except Exception as e:
            flash(f"An error occurred: {str(e)}", "danger")
            return render_template("register.html"), 500
            
    return render_template("register.html")

@auth_bp.route("/logout")
@login_required
def logout():
    try:
        logout_user()
        flash("Logged out successfully", "success")
        return redirect(url_for("auth.login"))
    except Exception as e:
        flash(f"An error occurred: {str(e)}", "danger")
        return redirect(url_for("auth.login")), 500