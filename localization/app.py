#!/usr/bin/env python3
"""
babel translation example
"""

from flask import Flask, request
from flask_babel import Babel, _, ngettext

app = Flask(__name__)
babel = Babel(app)

# Configure default locale and translations directory
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = './translations'

@babel.localeselector
def get_locale():
    # Select locale from user request Accept-Language headers
    return request.accept_languages.best_match(['en', 'fr'])

@app.route('/')
def index():
    greeting = _("Hello, World!")

    num_count= 3 
    # Choose message based on num_count
    message = ngettext(
        "You have one message",
        "You have %(num)d messages",
        num_count
    ) % {'num': num_count}

    return f"{greeting} {message}"

if __name__ == "__main__":
    app.run(debug=True)
