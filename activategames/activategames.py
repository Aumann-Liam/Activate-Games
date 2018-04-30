from flask import Flask, render_template, url_for

app = Flask(__name__)

categories = ['Category1', 'Category2', 'Category3', 'Category4', 'Category5', 'Category6']

questions = [{'200': ['Question1', 'Answer2'],
              '400': ['Question2', 'Answer2'],
              '600': ['Question3', 'Answer3'],
              '800': ['Question4', 'Answer4'],
              '1000': ['Question5', 'Answer5']},
             {'200': ['Question1', 'Answer2'],
              '400': ['Question2', 'Answer2'],
              '600': ['Question3', 'Answer3'],
              '800': ['Question4', 'Answer4'],
              '1000': ['Question5', 'Answer5']},
             {'200': ['Question1', 'Answer2'],
              '400': ['Question2', 'Answer2'],
              '600': ['Question3', 'Answer3'],
              '800': ['Question4', 'Answer4'],
              '1000': ['Question5', 'Answer5']},
             {'200': ['Question1', 'Answer2'],
              '400': ['Question2', 'Answer2'],
              '600': ['Question3', 'Answer3'],
              '800': ['Question4', 'Answer4'],
              '1000': ['Question5', 'Answer5']},
             {'200': ['Question1', 'Answer2'],
              '400': ['Question2', 'Answer2'],
              '600': ['Question3', 'Answer3'],
              '800': ['Question4', 'Answer4'],
              '1000': ['Question5', 'Answer5']},
             {'200': ['Question1', 'Answer2'],
              '400': ['Question2', 'Answer2'],
              '600': ['Question3', 'Answer3'],
              '800': ['Question4', 'Answer4'],
              '1000': ['Question5', 'Answer5']}]

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
