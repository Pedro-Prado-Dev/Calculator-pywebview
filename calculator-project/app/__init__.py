from flask import Flask

server = Flask(__name__, static_folder='./assets', template_folder='./templates')

from app import routes