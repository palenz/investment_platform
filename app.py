from flask import Flask, render_template
from controllers.company_controller import companies_blueprint
from controllers.investor_controller import investors_blueprint
from controllers.investment_controller import investments_blueprint

# This is the app per se. The blueprints, which are like mini-apps, include the controllers
# for each class/table.

app = Flask(__name__)

app.register_blueprint(companies_blueprint)
app.register_blueprint(investors_blueprint)
app.register_blueprint(investments_blueprint)

# This registers the flask blueprints in the app

@app.route('/')
def home():
    number_of_investors = 1
    return render_template('index.html', number_of_investors=number_of_investors)

if __name__ == '__main__':
    app.run(debug=True) 