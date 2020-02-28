from flask import Flask

app = Flask(__name__)

#imported at the bottom and not at the top of the script to avoid circular imports
from app import routes