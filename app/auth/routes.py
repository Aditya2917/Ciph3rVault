from flask import (
    render_template,
    redirect,
    url_for,
    flash,
    request
)

from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user
)

from app.auth import auth_bp
from app.auth.forms import RegisterForm, LoginForm
from app.auth.services import (
    create_user,
    authenticate_user
)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if current_user.is_authenticated:
        return redirect(url_for("dashboard.home"))

    form = RegisterForm()

    if form.validate_on_submit():

        success, message = create_user(
            form.username.data,
            form.email.data,
            form.password.data
        )

        if success:

            flash(message, "success")

            return redirect(url_for("auth.login"))

        flash(message, "danger")

    return render_template(
        "register.html",
        form=form
    )


@auth_bp.route("/login", methods=["GET", "POST"])
@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for("dashboard.home"))

    form = LoginForm()

    if form.validate_on_submit():

        user = authenticate_user(
            form.email.data,
            form.password.data
        )

        if user:

            login_user(
                user,
                remember=form.remember.data
            )

            flash(
                "Welcome back!",
                "success"
            )

            next_page = request.args.get("next")

            return redirect(
                next_page or url_for("dashboard.home")
            )

        flash(
            "Invalid email or password.",
            "danger"
        )

    return render_template(
        "login.html",
        form=form
    )


@auth_bp.route("/logout")
@login_required
def logout():

    logout_user()

    flash(
        "Logged out successfully.",
        "success"
    )

    return redirect(
        url_for("auth.login")
    )