from app.models import user
from flask import request, render_template, redirect, session, flash, request
from app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# / root route for showing the login/registration page
@app.route("/")
def main_page():
    return render_template("login_reg.html")
# /dashboard - shows the dashboard - but you must be logged in
@app.route("/dashboard")
def dashboard():
    # Check to see if someone is logged if - if not, send them back to the login/registration page
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id": session["user_id"]
    }
    print("HERE")
    print(request.form)
    logged_user = user.User.get_by_id(data)
    return render_template("dashboard.html", user = logged_user)
    # Check to see if someone is logged in - if not, send them back to the login/registration page "/"

# /register (INVISIBLE POST route) - handles registering a newuser
@app.route("/register", methods=["POST"])
def register():
    print("HERE")
    print(request.form)
    if not user.User.validate_register(request.form):
        return redirect("/")
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": bcrypt.generate_password_hash(request.form['password']), # HASH THE PASSWORD FIRST!!!!
    }
    # Call on the model to save in the database
    session["user_id"] = user.User.register(data)     # Save the ID in session!!!
    # Redirect to /dashboard
    return redirect("/dashboard")
        #If the validations fail, redirect back to the route that had the form - redirect("/")
    # Save in the database  y creating a dictionary, then calling on the model in the database
    # Save the ID in session!!!
    # Redirect to /dashboard if it is successful

# /login (INVISIBLE POST route) - logs auser in
@app.route("/login", methods=["POST"])
def login():
    if not user.User.validate_login(request.form):
        return redirect("/")
    data = {
        "email": request.form["email"]
    }
    logged_in_user = user.User.get_by_email(data)
    session["user_id"] = logged_in_user.id
    return redirect("/dashboard")

# /logout (INVISIBLE route) - clears session, sends theuser back to login/registration page
@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')
    #clear session
    #redirect to "/"
