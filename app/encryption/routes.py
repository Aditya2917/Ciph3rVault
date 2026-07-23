from flask import render_template

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
        try:
            print("Selected Operation:", form.operation.data)
            result = process_aes(
                form.input_text.data,
                form.secret_key.data,
                form.operation.data
            )

        except Exception as e:

            result = str(e)

    return render_template(
        "encryption.html",
        form=form,
        result=result
    )