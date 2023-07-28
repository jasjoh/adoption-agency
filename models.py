"""Demo file showing off a model for SQLAlchemy."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    app.app_context().push()
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """ A Pet. """

    __tablename__ = "pets"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
    )

    name = db.Column(
        db.Text,
        nullable = False,
    )

    species = db.Column(
        db.Text,
        nullable = False,
    )

    photo_url = db.Column(
        db.Text,
        default = '',
    )

    age = db.Column(
        db.Text,
        # db.CheckConstraint(age in ['baby', 'young', 'adult', 'senior']),
        nullable = False,
    )

    notes = db.Column(
        db.Text
    )

    available = db.Column(
        db.Boolean,
        nullable = False,
        default = True
    )

