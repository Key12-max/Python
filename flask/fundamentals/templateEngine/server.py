from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes
@app.route('/')
def index():
    return render_template("index.html", phrase="hello", times=5)	# notice the 2 new named arguments!
#to render the form
@app.route('/users')
def form():
    return render_template("form.html")
#post form submisition which is processing the form
@app.route('/users',methods=["POST"])
def create_user():
    print(request.form)
    #display the created user in the front end
    #accessing the data using request.form["name"], but can not access them in the show method without session

    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect("/show")
#need to route to display 
@app.route('/show')
def show():
    print("showing the user info from the form")
    print(request.form)
    """Previously in our show_user function, we didn't have access to the name and email from the form submission. Now, because of session, we have a way to access the name and email in a different function!"""
    return render_template('show.html', name_on_template=session['username'], email_on_template=session['useremail'])

""" As developers we should never render a template on a POST request.  If we do, then it could result in some disastrous consequences.

Duplication of Data in your application.
Over-Charging Credit Cards ( if processing payments ).  """


if __name__=="__main__":
    app.run(debug=True)

