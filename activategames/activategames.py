from flask import Flask, render_template, url_for

app = Flask(__name__)


questions = {'Category1': {'Box1': ['Question1', 'Answer2'],
                           'Box2': ['Question2', 'Answer2'],
                           'Box3': ['Question3', 'Answer3'],
                           'Box4': ['Question4', 'Answer4'],
                           'Box5': ['Question5', 'Answer5']},
             'Category2': {'Box1': ['Question1', 'Answer2'],
                           'Box2': ['Question2', 'Answer2'],
                           'Box3': ['Question3', 'Answer3'],
                           'Box4': ['Question4', 'Answer4'],
                           'Box5': ['Question5', 'Answer5']},
             'Category3': {'Box1': ['Question1', 'Answer2'],
                           'Box2': ['Question2', 'Answer2'],
                           'Box3': ['Question3', 'Answer3'],
                           'Box4': ['Question4', 'Answer4'],
                           'Box5': ['Question5', 'Answer5']},
             'Category4': {'Box1': ['Question1', 'Answer2'],
                           'Box2': ['Question2', 'Answer2'],
                           'Box3': ['Question3', 'Answer3'],
                           'Box4': ['Question4', 'Answer4'],
                           'Box5': ['Question5', 'Answer5']},
             'Category5': {'Box1': ['Question1', 'Answer2'],
                           'Box2': ['Question2', 'Answer2'],
                           'Box3': ['Question3', 'Answer3'],
                           'Box4': ['Question4', 'Answer4'],
                           'Box5': ['Question5', 'Answer5']}
             }

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
