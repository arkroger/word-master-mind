# ./flask_app/patched.py
from gevent import monkey
monkey.patch_all() # we need to patch very early

from wordmastermind import app  # re-export