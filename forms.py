from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError
#from wtforms.validators import ValidationError, DataRequired, Email, Length
class ContactForm(Form):
  name = TextField("Name",  [validators.Required("Please enter your name.")])
  email = TextField("Email",  [validators.Required(), validators.Email()])
  subject = TextField("Subject",  [validators.Required("Please enter a subject.")])
  message = TextAreaField("Message",  [validators.Required("Please enter a message.")])

  submit = SubmitField("Send")

