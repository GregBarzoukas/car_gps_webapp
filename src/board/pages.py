from flask import Blueprint, render_template


bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    return render_template("pages/home.html")

@bp.route("/about")
def about():
    markers = [
        {
            'lat': 0,
            'lon': 0,
            'popup': 'This is the middle of the map.'
        }
    ]
    return render_template("pages/about.html", markers=markers)