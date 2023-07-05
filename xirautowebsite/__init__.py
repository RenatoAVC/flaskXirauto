from flask import Flask

app = Flask(__name__)

from xirautowebsite.core.views import core
app.register_blueprint(core)

from xirautowebsite.error_pages.handlers import error_pages
app.register_blueprint(error_pages)