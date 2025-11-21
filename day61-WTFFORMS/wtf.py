from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import secrets

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)


@app.route("/")
def home():
    return render_template('index.html')

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In")

# @app.route("/login", methods=["GET", "POST"])
# def login():
#     form = LoginForm()
#
#     if form.validate_on_submit():   # <--- VALIDATES THE FORM
#         print("Form is valid!")
#         print("Email:", form.email.data)
#         print("Password:", form.password.data)
#         # Do your login logic here
#         return "Login successful!"
#
#     # If GET request or form invalid → return form with errors
#     return render_template('login.html', form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)



if __name__ == '__main__':
    app.run(debug=True)
