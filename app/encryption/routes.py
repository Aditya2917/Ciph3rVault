from flask import render_template, flash

from flask_login import login_required

from app.encryption import encryption_bp
from app.encryption.forms import EncryptionForm
from app.encryption.services import process_aes


@encryption_bp.route("/encryption", methods=["GET", "POST"])
@login_required
def encryption():

    form = EncryptionForm()

    result = ""

    if form.validate_on_submit():
        print("FORM SUBMITTED")
        success, result = process_aes(
    form.input_text.data,
    form.secret_key.data,
    form.operation.data
)
        if success:
            flash("Operation completed successfully.", "success")
        else:
            flash(result, "danger")

    return render_template(
        "encryption.html",
        form=form,
        result=result
    )