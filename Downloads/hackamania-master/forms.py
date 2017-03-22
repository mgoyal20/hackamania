from flask_wtf import Form
from wtforms import TextField, PasswordField, DateField
from wtforms.validators import DataRequired, EqualTo, Length

# Set your classes here.


class RegisterForm(Form):
    name = TextField(
        'Username', validators=[DataRequired(), Length(min=6, max=25)]
    )
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=6, max=40)]
    )
    confirm = PasswordField(
        'Repeat Password',
        [DataRequired(),
        EqualTo('password', message='Passwords must match')]
    )
    phone = TextField(
        'Phone Number', validators=[DataRequired(), Length(min=10)]
    )
    address = TextField(
        'Address', validators=[DataRequired(), Length(min=6, max=100)]
    )


class LoginForm(Form):
    name = TextField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])


class ForgotForm(Form):
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )
class PostForm(Form):
    title = TextField(
        'Title', validators=[DataRequired(), Length(min=6, max=25)]
    )
    category = TextField(
        'Category', validators=[DataRequired(), Length(min=6, max=40)]
    )
    details = TextField(
        'Details', validators=[DataRequired(), Length(min=10, max= 300)]
    )
    postDate = DateField(
	'Date'
    )

