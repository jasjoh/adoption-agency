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

    # TODO: Use a String() instead of Text
    name = db.Column(
        db.Text,
        nullable=False,
    )

    # TODO: Use a String() instead of Text
    species = db.Column(
        db.Text,
        nullable=False,
    )

    # TODO: Make not nullable - we don't not know, we just either have or don't
    photo_url = db.Column(
        db.Text,
        default='',
    )

    # TODO: Use a String() instead of Text
    age = db.Column(
        db.Text,
        nullable=False,
    )

    # TODO: Make not nullable - we don't not know, we just either have or don't
    notes = db.Column(
        db.Text
    )

    available = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )
