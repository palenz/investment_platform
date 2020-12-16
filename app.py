from flask import Flask, render_template
from controllers.company_controller import companies_blueprint
from controllers.investor_controller import investors_blueprint
from controllers.investment_controller import investments_blueprint
import repositories.investor_repository as investor_repository
import repositories.investment_repository as investment_repository
import repositories.company_repository as company_repository

# This is the app per se. The blueprints, which are like mini-apps, include the controllers
# for each class/table.

app = Flask(__name__)

app.register_blueprint(companies_blueprint)
app.register_blueprint(investors_blueprint)
app.register_blueprint(investments_blueprint)

# This registers the flask blueprints in the app

@app.route('/')
def home():
    number_of_investors = investor_repository.count()
    total_invested = investment_repository.total_invested()
    total_companies = company_repository.count()
    return render_template('index.html', number_of_investors=number_of_investors, total_invested=total_invested, total_companies=total_companies)

if __name__ == '__main__':
    app.run(debug=True) 