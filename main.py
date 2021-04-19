# https://www.udemy.com/course/100-days-of-code/learn/lecture/22407116#overview

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap


import util.logging
from util.logging import log_decorator
import util.network
import util.params

import logging

logger = logging.getLogger(__name__)
root = util.logging.get_root_logger()
app = Flask(__name__)
Bootstrap(app)
app.secret_key = "what-the-fuck"


@app.route("/")
@log_decorator
def home():
    return render_template('index.html')


class LoginForm(FlaskForm):
    name = StringField(label='name', validators=[DataRequired()])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=8)])
    email = StringField(
        label='email',
        validators=[Email()]
    )
    submit = SubmitField(label='Log In')


@app.route("/login", methods=['GET', 'POST'])
@log_decorator
def login():
    form = LoginForm()
    logger.info(f"method is {request.method}")
    if request.method == "POST":
        if form.validate_on_submit():
            if form.email.data == 'admin@email.com' and form.password.data == '12345678':
                return render_template('success.html')
            else:
                return render_template('denied.html')
    # always render login.html,
    # whether method is GET or
    # form.validate_on_submit is False
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, host=util.network.get_ipaddress())
