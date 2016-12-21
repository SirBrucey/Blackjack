import os
import sys
from logging import Formatter, FileHandler

APP_HOME = r"/var/www/blackjack"


activate_this = os.path.join("/var/www/blackjack/venv/bin/activate_this.py")
execfile(activate_this, dict(__file__=activate_this))

sys.path.insert(0, APP_HOME)
os.chdir(APP_HOME)

from blackjack import app

application = app
