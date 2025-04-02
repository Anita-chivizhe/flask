from operator import ge
from pprint import pprint
from sys import exception

from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from extensions import db
from models.user import Users

auth_bp = Blueprint("auth_bp", __name__)


@auth_bp.get("/login")
def login_page():
    return render_template("login.html")


@auth_bp.post("/login")
def submit_login_page():
    username = request.form.get("username")
    password = request.form.get("password")  # abc@123
    try:
        # 🛡️ Validations
        if not username:
            raise ValueError("Username must be filled")

        if not password:
            raise ValueError("Password must be filled")

        # Select * from users
        #   where username = 'Ethan'
        #   Limit 1;
        user_from_db = Users.query.filter_by(username=username).first()

        print(user_from_db)

        if not user_from_db:
            raise ValueError("Credentials are invalid")

        if not check_password_hash(user_from_db.password, password):
            raise ValueError("Credentials are invalid")
        login_user(user_from_db)

        return redirect(url_for("movies_list_bp.movie_list_page"))

    except Exception as e:
        print(e)
        db.session.rollback()
        return redirect(url_for("auth_bp.submit_login_page"))


@auth_bp.get("/signup")
def signup_page():
    return render_template("signup.html")


@auth_bp.post("/signup")
def submit_signup_page():
    password = request.form.get("password")
    # salt + password
    hashed_password = generate_password_hash(password)  # 16 -> salt length
    print(hashed_password)

    data = {
        "username": request.form.get("username"),
        "password": hashed_password,
    }

    try:
        if request.form.get("password") != request.form.get("confirm"):
            raise ValueError("Password does not match")

        new_user = Users(**data)
        db.session.add(new_user)
        db.session.commit()
        # Take them to login page
        return redirect(url_for("main_bp.hello_world"))
    except Exception as e:
        print(e)
        db.session.rollback()
        return redirect(url_for("auth_bp.submit_signup_page"))


@auth_bp.get("/logout")
def logout_page():
    logout_user()
    return redirect(url_for("auth_bp.submit_login_page"))
