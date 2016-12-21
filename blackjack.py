import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from wtforms import Form, BooleanField, StringField, PasswordField, validators
import redis

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

app.config.update(dict(
  SECRET_KEY='development key',
  USERNAME='admin',
  PASSWORD='test'
))

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if _loggedIn(): return redirect(url_for('home'))
  error = None
  if request.method == 'POST':
    if (request.form['username'] != app.config['USERNAME']) or \
       (request.form['password'] != app.config['PASSWORD']):
      error = 'Invalid login'
    else:
      session['logged_in'] = True
      flash('You were logged in')
      return redirect(url_for('home'))
  return render_template('login.html', error=error)

@app.route('/logout')
def logout():
  if not _loggedIn(): return redirect(url_for('home'))
  session.pop('logged_in', None)
  flash('You were logged out')
  return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
  if _loggedIn(): return redirect(url_for('home'))
  if request.method == 'POST':
    session['logged_in'] = True
    flash('Thanks for registering')
    return redirect(url_for('home'))
  return render_template('register.html')

# Use for pages that EU can only see if logged out
# Redircts to home
def _loggedIn():
  if "logged_in" in session:
    return True
  else:
    return False

if __name__ == '__main__':
  app.run(debug=True)   # Remove debug=True before making app live
