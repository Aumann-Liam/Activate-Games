from flask import Flask, render_template, url_for

app = Flask(__name__)

categories = ['Category1', 'Category2', 'Category3', 'Category4', 'Category5', 'Category6']

questions = [{'Q1': ['Question1', 'Answer1', '200'],
              'Q2': ['Question2', 'Answer2', '400'],
              'Q3': ['Question3', 'Answer3', '600'],
              'Q4': ['Question4', 'Answer4', '800'],
              'Q5': ['Question5', 'Answer5', '1000']},
             {'Q1': ['Question1', 'Answer1', '200'],
              'Q2': ['Question2', 'Answer2', '400'],
              'Q3': ['Question3', 'Answer3', '600'],
              'Q4': ['Question4', 'Answer4', '800'],
              'Q5': ['Question5', 'Answer5', '1000']},
             {'Q1': ['Question1', 'Answer1', '200'],
              'Q2': ['Question2', 'Answer2', '400'],
              'Q3': ['Question3', 'Answer3', '600'],
              'Q4': ['Question4', 'Answer4', '800'],
              'Q5': ['Question5', 'Answer5', '1000']},
             {'Q1': ['Question1', 'Answer1', '200'],
              'Q2': ['Question2', 'Answer2', '400'],
              'Q3': ['Question3', 'Answer3', '600'],
              'Q4': ['Question4', 'Answer4', '800'],
              'Q5': ['Question5', 'Answer5', '1000']},
             {'Q1': ['Question1', 'Answer1', '200'],
              'Q2': ['Question2', 'Answer2', '400'],
              'Q3': ['Question3', 'Answer3', '600'],
              'Q4': ['Question4', 'Answer4', '800'],
              'Q5': ['Question5', 'Answer5', '1000']},
             {'Q1': ['Question1', 'Answer1', '200'],
              'Q2': ['Question2', 'Answer2', '400'],
              'Q3': ['Question3', 'Answer3', '600'],
              'Q4': ['Question4', 'Answer4', '800'],
              'Q5': ['Question5', 'Answer5', '1000']}]

@app.route('/')
@app.route('/HomePage')
def index():
    return render_template('HomePage.html')
  

@app.route('/')
@app.route('/Jeopardy')
def jeopardy():
    return render_template('Jeopardy.html', foo=(categories, questions))


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
