from flask_wtf import Form
from wtforms import TextField, BooleanField, TextAreaField, SubmitField, StringField, validators, ValidationError
from wtforms.validators import DataRequired, InputRequired


class ContactForm(Form):
  name = StringField('Ime in priimek otroka:', validators=[DataRequired("Prosimo, vpišite svoje polno ime.")])
  birth = StringField('Datum rojstva otroka:', validators=[DataRequired("Prosimo, vpišite datum rojstva.")])
  school = StringField("Šola, ki jo obiskuje otrok:", validators=[DataRequired("Prosimo, vpišite šolo, ki jo obiskuje.")])
  year = StringField("Razred, ki ga obiskuje otrok:", validators=[DataRequired("Prosimo, vpišite razred, ki ga obiskuje.")])
  """phone = StringField('Telefon', validators=[DataRequired("Prosimo, vpišite svojo telefonsko številko.")])"""
  names = StringField("Ime in priimek staršev:", validators=[DataRequired("Prosimo, vpišite datum rojstva.")])
  email = StringField('Email naslov staršev:', validators=[DataRequired("Prosimo, vpišite email staršev."),
                                                   validators.Email("Prosimo, vpišite svoj email.")])
  phone = StringField('Telefonska številka staršev:', [validators.optional(strip_whitespace=True)])
  subject = StringField('Zadeva:', validators=[DataRequired("Prosimo, vpišite zadevo.")])
  message = TextAreaField('Dodatna vprašanja:', [validators.optional(strip_whitespace=True)])
  """message = TextAreaField('Sporočilo', validators=[DataRequired("Prosimo, vpišite sporočilo, ki nam ga želite poslati.")])"""
  submit = SubmitField("Pošlji")