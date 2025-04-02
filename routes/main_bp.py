from pprint import pprint

from flask import Blueprint, render_template, request

HTTP_NOT_FOUND = 404
main_bp = Blueprint("main_bp", __name__)

#  API / Endpoint
name = "Nia"
hobbies = ["Gaming", "Reading", "Soccer", "Ballet", "Gyming", "Yoga"]


profiles = [
    {
        "name": "Kuromi",
        "image": "https://th.bing.com/th/id/OIP.PynAxQUy7QUOwXbCv0RP2QHaHa?rs=1&pid=ImgDetMain",
        "isVerified": True,
    },
    {
        "name": "Melody",
        "image": "https://th.bing.com/th/id/OIP.70zFTnd4dntTQwCdPSJvjQHaHa?rs=1&pid=ImgDetMain",
        "isVerified": True,
    },
    {
        "name": "Kitty",
        "image": "https://th.bing.com/th/id/OIP.P5CGJN00cxOObMGZ2NLllgHaHa?rs=1&pid=ImgDetMain",
        "isVerified": True,
    },
]


@main_bp.get("/")
def hello_world():
    return render_template("home.html")


@main_bp.get("/about")
def about_page():
    return render_template("about.html", name=name, hobbies=hobbies)


@main_bp.get("/profile")
def profile_page():
    return render_template("profile.html", profiles=profiles)
