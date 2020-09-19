#!/usr/bin/env python3
from flask import Flask,redirect,request,render_template,g,session,jsonify,abort
from libs import cmd as CMD
from core.tokengen import generate
import core.request
import core.reader
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect('database.db')

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.errorhandler(404)
def not_found(e):
    return 'Status : 404'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['POST'])
def login_page():
    user = request.form.get('username')
    password = request.form.get('password')
    if user == '80093ee2532' and password =='7d1271539e9590de3e57b416c5a4a97':
        return redirect('/admin')
    return redirect('/login')
@app.route('/admin')
@app.route('/admin/')
def admin_page():
    return render_tempate('admin.html')

@app.route('/api/<cmd>')
def api_cmd(cmd):
    commands = {
    'uname':'uname',
    'id':'id',
    'pwd':'pwd',
    'ls':'ls'
            }
    try:
        c = CMD(commands[cmd])
        return c
    except:
        return abort(404)
    #return redirect('/')
# for testing
token = generate(30)

@app.route('/api/read/')
def readforme():
    name = request.args.get('name',None)
    if name == None:
        return ''
    t = request.headers.get('Token',None)
    if t:
        if token == t:
            pass
    else:
        return abort(403)
    blacklist = 'YOUR_FILE.txt'
    if name == blacklist:
        return abort(404)
    if len(name) < 8:
        return abort(403)
    name = name.replace('"','').replace("'",'').replace(';','').replace('|','').replace('\n','').replace('&','').replace(' ','')
    c = CMD(f'cat {name}')
    return jsonify({'OUTPUT':c})
if __name__ == '__main__':
    app.run()
