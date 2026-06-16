from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/quiz')
def quiz():
    return render_template('quiz.html')
@app.route('/result', methods=['POST'])
def result():

    score = 0

    if request.form.get('q1') == 'b':
        score += 1

    if request.form.get('q2') == 'a':
        score += 1

    if request.form.get('q3') == 'a':
        score += 1

    return render_template('result.html', score=score)
if __name__ == '__main__':
    app.run(debug=True)
print("hi")
