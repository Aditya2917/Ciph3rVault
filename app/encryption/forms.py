from flask_wtf import FlaskForm

from wtforms import (
    TextAreaField,
    StringField,
    RadioField,
    SubmitField
)

from wtforms.validators import DataRequired


class EncryptionForm(FlaskForm):

    input_text = TextAreaField(
        "Input Text",
        validators=[DataRequired()]
    )

    secret_key = StringField(
        "Secret Key",
        validators=[DataRequired()]
    )

    operation = RadioField(

        "Operation",

        choices=[
            ("encrypt", "Encrypt"),
            ("decrypt", "Decrypt")
        ],

        default="encrypt"
    )

    submit = SubmitField("Run")