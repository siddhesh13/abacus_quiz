from flask import Flask, render_template, request
import requests


app = Flask(__name__)

rightAnswers = ["d","b","a","c","b","d","b","c","a","b"]
answers=["1","2","3","4","5","6","7","8","9","10"]
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/basic')
def basic():
    return render_template('basic.html')
@app.route('/mover1')
def mover1():
    return render_template('mover1.html')
@app.route('/mover2')
def mover2():
    return render_template('mover2.html')
@app.route('/mover3')
def mover3():
    return render_template('mover3.html')
@app.route('/mover4')
def mover4():
    return render_template('mover4.html')
@app.route('/mover5')
def mover5():
    return render_template('mover5.html')
@app.route('/advance1')
def advance1():
    return render_template('advance1.html')
@app.route('/advance2')
def advance2():
    return render_template('advance2.html')
@app.route('/grand1')
def grand1():
    return render_template('grand1.html')

@app.route('/basic_un')
def basic1():
    return render_template('basic1.html')
@app.route('/mover_un')
def mover11():
    return render_template('mover11.html')
@app.route('/mover_dos')
def mover21():
    return render_template('mover21.html')
@app.route('/mover_tres')
def mover31():
    return render_template('mover31.html')
@app.route('/mover_cuatro')
def mover41():
    return render_template('mover41.html')
@app.route('/mover_cinco')
def mover51():
    return render_template('mover51.html')
@app.route('/advance_un')
def advance11():
    return render_template('advance11.html')
@app.route('/advance_dos')
def advance21():
    return render_template('advance21.html')
@app.route('/grand_un')
def grand11():
    return render_template('grand11.html')

@app.route('/grand2')
def grand2():
    return render_template('grand2.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        marks=0
        name = request.form['email']
        level = request.form['level']
        timeTaken = request.form['time']
        answers[0] = request.form['q1']
        answers[1] = request.form['q2']
        answers[2] = request.form['q3']
        answers[3] = request.form['q4']
        answers[4] = request.form['q5']
        answers[5] = request.form['q6']
        answers[6] = request.form['q7']
        answers[7] = request.form['q8']
        answers[8] = request.form['q9']
        answers[9] = request.form['q10']
        print(answers)
        for i in range(10):
            if answers[i]==rightAnswers[i]:
                marks=marks+5
        firstValue = name+ "-" + level
        secondValue = timeTaken
        fourthValue = answers[0] + "," + answers[1] + ","+ answers[2] + ","+ answers[3] + ","+ answers[4] + ","+ answers[5] + ","+ answers[6] + ","+ answers[7] + ","+ answers[8] + ","+ answers[9]
        thirdValue = str(marks) + " ["+ fourthValue +"]"
        print("trigger ifttt")
        email_alert(firstValue, secondValue, thirdValue)
        marks=0
        # print(customer, dealer, rating, comments)
        #if customer == '' or dealer == '':
            #return render_template('index.html', message='Please enter required fields')
        #if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
            #data = Feedback(customer, dealer, rating, comments)
            #db.session.add(data)
            #db.session.commit()
            #send_mail(customer, dealer, rating, comments)
        return render_template('success.html')
        #return render_template('index.html', message='You have already submitted feedback')

def email_alert(first, second, third):
    report = {}
    
    report["value1"] = first
    report["value2"] = second
    report["value3"] = third
    requests.post("https://maker.ifttt.com/trigger/quiz_results/with/key/iYiYhj3KyPFEwyVRuJzEb", data=report)    
    print(first)
    print(second)
    print(third)
if __name__ == '__main__':
    app.run(port='8000')
