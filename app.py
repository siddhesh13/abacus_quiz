from flask import Flask, render_template, request


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['email']
        level = request.form['levelr']
        #rating = request.form['rating']
        answer1 = request.form['q1']
        answer2 = request.form['q2']
        answer3 = request.form['q3']
        answer4 = request.form['q4']
        answer5 = request.form['q5']
        answer6 = request.form['q6']
        answer7 = request.form['q7']
        answer8 = request.form['q8']
        answer9 = request.form['q9']
        answer10 = request.form['q10']
        firstValue = name+ " " + level
        secondValue = "timeTaken"
        thirdValue = answer1 + "," + answer2 + ","+ answer3 + ","+ answer4 + ","+ answer4 + ","+ answer5 + ","+ answer6 + ","+ answer7 + ","+ answer8 + ","+ answer9 + ","+ answer10
        email_alert(firstValue, secondValue, thirdValue)
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
    requests.post("https://maker.ifttt.com/trigger/YourEventName/with/key\
    /iYiYhj3KyPFEwyVRuJzEb", data=report)    
    print(first)
    print(second)
    print(third)
if __name__ == '__main__':
    app.run()
