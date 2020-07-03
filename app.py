#!/usr/bin/env python3
from flask import Flask,request,abort
import subprocess
app = Flask(__name__)
parameter = '' # your parameter . for example : file
# localhost/?file=hi.txt
black_list = 'example.txt' # add your blacklist here
# for example | dangerous file | /etc/passwd 

@app.errorhandler(404)
def show_404(e):
        return '<h3> <a href="https://github.com/f0rlo0p/thereader">TheReader </a>v0.6</h3><hr><br><h4> Status : 404 </h4>'
@app.route('/')
def index():
  r = request.args.get(parameter,'')
  return command(f'cat {r.replace(black_list,"")}').decode()
def command(cmd):
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        return out

if __name__ == '__main__':
  app.run(port=9090)
