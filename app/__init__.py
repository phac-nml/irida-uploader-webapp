from flask import Flask, redirect, session
from app.mod_tables.models import TableBuilder, TextBuilder


flask_app = Flask(__name__)

table_builder = TableBuilder()
text_builder = TextBuilder()


from app.common.routes import main
from app.mod_tables.controllers import tables


# init uploader config
from iridauploader import config as uploader_config
from app.config import CONFIG_FILE

uploader_config.set_config_file(CONFIG_FILE)
uploader_config.setup()

# Register the different blueprints
flask_app.register_blueprint(main)
flask_app.register_blueprint(tables)
