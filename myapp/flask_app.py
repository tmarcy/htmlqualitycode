
import logging
import myapp.app_config
import appengine_config

from flask import Flask
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.config.from_object(__name__)

if appengine_config.GAE_DEV:
    logging.info('using a dummy secret key')
    app.secret_key = 'my-secrete-key'
    app.debug = True
else:
    app.secret_key = myapp.app_config.app_secure_key

DEBUG = True
csrf = CSRFProtect(app)


