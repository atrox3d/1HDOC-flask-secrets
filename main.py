from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
import util.logging
from util.logging import log_decorator
import util.network
import util.params
import logging

logger = logging.getLogger(__name__)
root = util.logging.get_root_logger()
app = Flask(__name__)
app.secret_key = "what-the-fuck"


@app.route("/")
@log_decorator
def home():
    return render_template('index.html')


class LoginForm(FlaskForm):
    name = StringField(label='email')
    password = PasswordField(label='password')
    submit = SubmitField(label='Log In')


@app.route("/login")
@log_decorator
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, host=util.network.get_ipaddress())
