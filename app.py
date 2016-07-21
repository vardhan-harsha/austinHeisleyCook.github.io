from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutme')
def about():
  return render_template('/')

@app.route('/blog')
def blog():
  return render_template('blog.html')

@app.route('/jquerytest')

def jquerytest():
    return render_template('jquerytester.html')


if __name__ == '__main__':

  app.run(debug=True, host='127.0.0.1')
