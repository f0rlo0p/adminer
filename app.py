#!/usr/bin/env python3
from flask import Flask,request,abort
import subprocess
app = Flask(__name__)

black_list = [''] # add your blacklist here
# for example | dangerous file | /etc/passwd 

@app.route('/')
def index():
  r = request.args.get('file','')
  if r not in black_list:
    return command(f'cat {r}')
  else:
    return abort(403)
def command(cmd):
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        return out
        
if __name__ == '__main__':
  app.run()
