from flask import Flask, render_template, request, redirect
app = Flask(__name__)
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
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)

