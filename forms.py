"""Forms for our demo Flask app."""

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, AnyOf


class AddPetForm(FlaskForm):
    """Form for adding a new Pet."""

    name = StringField("Pet name", validators=[InputRequired()])

    species = StringField("Species",
        validators=[InputRequired(),
            AnyOf(values=['cat', 'dog', 'porcupine'])])

    photo_url = StringField("Photo", validators=[URL(), Optional()])

    age = StringField("Age",
        validators=[InputRequired(),
            AnyOf(values=['baby', 'young', 'adult', 'senior'])])

    notes = TextAreaField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form for editing an existing Pet."""

    photo_url = StringField("Photo", validators=[URL(), Optional()])

    available = BooleanField("Available")

    notes = TextAreaField("Notes", validators=[Optional()])