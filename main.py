from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    text = 'ovo je početna stranica!'
    return render_template('index.html',text=text)

@app.route('/columns_equal_3')
def columns_equal_3():  
    return render_template('columns_equal_3.html')

@app.route('/columns_unequal_2')
def columns_unequal_2():  
    return render_template('columns_unequal_2.html')

@app.route('/columns_unequal_3')
def columns_unequal_3():  
    return render_template('columns_unequal_3.html')

# Error pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
