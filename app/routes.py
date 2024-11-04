from flask import render_template

from app import app
from .rqsts import p2i

@app.route('/')
@app.route('/index')
def index():
    image,text=p2i()
    return render_template('outpage.html',image=image,text=text)