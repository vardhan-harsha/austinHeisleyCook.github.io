from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  
    return render_template('index.html')

@app.route('/aboutme')
def about():
  return render_template('/')
@a
def blog():
  return render_template('/blog')

@app.route


if __name__ == '__main__':

  app.run(debug=True, host='127.0.0.1')
