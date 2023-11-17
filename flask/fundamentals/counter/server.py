from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def counter():
    if 'count' not in session:
        session['count']=0
    return render_template('counter.html')
@app.route('/increment')
def clickToAdd():
    session['count']+=1
    return redirect('/')
@app.route('/reset')
def clearsession():
    session.clear()
    return redirect('/')
@app.route('/form', methods = ['POST'])
def addValue():
    session['value'] = request.form['number']
    return redirect('/')
@app.route('/form')
def amount():
    return render_template('form.html')
if __name__ ==("__main__"):
    app.run(debug=True)