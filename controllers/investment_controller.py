from flask import Flask, Blueprint, render_template, request, redirect
from models.investment import Investment
import repositories.company_repository as company_repository
import repositories.investment_repository as investment_repository
import repositories.investor_repository as investor_repository

investments_blueprint = Blueprint("investments", __name__)

@investments_blueprint.route("/investments")
def investments():
    investments = investment_repository.select_all()
    return render_template("investments/index.html", investments=investments)

@investments_blueprint.route("/investments/new", methods=['GET'])
def new_investment():
    investors = investor_repository.select_all()
    companies = company_repository.select_all()
    return render_template("investments/new.html", investors=investors, companies=companies)

@investments_blueprint.route("/investments", methods=['POST'])
def create_investment():
    investor_id = request.form['investor_id']
    company_id = request.form['company_id']
    equity = request.form['equity']
    payment = request.form['payment']
    date_of_investment = request.form['date_of_investment']
    
    investor = investor_repository.select(investor_id)
    company = company_repository.select(company_id)
    investment = Investment(investor, company, equity, payment, date_of_investment)
    investment_repository.save(investment)

    return redirect('/investments')

@investments_blueprint.route("investments/<id>/delete", methods=['POST'])
def delete_investment(id):
    investment_repository.delete(id)
    return redirect('/investments')