from flask import session
import os

def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = os.urandom(16).hex()
    return session['_csrf_token']
