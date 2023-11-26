"""
from flask_app.models.burger import Burger
@app.route('/create', methods=['POST'])
def create_burger():
    # if there are errors:
    # We call the staticmethod on Burger model to validate
 if not Burger.validate_burger(request.form):
        # redirect to the route where the burger form is rendered.
        return redirect('/')
    # else no errors:
    Burger.save(request.form)
    return redirect("/burgers")




"""