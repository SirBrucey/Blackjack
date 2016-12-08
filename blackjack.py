import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import redis

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

app.config.update(dict(
  SECRET_KEY='development key',
  USERNAME='admin',
  PASSWORD='testing'
))

@app.route('/')
def home():
  return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  error = None
  if request.method == 'POST':
    if (request.form['username'] != app.config['USERNAME']) or \
       (request.form['password'] != app.config['PASSWORD']):
      error = 'Invalid login'
    else:
      session['logged_in'] = True
      flash('You were logged in')
      return redirect(url_for('login'))
  return render_template('login.html', error=error)

@app.route('/logout')
def logout():
  session.pop('logged_in', None)
  flash('You were logged out')
  return redirect(url_for('login'))

if __name__ == '__main__':
  app.run()
