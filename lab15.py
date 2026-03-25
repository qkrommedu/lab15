# hello_flask.py
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5


# create an instance of Flask
app = Flask(__name__)
bootstrap = Bootstrap5(app)

# route decorator binds a function to a URL
@app.route('/')
def hello():
  return '<p>Mason Melendy: LASER</p>'
@app.route('/mytemplate')
def t_test():
   return render_template('my_template_1.html')
