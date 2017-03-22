#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request,session
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from forms import *
import os
from flask import json
import urllib2

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
#db = SQLAlchemy(app)

# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def home():
    return render_template('pages/placeholder.home.html')


@app.route('/about',methods=['GET','POST'])
def about():
    data = json.dumps({"username": session['username'],"requestCode": "GET_POST"}).encode('utf-8')
    u = urllib2.Request("http://10.20.3.111:6000/", data, {"Content-Type": "application/json"})
    f = urllib2.urlopen(u)
    response = f.read()
    f.close()
    print data
    print u
    print response
    res = json.loads(response)
    for i in res['POSTS']:
        print i['Category']
    return render_template('pages/placeholder.about.html')


@app.route('/login',methods=['GET','POST'])
def login():
    forms= LoginForm(request.form)
    if request.method == "POST":
        user = request.form['name']
        pswd = request.form['password']
        print user, pswd
        data = json.dumps({"username": user, "password": pswd, "requestCode": "LOGIN"}).encode('utf-8')
        u = urllib2.Request("http://10.20.3.111:6000/", data, {"Content-Type": "application/json"})
        f = urllib2.urlopen(u)
        response = f.read()
        f.close()
        print data
        print u
        print response
        res=json.loads(response)
        session['username']=user
        if res['SERVER_RESPONSE']=='1':
            print "Successful"
        else:
            print "Unsuccessful"
    return render_template('forms/login.html', form=forms)

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    u=session['username']
    print u
    if request.method == "POST":
        user = request.form['name']
        pswd = request.form['password']
        email=request.form['email']
        pswd2=request.form['confirm']
        phone=request.form['phone']
        address=request.form['address']
        print user, pswd
        if pswd==pswd2:
            data = json.dumps({"username": user, "password": pswd,"email":email,"contact":phone,"address":address, "requestCode": "REGISTER"}).encode('utf-8')
            u = urllib2.Request("http://10.20.3.111:6000/", data, {"Content-Type": "application/json"})
            f = urllib2.urlopen(u)
            response = f.read()
            f.close()
            print data
            print u
            print response
        else:
            return render_template('forms/register.html', form=form)
    return render_template('forms/register.html', form=form)

@app.route('/post',methods=['GET','POST'])
def post():
    form = PostForm(request.form)
    if request.method == "POST":
        user=session['username']
        phone="b"
        email="c"
        address="d"
        title = request.form['title']
        category = request.form['category']
        details=request.form['details']
        postDate=request.form['postDate']
        data = json.dumps({"username": user, "title": title,"category":category,"details":details,"postDate":postDate,"contact":phone,"email":email,"address":address, "requestCode": "CREATE_POST"}).encode('utf-8')
        u = urllib2.Request("http://10.20.3.111:6000/", data, {"Content-Type": "application/json"})
        f = urllib2.urlopen(u)
        response = f.read()
        f.close()
        print data
        print u
        print response
    return render_template('forms/post.html', form=form)


@app.route('/forgot')
def forgot():
    form = ForgotForm(request.form)
    return render_template('forms/forgot.html', form=form)

# Error handlers.


@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
