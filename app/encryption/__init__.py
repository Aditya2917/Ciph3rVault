from flask import Blueprint

encryption_bp = Blueprint(
    "encryption",
    __name__,
    template_folder="templates"
)

from app.encryption import routes