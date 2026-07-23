from flask import render_template
from flask_login import login_required

from app.dashboard import dashboard_bp


@dashboard_bp.route("/")
@login_required
def home():

    return render_template("dashboard.html")