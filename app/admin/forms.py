
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class AdminDetailsForm(FlaskForm):
    """
    Form for entering admin details during the registration process.

    Attributes:
    - username (StringField): User's desired username.
    - email (StringField): User's email address.
    - fullname (StringField): User's full name.
    - password (PasswordField): User's chosen password.
    - confirm_password (PasswordField): Confirmatory password to ensure accuracy.
    - submit (SubmitField): Button to submit the form.

    Validators:
    - username: Required, with a length between 4 and 50 characters.
    - email: Required, with a valid email format.
    - fullname: Required, with a maximum length of 100 characters.
    - password: Required, with a minimum length of 8 characters.
    - confirm_password: Required, with a minimum length of 8 characters, and must match the 'password' field.
    """
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    fullname = StringField('Full Name', validators=[DataRequired(), Length(max=100)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=8), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Create Admin')


class VerifyOTPForm(FlaskForm):
    """
    Form for verifying the OTP during the admin registration process.

    Attributes:
    - otp (StringField): Input field for entering the OTP.
    - submit (SubmitField): Button to submit the form.

    Validators:
    - otp: Required, with a length between 6 and 6 characters.
    """
    otp = StringField('OTP', validators=[DataRequired(), Length(min=6, max=6, message='OTP must be 6 digits')])
    submit = SubmitField('Verify OTP')