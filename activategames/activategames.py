from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/HomePage')
def index():
    return render_template('HomePage.html')


@app.route('/')
@app.route('/Jeopardy')
def jeopardy():
    return render_template('Jeopardy.html')


@app.route('/')
@app.route('/FF')
def fam_feud():
    return render_template('FF.html')

@app.route('/')
@app.route('/answers')
def answers():
    return render_template('answer.html')

if __name__ == "__main__":
    app.run(debug=True)
